from pymongo import MongoClient


class Connection:
    mongo_client: MongoClient

    def __init__(self):
        self.mongo_client = MongoClient('mongodb://root:%7CcSFu%405rFv%23h8*%3D@localhost:12220/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&authSource=admin&authMechanism=SCRAM-SHA-1')

    def get_connection(self):
        return self.mongo_client

    def close(self):
        self.mongo_client.close()
