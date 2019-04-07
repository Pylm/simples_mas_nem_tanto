#!/usr/bin/env python3

import pandas as pd
import tabela

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)


def gerar_df():
    esqueleto = tabela.base(list(map(float, input('Faturamento: ').strip().split())))
    pronto = tabela.preencher(esqueleto, nanexo=int(input('Número do anexo: ')))
    print(pronto)


gerar_df()
