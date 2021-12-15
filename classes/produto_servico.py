from datetime import datetime
from bson.tz_util import FixedOffset
from bson.regex import Regex
import unidecode 


class Produtos:
    connection = None
    def __init__(self, connection):
        self.connection = connection
        self.database = self.connection['DigisatServer']
        self.collection_movimentacoes = self.database["Movimentacoes"]
        self.collection_produtos_servicos = self.database["ProdutosServicos"]
        self.collection_pessoas = self.database["Pessoas"]

    def get_prods(self):
        query = {"Ativo": True, "CamposPersonalizado": {u"$exists": True}}
        cursor = self.collection_produtos_servicos.find(query)
        produtos = []
        try:
            for doc in cursor:
                produto = {
                    'codigo': doc['CodigoInterno'],
                    'descricao': doc['Descricao'],
                    'marca': '',
                    'produto': False,
                    'tipo': False,
                    'classe': False,
                    'especie': False,
                    'percentual': False,
                    'safra': False,
                    'unidade': doc['UnidadeMedida']['Sigla']
                }
                if 'Marca' in doc:
                        produto['Marca'] = doc['Marca']['Descricao']

                if 'CamposPersonalizado' in doc:
                    for campo in doc['CamposPersonalizado']:
                        if campo['TipoPersonalizado']['Ativo'] is True:
                            campo_desc = unidecode.unidecode(campo['TipoPersonalizado']['Descricao']).lower()
                            if  campo_desc == 'codigo_sisdevin' and campo['Valor'] != '':
                                produto['codigo'] = campo['Valor']

                            if  campo_desc == 'produto' and campo['Valor'] != '':
                                produto['produto'] = campo['Valor']

                            if campo_desc == 'tipo' and campo['Valor'] != '':
                                produto['tipo'] = campo['Valor']

                            if campo_desc == 'classe' and campo['Valor'] != '':
                                produto['classe'] = campo['Valor']
                            
                            if campo_desc == 'especie' and campo['Valor'] != '':
                                produto['especie'] = campo['Valor']

                            if campo_desc == 'percentual' and campo['Valor'] != '':
                                produto['percentual'] = campo['Valor']

                            if campo_desc == 'safra' and campo['Valor'] != '':
                                produto['safra'] = campo['Valor']
                
                if produto not in produtos and False not in produto.values():
                    produtos.append(produto)
        finally:
            return produtos
            
    def get_prod_vend(self):
        produtos = []

        query = {
            "DataHoraEmissao": {
                u"$gte": datetime.strptime("2000-03-27 21:00:00.000000", "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo = FixedOffset(-180, "-0300")),
                u"$lte": datetime.strptime("2021-04-14 20:59:59.000000", "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo = FixedOffset(-180, "-0300"))
            },
            "$or": [
                {
                    u"_t": Regex(u".*NotaFiscalEletronicaSaida.*", "i")
                },
                {
                    u"_t": Regex(u".*NotaFiscalConsumidorEletronica.*", "i")
                }
            ]
        }

        cursor = self.collection_movimentacoes.find(query)
        notas = []

        for doc in cursor:
            if 'NotaFiscalConsumidorEletronica' in doc['_t']:
                tipo = 2
            elif 'NotaFiscalEletronicaSaida' in doc['_t']:
                tipo = 1
            else:
                tipo = 3

            if 'EnderecoPrincipal' not in doc['Pessoa']:
                pessoa = self.collection_pessoas.find_one({'_id': doc['Pessoa']['PessoaReferencia']})
                pessoa = pessoa['Carteira']
            else:
                pessoa = doc['Pessoa']

            nota = {
                'mes':doc['DataHoraEmissao'].month, 
                'ano': doc['DataHoraEmissao'].year, 
                'operacao': '01', 
                'numero': doc['Numero'], 
                'uf': pessoa['EnderecoPrincipal']['Municipio']['Uf']['Sigla'], 
                'tipo': tipo, 
                'serie': doc['Serie'],
                'itens': []
            }
            
            for item in doc['ItensBase']:
                prod = self.collection_produtos_servicos.find_one({'_id': item['ProdutoServico']['ProdutoServicoReferencia']})
                valid = self.is_prod_valid(prod)
                if valid:
                    prod_valid = {
                        'produto': '',
                        'embalagem': '',
                        'litros': ''
                    }
                    for campo in prod['CamposPersonalizado']:
                        if campo['TipoPersonalizado']['Ativo'] is True:
                            campo_desc = unidecode.unidecode(campo['TipoPersonalizado']['Descricao']).lower()
                            if  campo_desc == 'codigo_sisdevin' and campo['Valor'] != '':
                                prod_valid['produto'] = campo['Valor']

                            if  campo_desc == 'embalagem' and campo['Valor'] != '':
                                prod_valid['embalagem'] = campo['Valor']

                            if  campo_desc == 'quantidade_baixar' and campo['Valor'] != '':
                                prod_valid['litros'] = item['Quantidade'] * campo['Valor']
                    nota['itens'].append(prod_valid)
            if nota['itens']:
                notas.append(nota)
        return notas

    def is_prod_valid(self, doc):
        cont = 0
        campos = ['tipo', 'classe', 'especie', 'produto', 'percentual', 'codigo_sisdevin', 'embalagem', 'quantidade_baixar']
        if doc['CodigoInterno'] == '98':
            print(doc['Descricao'])
        if 'CamposPersonalizado' in doc:
            for campo in doc['CamposPersonalizado']:
                if campo['TipoPersonalizado']['Ativo'] is True:
                    campo_desc = unidecode.unidecode(campo['TipoPersonalizado']['Descricao']).lower()
                    if doc['CodigoInterno'] == '98':
                        print(campo_desc)
                    for x in campos:
                        if campo_desc == x and campo['Valor'] != '':
                            cont += 1
            if cont == len(campos):
                return True
            else:
                return False
        else:
            return False