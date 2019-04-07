#!/usr/bin/env python3

from tabela import tabela_unica
import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)


def select():
    return input("""
    1) Empresa de atividade única sem substituição tributária
    
    2) Empresa com atividade internacional
        """)


if select() == '1':
    dados = tabela_unica(list(map(float, input('Faturamento: ').strip().split())), input('Anexo: '))
    print(dados)
else:
    print('num deu')
