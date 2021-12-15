import re
from classes.pessoas import Pessoas
from classes.connection import Connection
from classes.generator import Generator
from classes.produto_servico import Produtos

db_con = Connection()
connection = db_con.get_connection()
pessoas = Pessoas(connection, 'DigisatServer')
emitente = pessoas.get_emitente()
generator = Generator()

responsavel_tecnico = ''
documento_tecnico = ''
tipo_empresa = ''
registro_mapa = ''

for x in emitente['CamposPersonalizado']:
    if x['TipoPersonalizado']['Descricao'].lower() == 'responsavel tecnico nome':
        responsavel_tecnico = x['Valor']

    if x['TipoPersonalizado']['Descricao'].lower() == 'responsavel tecnico documento':
        documento_tecnico = x['Valor']

    if x['TipoPersonalizado']['Descricao'].lower() == 'tipo empresa':
        tipo_empresa = x['Valor']

    if x['TipoPersonalizado']['Descricao'].lower() == 'registro mapa':
        registro_mapa = x['Valor']

if responsavel_tecnico == '':
    responsavel_tecnico = input('Nome do responsavel Tecnico, não foi cadastrado nos campos adicionais, '
                                'favor digitar\n')

if documento_tecnico == '':
    documento_tecnico = input('O Documento do responsavel Tecnico, não foi cadastrado nos campos adicionais, '
                              'favor digitar\n')
if tipo_empresa == '':
    tipo_empresa = input('O Tipo de de empresa, não foi cadastrado nos campos adicionais, favor digitar, opções:\n'
                         ' * 01 - Cantina Centra\n'
                         ' * 02 - Cantina Rural\n'
                         ' * 03 - Adega de Vinhos Finos\n'
                         ' * 04 - Engarrafador\n'
                         ' * 05 - Estandardizador\n'
                         ' * 06 - Posto de Vinificação\n'
                         ' * 07 - Cantina. Central (Cooperativa)\n')

if registro_mapa == '':
    registro_mapa = input('O registro mapa, não foi cadastrado nos campos adicionais, favor digitar\n')

endereco = emitente['Carteira']['EnderecoPrincipal']['Logradouro']
if 'Numero' in emitente['Carteira']['EnderecoPrincipal']:
    endereco += ', ' + emitente['Carteira']['EnderecoPrincipal']['Numero']

if 'Bairro' in emitente['Carteira']['EnderecoPrincipal']:
    endereco += ', ' + emitente['Carteira']['EnderecoPrincipal']['Bairro']

if 'Complemento' in emitente['Carteira']['EnderecoPrincipal']:
    endereco += ', ' + emitente['Carteira']['EnderecoPrincipal']['Complemento']


generator.set_registro_10(
    cnpj=emitente['Cnpj'],
    registro_mapa=registro_mapa,
    razao_social=emitente['Nome'],
    endereco=endereco,
    municipio=str(emitente['Carteira']['EnderecoPrincipal']['Municipio']['CodigoIbge']),
    cep=emitente['Carteira']['EnderecoPrincipal']['Cep'],
    versao='V4.5'
)

telefone = emitente['Carteira']['TelefonePrincipal']['Numero']
telefone = re.sub('[^0-9]', '', telefone)

fax = ''
if 'TelefoneFax' in emitente['Carteira']:
    fax = emitente['Carteira']['TelefoneFax']['Numero']
    fax = re.sub('[^0-9]', '', fax)

generator.set_registro_11(
    telefone=telefone,
    fax=fax,
    tipo_empresa=tipo_empresa,
    ie=emitente['Carteira']['Ie']['Numero'],
    diretor=emitente['NomeDoResponsavel'],
    responsavel_tecnico=responsavel_tecnico,
    documento_tecnico=documento_tecnico,
    email=emitente['Carteira']['EmailPrincipal']['Endereco']
)
produtos = Produtos(connection)
produtos_vendidos = produtos.get_prods()
produtos.get_prod_vend()
for produto in produtos_vendidos:
    generator.set_registro_15(
        cnpj=emitente['Cnpj'],
        codigo=produto['codigo'],
        descricao=produto['descricao'],
        marca=produto['marca'],
        produto=produto['produto'],
        tipo=produto['tipo'],
        classe=produto['classe'],
        especie=produto['especie'],
        percentual=produto['percentual'],
        safra=produto['safra'],
        unidade=produto['unidade']
    )


generator.export_file()
