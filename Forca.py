# -*- coding:utf-8 -*-
import random
import sys


class JogoForca:
    def __init__(self):
        self.__qtd_erros = 0
        self.__lst_erro = ['\n     __\n    |  |\n    |  \n    |  \n    |  \n    |    ',
                           '\n     __\n    |  |\n    |  O\n    |  \n    |  \n    |    ',
                           '\n     __\n    |  |\n    |  O\n    |  | \n    |  \n    |    ',
                           '\n     __\n    |  |\n    |  O\n    | /| \n    |  \n    |    ',
                           '\n     __\n    |  |\n    |  O\n    | /|\\ \n    |  \n    |    ',
                           '\n     __\n    |  |\n    |  O\n    | /|\\ \n    | / \n    |    ',
                           '\n     __\n    |  |\n    |  O\n    | /|\\ \n    | / \\ \n    |  \n    |    ',
                           '\n  \\      /\n   \\    /\n    \\  /\n     \\/\n     /\\\n    /  \\\n   /    \\\n  /      \\\n  YOU LOST?\n']

    def __sorteio(self):
        __lst_palavras = ['caneta', 'celular', 'teclado']
        return random.choice(__lst_palavras)

    def __gerar_forca(self, letra, *args):
        if len(args[0]) == 0:
            self.__qtd_erros += 1
        else:
            for p in args[0]:
                self.__monta_linha[p] = letra

        string = ''
        for x in self.__monta_linha:
            string += x + ' '

        # sys.stdout.write('Letras erradas: ' + ''.join(self.__letras_erradas))
        # sys.stdout.write('self.__lst_erro[self.__qtd_erros] + string')
        # sys.stdout.flush()
        print('Letras erradas:', ''.join(self.__letras_erradas))
        print(self.__lst_erro[self.__qtd_erros] + string)

    def player(self, letra):
        r = True
        posicao = []
        cont = 0
        if letra in self.__sorteado:
            for l in self.__sorteado:
                if l == letra:
                    posicao.append(cont)
                cont += 1
        else:
            self.__letras_erradas.append(letra)
        letra = letra if len(posicao) > 0 else "_"
        self.__gerar_forca(letra, posicao)

        if self.__qtd_erros > 6:
            r = False
            print("A palavra seria", ''.join(self.__sorteado))

        return r

    def novo_jogo(self):
        self.__qtd_erros = 0
        self.__sorteado = list(self.__sorteio())

        self.__monta_linha = list("_" * len(self.__sorteado))
        self.__letras_erradas = []


if __name__ == '__main__':

    j = JogoForca()
    j.novo_jogo()

    while True:
        print('Digite 0: Sair 1: Novo Jogoar')
        x = input('\r\nDigite uma letra: ')

        if x.strip() == '0':
            break
        if x.strip() == '1':
            j.novo_jogo()

        j.player(x)
