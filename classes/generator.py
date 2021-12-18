from datetime import date


class Generator:
    registro_10 = []
    registro_11 = []
    registro_15 = []
    registro_20 = []
    registro_52 = []
    registro_53 = []
    registro_70 = []

    total_litros = 0
    total_kg = 0
    valor_total = 0
    total_linhas = 1

    def set_registro_10(self, cnpj: str, registro_mapa: str, razao_social: str, endereco: str, municipio: str, cep: str,
                        versao: str):
        if len(cnpj) != 14:
            raise ValueError('CNPJ Invalido')
        if len(registro_mapa) > 8:
            raise ValueError('registro mapa Invalido')
        if len(razao_social) > 40:
            raise ValueError('razao social Invalido')
        if len(endereco) > 40:
            raise ValueError('endereco Invalido')
        if len(municipio) > 8:
            raise ValueError('municipio Invalido')
        if len(cep) > 8:
            raise ValueError('cep Invalido')
        if len(versao) > 10:
            raise ValueError('versao Invalido')
        self.registro_10.append([
            cnpj,
            registro_mapa,
            razao_social,
            endereco,
            municipio,
            cep,
            versao
        ])

    def set_registro_11(self, telefone, fax, tipo_empresa, ie, diretor, responsavel_tecnico, documento_tecnico, email):
        if len(telefone) > 15:
            raise ValueError('Telefone Invalido')
        if len(fax) > 15:
            raise ValueError('fax Invalido')
        if len(tipo_empresa) > 2:
            raise ValueError('Tipo empresa Invalido')
        if len(ie) > 15:
            raise ValueError('Inscrição Estadual Invalido')
        if len(diretor) > 30:
            raise ValueError('diretor Invalido')
        if len(responsavel_tecnico) > 30:
            raise ValueError('responsavel tecnico Invalido')
        if len(documento_tecnico) > 10:
            raise ValueError('documento do responsavel tecnico Invalido')
        if len(email) > 40:
            raise ValueError('email Invalido')

        self.registro_11.append([
            telefone,
            fax,
            tipo_empresa,
            ie,
            diretor,
            responsavel_tecnico,
            documento_tecnico,
            email
        ])

    def set_registro_15(self, cnpj, codigo, descricao, marca, produto, tipo, classe, especie, percentual, safra,
                        unidade):
        unidades = ['LT', 'L', 'KG']
        if unidade == 'L':
            unidade = 'LT'
        if len(cnpj) > 14:
            raise ValueError('cnpj Invalido')

        if len(codigo) > 15:
            raise ValueError('codigo Invalido')

        if len(descricao) > 50:
            raise ValueError('descricao Invalido')

        if len(marca) > 6:
            raise ValueError('marca Invalido')

        if len(produto) > 3:
            raise ValueError('produto Invalido')

        if len(tipo) > 2:
            raise ValueError('tipo tecnico Invalido')

        if len(classe) > 2:
            raise ValueError('classe Invalido')

        if len(especie) > 4:
            raise ValueError('especie Invalido')

        if len(percentual) > 3:
            raise ValueError('percentual Invalido')

        if len(safra) > 4:
            raise ValueError('safra Invalido')

        if len(unidade) > 2 or unidade not in unidades:
            raise ValueError('Unidade Invalido, valores validos LT, KG e o valor informado foi {0}'.format(unidade))
        
        self.registro_15.append([
            cnpj,
            codigo,
            descricao,
            marca,
            produto,
            tipo,
            classe,
            especie,
            percentual,
            safra,
            unidade
        ])

    def set_registro_20(self, cnpj, mes, ano, operacao, numero, uf, tipo, serie, itens):
        if len(cnpj) != 14:
            raise ValueError('Cnpj Invalido')

        if 1 > int(mes) > 12:
            raise ValueError('Mes Invalido, valor passado', mes)

        if 2000 > int(ano) > datetime.datetime.now().year:
            raise ValueError('Ano Invalido')

        if operacao not in ['01', '05', '11', '13', '14', '22', '23']:
            raise ValueError('Operacao Invalido')

        if len(str(numero)) > 10:
            raise ValueError('Numero Invalido')

        if len(uf) > 2:
            raise ValueError('Uf Invalido')

        if tipo not in [1,2,3]:
            raise ValueError('Tipo Invalido')

        if len(serie) > 3:
            raise ValueError('Serie Invalido')

        for item in itens:
            self.set_registro_21(
                cgc=cnpj,
                produto=item['produto'],
                embalagem=item['embalagem'],
                litros=item['litros']
            )

        self.registro_20.append([
            cnpj,
            mes,
            ano,
            operacao,
            numero,
            uf,
            tipo,
            serie,
            itens
        ])
        return '{0}{1}{2}{3}{4}{5}{6}{7}'.format(cnpj, mes, ano, operacao, numero, uf, tipo, serie)

    def set_registro_21(self, cgc, produto, embalagem, litros):
        litros = float('{:0.2f}'.format(litros))
        if len(cgc) != 14:
            raise ValueError('cgc Invalido')

        if len(produto) > 15:
            raise ValueError('produto Invalido')

        if embalagem not in ['01', '02']:
            raise ValueError('embalagem Invalido, valor passado: ', embalagem)

        if len(str(litros)) > 10:
            raise ValueError('litros Invalido, valor informado: ', litros, produto)

    def set_registro_52(self, cgc, mes, ano):
        if len(cgc) > 14:
            return 'cgc Invalido'
        if len(mes) > 2:
            return 'mes Invalido'
        if len(ano) > 4:
            return 'ano Invalido'

        self.registro_52.append([
            cgc,
            mes,
            ano
        ])

    def set_registro_53(self, cgc, produto, litros):
        if len(cgc) > 14:
            return 'cgc Invalido'
        if len(produto) > 15:
            return 'produto Invalido'
        if len(litros) > 10:
            return 'litros Invalido'

        self.registro_53.append([
            cgc,
            produto,
            litros
        ])

    def set_registro_70(self, cgc, produto, quantidade, mes, ano, operacao):
        if len(cgc) > 14:
            return 'cgc Invalido'
        if len(produto) > 4:
            return 'produto Invalido'
        if len(quantidade) > 10:
            return 'quantidade Invalido'
        if len(mes) > 2:
            return 'mes Invalido'
        if len(ano) > 4:
            return 'ano Invalido'
        if len(operacao) > 2:
            return 'operacao Invalido'

        self.registro_70.append([
            cgc,
            produto,
            quantidade,
            mes,
            ano,
            operacao
        ])

    def export_file(self):
        data_atual = date.today()
        name_file = '{}-{}.txt'.format(data_atual.year, data_atual.month)
        f = open(name_file, "w")
        for x in self.registro_10:
            line = '10'
            line += x[0].ljust(14)
            line += x[1].ljust(8)
            line += x[2].ljust(40)
            line += x[3].ljust(40)
            line += x[4].rjust(8, '0')
            line += x[5].ljust(8, '0')
            line += x[6].ljust(10)
            line += '\n'.rjust(31)
            f.write(line)
            self.total_linhas += 1

        for x in self.registro_11:
            line = '11'
            line += x[0].ljust(15)
            line += x[1].ljust(15)
            line += x[2].ljust(2, '0')
            line += x[3].ljust(15)
            line += x[4].ljust(30)
            line += x[5].ljust(30)
            line += x[6].ljust(10, '0')
            line += x[7].ljust(40)
            line += '\n'.rjust(2)
            f.write(line)
            self.total_linhas += 1
        
        for x in self.registro_15:
            line = '15'
            line += x[0].ljust(14, '0')
            line += x[1].ljust(15)
            line += x[2].ljust(50)
            line += x[3].ljust(6)
            line += ''.ljust(9)
            line += x[4].ljust(3, '0')
            line += x[5].ljust(2, '0')
            line += x[6].ljust(2, '0')
            line += x[7].ljust(4, '0')
            line += x[8].ljust(3, '0')
            line += x[9].ljust(4, '0')
            line += x[10].ljust(2)
            line += '\n'.rjust(45)
            f.write(line)
            self.total_linhas += 1

        for nota in self.registro_20:
            line = '20'
            line += nota[0].ljust(14, '0')
            line += str(nota[1]).rjust(2, '0')
            line += str(nota[2]).rjust(4, '0')
            line += str(nota[3]).ljust(2, '0')
            line += str(nota[4]).rjust(10, '0')
            line += str(nota[5]).ljust(2)
            line += str(nota[6]).ljust(1)
            line += str(nota[7]).ljust(3)
            line += '\n'.rjust(121)
            f.write(line)
            self.total_linhas += 1
            for item in nota[8]:
                line = '21'
                line += nota[0].ljust(14, '0')
                line += item['produto'].ljust(15)
                line += item['embalagem'].ljust(2, '0')
                line += '{:0.2f}'.format(item['litros']).replace(',', '').replace('.', '').rjust(10, '0')
                line += '\n'.rjust(118)
                f.write(line)
                self.total_litros += item['litros']
                self.total_linhas += 1

        for x in self.registro_52:
            line = '52'
            line += x[0].ljust(14, '0')
            line += x[1].ljust(2, '0')
            line += x[2].ljust(4, '0')
            line += '\n'.rjust(139)
            f.write(line)
            self.total_linhas += 1

        for x in self.registro_53:
            line = '53'
            line += x[0].ljust(14, '0')
            line += x[1].ljust(15, '0')
            line += x[2].ljust(10, '0')
            line += '\n'.rjust(120)
            f.write(line)
            self.total_linhas += 1

        for x in self.registro_70:
            line = '70'
            line += x[0].ljust(14, '0')
            line += x[1].ljust(4, '0')
            line += x[2].ljust(10, '0')
            line += x[3].ljust(2, '0')
            line += x[4].ljust(4, '0')
            line += x[5].ljust(2, '0')
            line += '\n'.rjust(123)
            f.write(line)
            self.total_linhas += 1
        
        # Registro 90
        line = '90'
        line += '{:0.2f}'.format(self.total_litros).replace('.', '').replace(',', '').rjust(20, '0')
        line += '{:0.2f}'.format(self.total_kg).replace('.', '').replace(',', '').rjust(20, '0')
        line += '{:0.4f}'.format(self.valor_total).replace('.', '').replace(',', '').rjust(20, '0')
        line += str(self.total_linhas).rjust(10, '0')
        line += ''.rjust(88)
        f.write(line)

        f.close()
