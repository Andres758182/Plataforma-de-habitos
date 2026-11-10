import logging
import falcon.asgi
import pydgraph
from cassandra.cluster import Cluster
from pymongo import MongoClient
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoggingMiddleware:
    async def process_request(self, req, resp):
        logger.info(f"Request: {req.method} {req.uri}")

    async def process_response(self, req, resp, resource, req_succeeded):
        logger.info(f"Response: {resp.status} for {req.method} {req.uri}")
        
stub = pydgraph.DgraphClientStub("localhost:9080")
client = pydgraph.DgraphClient(stub)

CLUSTER_IPS = os.getenv('CASSANDRA_CLUSTER_IPS', '127.0.0.1')
KEYSPACE = os.getenv('CASSANDRA_KEYSPACE', 'habits_project')
REPLICATION_FACTOR = os.getenv('CASSANDRA_REPLICATION_FACTOR', '1')

cliente = MongoClient("mongodb://localhost:27017/")
db = client.bookstore

app = falcon.asgi.App(middleware=[LoggingMiddleware()])


def connect():

    cluster = Cluster(CLUSTER_IPS.split(','))
    session = cluster.connect()

    try:
        pass
    finally:
        stub.close()

    return session, client, db