from datetime import datetime
from bson.tz_util import FixedOffset
from bson.regex import Regex


class Produtos:
    connection = None
    def __init__(self, connection):
        self.connection = connection

    def get_prod_vend(self):
        database = self.connection['DigisatServer']
        collection_movimentacoes = database["Movimentacoes"]
        collection_produtos_servicos = database["ProdutosServicos"]
        produtos = []

        query = {
            "DataHoraEmissao": {
                u"$gte": datetime.strptime("2021-09-30 21:00:00.000000", "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo = FixedOffset(-180, "-0300")),
                u"$lte": datetime.strptime("2021-10-31 20:59:59.000000", "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo = FixedOffset(-180, "-0300"))
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

        cursor = collection_movimentacoes.find(query)
        try:
            for doc in cursor:
                for item in doc['ItensBase']:
                    produto = {
                        'codigo': item['ProdutoServico']['CodigoInterno'],
                        'descricao': item['ProdutoServico']['Descricao'],
                        'marca': '',
                        'produto': '',
                        'tipo': '',
                        'classe': '',
                        'especie': '',
                        'percentual': '',
                        'safra': '',
                        'unidade': ''
                    }
                
                    produtos_servicos = collection_produtos_servicos.find_one({"_id": item['ProdutoServico']['ProdutoServicoReferencia']})
                    produto['unidade'] = produtos_servicos['UnidadeMedida']['Sigla']
                    if 'Marca' in produtos_servicos:
                        produto['Marca'] = produtos_servicos['Marca']['Descricao']
                    if 'CamposPersonalizado' in produtos_servicos:
                        for campo in produtos_servicos['CamposPersonalizado']:
                            if campo['TipoPersonalizado']['Ativo'] is True:
                                campo_desc = campo['TipoPersonalizado']['Descricao'].lower()
                                if  campo_desc == 'produto':
                                    produto['produto'] = campo['Valor']

                                if campo_desc == 'tipo':
                                    produto['tipo'] = campo['Valor']

                                if campo_desc == 'classe':
                                    produto['classe'] = campo['Valor']

                                if campo_desc == 'especie':
                                    produto['especie'] = campo['Valor']

                                if campo_desc == 'percentual':
                                    produto['percentual'] = campo['Valor']

                                if campo_desc == 'safra':
                                    produto['safra'] = campo['Valor']
                        if produto not in produtos:
                            produtos.append(produto)
        finally:
            return produtos