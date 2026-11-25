#!/usr/bin/env python3
import os

import falcon.asgi
import pydgraph
from cassandra.cluster import Cluster
from pymongo import MongoClient


MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
MONGO_DATABASE = os.getenv("MONGO_DATABASE", "bookstore")
CASSANDRA_CLUSTER_IPS = [
    host.strip()
    for host in os.getenv("CASSANDRA_CLUSTER_IPS", "127.0.0.1").split(",")
    if host.strip()
]
DGRAPH_ADDRESS = os.getenv("DGRAPH_ADDRESS", "localhost:9080")

mongo_client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000,
)
db = mongo_client[MONGO_DATABASE]


def connect():
    cluster = Cluster(CASSANDRA_CLUSTER_IPS)
    session = cluster.connect()

    stub = pydgraph.DgraphClientStub(DGRAPH_ADDRESS)
    dgraph_client = pydgraph.DgraphClient(stub)

    return session, dgraph_client, db

app = falcon.asgi.App()

app.add_route("/users")
app.add_route("/users/friends")
app.add_route("/users/estadistic")
app.add_route("/users/history")
app.add_route("/users/habits")
app.add_route("/users/habits/history")
app.add_route("/users/{id}")
app.add_route("/habits")
app.add_route("/habits/{id}")
app.add_route("/challenges")
app.add_route("/challenges/{id}")
app.add_route("/categories")
app.add_route("/categories/{id}")
app.add_route("/updates")
app.add_route("/updates/{id}")
