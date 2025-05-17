from typing import List

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import docker

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
        print(username)
        containers = client.containers.list(
            all=True, filters={"label": f"username={username}"}
        )

        if len(containers) == 0:
            return []

        response = []
        for container in containers:
            if container.image.attrs["RepoTags"][0] == "postgres:latest":
                contain = Container(
                    id=container.id, name=container.name, status=container.status
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

        # labels for traefik
        labels = {
            "username": f"{create_container.username}",
            "url": f"{create_container.username}-{create_container.database_name}.tysonjenkins.dev",
        }
        client.containers.run(
            name=database_name,
            image="postgres",
            environment={
                "POSTGRES_USERNAME": create_container.database_username,
                "POSTGRES_PASSWORD": create_container.database_password,
            },
            labels=labels,
            detach=True,
        )
        container = client.containers.get(database_name)

        # if the container was able to successfully be created than go ahead and add a public url
        # for the database

        return Response(status_code=200)
    except NameError as e:
        print(e)
        return Response(status_code=500)
