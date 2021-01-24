from pymongo import MongoClient


class Connection:
    mongo_client: MongoClient
    host = '127.0.0.1'
    username = 'root'
    password = '|cSFu@5rFv#h8*='
    connectTimeoutMS = 10000
    authMechanism = 'SCRAM-SHA-1'
    authSource = 'admin'
    serverSelectionTimeoutMS = 5000
    port = 12220
    database = 'DigisatServer'

    def __init__(self):
        self.mongo_client = MongoClient(
            host=self.host,
            username=self.username,
            password=self.password,
            authSource=self.authSource,
            port=self.port,
            serverSelectionTimeoutMS=self.serverSelectionTimeoutMS,
            connectTimeoutMS=self.connectTimeoutMS,
            authMechanism=self.authMechanism
        )

    def get_connection(self):
        return self.mongo_client
