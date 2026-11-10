import falcon.asgi
import pydgraph
from cassandra.cluster import Cluster
from pymongo import MongoClient
import os

stub = pydgraph.DgraphClientStub("localhost:9080")
client = pydgraph.DgraphClient(stub)

CLUSTER_IPS = os.getenv('CASSANDRA_CLUSTER_IPS', '127.0.0.1')
KEYSPACE = os.getenv('CASSANDRA_KEYSPACE', 'habits_project')
REPLICATION_FACTOR = os.getenv('CASSANDRA_REPLICATION_FACTOR', '1')

cliente = MongoClient("mongodb://localhost:27017/")
db = client.bookstore

app = falcon.asgi.App()

def connect():

    cluster = Cluster(CLUSTER_IPS.split(','))
    session = cluster.connect()

    try:
        pass
    finally:
        stub.close()

    return session, client, db