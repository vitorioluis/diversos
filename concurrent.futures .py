# -*- coding: utf-8 -*-

import json
from concurrent.futures import ThreadPoolExecutor
from os import cpu_count

import requests

# verifica quantos nucleos tem no computador
qtd_cpu = cpu_count() - 1


def busca_cnpj(cnpj):
    dic_json = {}
    response = requests.get('https://www.receitaws.com.br/v1/cnpj/{0}'.format(cnpj))
    if response.status_code == 200:
        dic_json = json.loads(response.content.decode('utf-8'))
        print(dic_json)

    # return dic_json


if __name__ == '__main__':
    # lista de cnpj obtida no dia 18/06/2018 no site: http://cnpj.info/lista
    lst_cnpj = ['092962950001', '61190658000106', '00000000542245', '17298092000130', '00000000497606',
                '17192451000170', '59461152000134', '49925225000148', '18725747000172', '43425008000102',
                '62291208000164', '01247325000136', '07113647000179']
    with ThreadPoolExecutor(max_workers=qtd_cpu) as executor:
        for cnpj in lst_cnpj:
            executor.submit(busca_cnpj, cnpj)
