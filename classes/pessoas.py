from bson import Regex
from pymongo import MongoClient


class Pessoas:
    filter = {}
    colletion = []

    def __init__(self, connection, database):
        """
        :parameter connection: Conexão feita via pymongo
        :type connection: MongoClient
        :parameter database: Banco de dados para conexão
        :type database: Str
        """
        self.connection = connection
        database = connection[database]
        self.colletion = database['Pessoas']

    def set_query(self, value):
        """
        :parameter value: Valor usado para fazer filtro nas buscas
        :type value: dict
        """
        self.filter = value

    def get_emitente(self):
        self.set_query({"_t": Regex(u".*Emitente.*", "i")})
        return self.return_one()

    def return_one(self):
        return self.colletion.find_one(self.filter)
