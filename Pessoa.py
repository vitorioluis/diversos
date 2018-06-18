# -*- coding:utf-8 -*-

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self._altura = altura
        self.__idade = idade

    def __str__(self):
        return self.__nome

    @property
    def nome(self):
        print('get nome')
        return self.__nome

    @nome.setter
    def nome(self, nome):
        print('set nome')
        self.__nome = nome

    @property
    def idade(self):
        print('get idade')
        return self.__idade

    @idade.setter
    def idade(self, idade):
        print('set idade', idade)
        self.__idade = idade


if __name__=='__main__':
    p1 = Pessoa('José', 40)
    p1.nome = 'José Bonifacio'
    p1.idade = 34
    print(p1.__dict__)

    p2 = Pessoa('João', 27)
    p2.nome = 'João da Silva'
    p2.idade = 20
    print(p2.__dict__)
