from datetime import date


class Generator:
    registro_10 = []
    registro_11 = []
    registro_15 = []
    registro_20 = []
    registro_21 = []
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
        unidades = ['LT', 'KG']
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

    def set_registro_20(self, cnpj, mes, ano, operacao, numero, uf, tipo, serie):
        if len(cnpj) > 14:
            return 'cnpj Invalido'
        if len(mes) > 2:
            return 'mes Invalido'
        if len(ano) > 4:
            return 'ano Invalido'
        if len(operacao) > 2:
            return 'operacao Invalido'
        if len(numero) > 10:
            return 'numero Invalido'
        if len(uf) > 2:
            return 'uf Invalido'
        if len(tipo) > 1:
            return 'tipo Invalido'
        if len(serie) > 3:
            return 'serie Invalido'

        self.registro_20.append([
            cnpj,
            mes,
            ano,
            operacao,
            numero,
            uf,
            tipo,
            serie
        ])

    def set_registro_21(self, cgc, produto, embalagem, litros):
        if len(cgc) > 14:
            return 'cgc Invalido'
        if len(produto) > 15:
            return 'produto Invalido'
        if len(embalagem) > 2:
            return 'embalagem Invalido'
        if len(litros) > 10:
            return 'litros Invalido'

        self.registro_21.append([
            cgc,
            produto,
            embalagem,
            litros
        ])

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

        for x in self.registro_20:
            line = '20'
            line += x[0].ljust(14, '0')
            line += x[1].ljust(2, '0')
            line += x[2].ljust(4, '0')
            line += x[3].ljust(2, '0')
            line += x[4].ljust(10, '0')
            line += x[5].ljust(2)
            line += x[6].ljust(1)
            line += x[7].ljust(3)
            line += '\n'.rjust(122)
            f.write(line)
            self.total_linhas += 1

        for x in self.registro_21:
            line = '21'
            line += x[0].ljust(14, '0')
            line += x[1].ljust(15)
            line += x[2].ljust(2, '0')
            line += x[3].ljust(10, '0')
            line += '\n'.rjust(118)
            f.write(line)
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
        line += str(self.total_litros).rjust(20, '0')
        line += str(self.total_kg).rjust(20, '0')
        line += str(self.valor_total).rjust(20, '0')
        line += str(self.total_linhas).rjust(10, '0')
        line += '\n'.rjust(89)
        f.write(line)

        f.close()
