from typing import Dict, List

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import docker
from tunnel import *

client = docker.from_env()


class CreateContainer(BaseModel):
    username: str
    database_name: str
    database_username: str
    database_password: str


class GetContainers(BaseModel):
    container_ids: List[str]


class Container(BaseModel):
    id: str
    name: str
    status: str
    url: str


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/databases")
def get_containers(username=""):
    try:
        containers = client.containers.list(
            all=True, filters={"label": f"username={username}"}
        )

        if len(containers) == 0:
            return []

        response = []
        for container in containers:
            if container.image.attrs["RepoTags"][0] == "postgres:latest":
                contain = Container(
                    id=container.id,
                    name=container.name,
                    status=container.status,
                    url=container.labels["url"],
                )
                response.append(contain)
        return response
    except NameError:
        print(NameError)
        return Response(status_code=500)


@app.post("/database")
def create_container(create_container: CreateContainer):
    try:
        database_name = create_container.database_name

        url_subdomain = create_container.username + "-" + create_container.database_name
        # labels for traefik
        labels = {
            "username": f"{create_container.username}",
            "url": f"{url_subdomain}.tysonjenkins.dev",
        }
        client.containers.run(
            name=url_subdomain,
            image="postgres",
            hostname=url_subdomain,
            environment={
                "POSTGRES_USER": create_container.database_username,
                "POSTGRES_PASSWORD": create_container.database_password,
            },
            labels=labels,
            detach=True,
            network="frontend",
        )

        # if the container was able to successfully be created than go ahead and add a public url
        # for the database
        create_public_url(url_subdomain)

        return Response(status_code=200)
    except NameError as e:
        print(e)
        return Response(status_code=500)
