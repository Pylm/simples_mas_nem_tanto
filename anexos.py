#!/usr/bin/env python3

import pandas as pd

if __name__ == '__main__':
    print('Use o arquivo menu.py')
else:
    def anexo(num):
        return pd.read_csv(f'tabelas/anexo{num}.csv')
