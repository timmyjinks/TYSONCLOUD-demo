from typing import List

from fastapi import FastAPI, Response
from pydantic import BaseModel

import docker

client = docker.from_env()


class CreateContainer(BaseModel):
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


@app.post("/databases")
def get_containers():
    try:
        containers = client.containers.list(all=True)
        if len(containers) == 0:
            return []

        response = []
        for container in containers:
            contain = Container(
                id=container.id, name=container.name, status=container.status
            )
            response.append(contain)
        return response
    except NameError:
        # print(NameError)
        return Response(status_code=500)


@app.post("/database")
def create_container(create_container: CreateContainer):
    try:
        print(create_container)
        database_name = create_container.database_name

        client.containers.run(name=database_name, image="postgres", detach=True)
        container = client.containers.get(database_name)
        container_id = container.id

        return {"container_id": container_id}
    except NameError as e:
        print(e)
        return Response(status_code=500)
