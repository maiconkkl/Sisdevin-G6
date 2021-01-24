from classes.pessoas import Pessoas
from classes.connection import Connection
from classes.generator import Generator

connection = Connection()
connection = connection.get_connection()
pessoas = Pessoas(connection, 'DigisatServer')
emitente = pessoas.get_emitente()
generator = Generator()
print()
generator.set_registro_10(
    cnpj=emitente['Cnpj'],

)