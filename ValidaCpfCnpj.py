# -*- coding:utf-8 -*-
class ValidaCpfCnpj:
    """
        Exemplo de como Usa:
        x = ValidaCpfCnpj()
        print(x.exe('253231350001', 'cnpj'))
        print(x.exe('40012342211', 'cpf'))
    """

    cpf, cnpj = '', ''

    def exe(self, teste, tipo):
        try:
            tipo = tipo.lower()
            if tipo == 'cpf':
                self.cpf = teste
                return self.__valida_cpf()
            else:
                self.cnpj = teste
                return self.__valida_cnpj()
        except:
            return 'Não foi possivel calcular a entrada "' + teste + '"'

    def __valida_cpf(self):
        lst_invalidos = [str(x) * 11 for x in range(0, 10)]
        if self.cpf in lst_invalidos:
            return 'cpf_invalido: ' + self.cpf
        else:
            cpf = self.__completa_tamanho(self.cpf, 11)
            r = self.__calcula_digito_verificadorj(cpf, 11)
            if r == cpf:
                return self.cpf + ' OK.'
            else:
                return 'O CPF ' + self.cpf + ' é Invalido o correto deveria ser ' + r

    def __valida_cnpj(self):
        cnpj = self.__completa_tamanho(self.cnpj, 14)
        r = self.__calcula_digito_verificadorj(cnpj, 14)
        if r == cnpj:
            return 'cnpj_ok'
        else:
            return 'CNPJ Invalido! O correto seria ' + r

    def __completa_tamanho(self, cpf_cnpj, tam):
        if len(cpf_cnpj) < tam:
            return cpf_cnpj + str('0' * (tam - len(cpf_cnpj)))
        else:
            return cpf_cnpj

    def __calcula_digito_verificadorj(self, cpf, tam):
        b = 0
        if tam == 11:
            cpf2 = list(cpf[0:9])
        else:
            cpf2 = list(cpf[0:12])

        while b < 2:
            dv = self.__calcula_cpf_cnpj(cpf2, tam)
            if dv % 11 < 2:
                cpf2.append('0')
            else:
                cpf2.append(str(11 - dv % 11))
            b += 1

        return ''.join(cpf2)

    def __calcula_cpf_cnpj(self, cpf_cnpj, tam):
        calc = 0
        if tam == 11:
            n = len(cpf_cnpj) + 1
            for a in cpf_cnpj:
                calc += n * int(a)
                n -= 1
        elif tam == 14:
            n = 2
            for a in cpf_cnpj[::-1]:
                calc += n * int(a)
                n += 1
                if n == 10:
                    n = 2
        return calc


if __name__ == '__main__':
    x = ValidaCpfCnpj()
    # print(x.exe('253231350001', 'cnpj'))
    print(x.exe('836360190001', 'CNPJ'))
    print(x.exe('93248522', 'cpf'))
    print(x.exe('402831502', 'cpf'))
