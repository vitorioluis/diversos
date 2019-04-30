# -*- coding: utf8 -*-

"""
Exemplo simples de como utilizar concurrent futures para mapear arquivos em diretórios
"""


import os
from concurrent.futures import ThreadPoolExecutor as pool
from datetime import datetime


def LerSubDir(diretorio, extensao=None):
    """
    Mapeia diretórios e sub-diretórios

    :param diretorio: diretório que contém os arquivos a serem mapeados
    :param extensao: Parametro facultativo que se inserido só arquivos que contiver a extensão seram mapeados
    :return: Um lista contendo os arquivos mapeados
    """
    lista_arquivos = []
    lst_ext = []
    for path, subdirs, files in os.walk(diretorio):
        for name in files:
            arquivo = str(os.path.join(path, name))
            ext_arq = arquivo[-3:].lower()
            extensao = extensao.lower() if extensao is not None else extensao
            if extensao == ext_arq:
                lst_ext.append(arquivo.replace(chr(92), chr(47)))
            elif extensao is None:
                lista_arquivos.append(arquivo.replace(chr(92), chr(47)))

    return lista_arquivos if len(lista_arquivos) > 0 else lst_ext


if __name__ == "__main__":
    # captura o horario que começou para calcular o tempo que gastou
    start = datetime.now()

    # lista arquivos do diretório
    lst_arq = LerSubDir("./")

    # verifica quantos arquivos tem o diretório
    qtd_arq = len(lst_arq)

    # caputura a qtd total de nucleos de processadores disponíveis e subtrai 1
    n_cpu = os.cpu_count() - 1

    print('arquivos encontrados', qtd_arq)
    print('Processadores utilizados', n_cpu)

    # declara o executor para concurrent futures
    executor = pool(max_workers=n_cpu)

    # executa o processamento paralelo
    final = executor.map(lambda txt: os.rename(txt, txt[0:-3] + 'txt'), lst_arq)

    # deleta da memória a lista de arquivos
    del lst_arq

    # captura o horario que começou para calcular o tempo que gastou
    stop = datetime.now()

    # tempo gasto de execução
    print('Tempo gasto:', stop - start)
