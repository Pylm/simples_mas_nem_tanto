#!/usr/bin/env python3

from anexos import anexo
import pandas as pd
import numpy as np

if __name__ == '__main__':

    print('Use o arquivo menu.py')

else:

    def base(faturamento, nacional=True, faturamento_e=0):
        if nacional:
            df = pd.DataFrame({'Faturamento Mensal': faturamento})
        else:
            df = pd.DataFrame({'Faturamento Mensal': faturamento, 'Mercado Externo': faturamento_e})
        df['Faixa'] = np.nan
        df['Faturamento Acumulado'] = np.nan
        df['Alíquota Nominal'] = np.nan
        df['Alíquota Real'] = np.nan
        df['A pagar'] = np.nan
        return df

    def preencher(df, nanexo, acum=0, media_mensal=0):

        if acum == 0:
            for i in df.index:

                if i == 0:
                    df['Faturamento Acumulado'].iat[i] = df['Faturamento Mensal'].iat[i] * 12
                else:
                    df['Faturamento Acumulado'].iat[i] = df['Faturamento Mensal'][:i].sum() / len(df['Faturamento Mensal'][:i]) * 12
        else:
            for i in df.index:
                df['Faturamento Acumulado'].iat[i] = acum - media_mensal + df['Faturamento Mensal'].iat[i]

        for i in df.index:
            if df['Faturamento Acumulado'].iat[i] < 180000:
                info = anexo(nanexo).head(1)
            elif df['Faturamento Acumulado'].iat[0] <= 4800000:
                info = anexo(nanexo)[anexo(nanexo)['Receita Bruta'] <= df['Faturamento Acumulado'].values[i]].tail(1)
            else:
                info = anexo(nanexo)[-1:]
            df['Alíquota Nominal'].iat[i] = info['Alíquota']
            df['Alíquota Real'].iat[i] = (df['Faturamento Acumulado'].iat[i] * info['Alíquota'] - info['Desconto']) / df['Faturamento Acumulado'].values[i]
            df['A pagar'].iat[i] = round(df['Faturamento Mensal'].values[i] * df['Alíquota Real'].values[i], 2)
            df['Faixa'].iat[i] = info['Faixa']
        return df

    #
    # def tabela_unica(faturamento_mensal, nanexo, acum=0, media_mensal=0):
    #
    #     tabela_anexo = anexo(nanexo)
    #     fat = pd.DataFrame(columns=['Faturamento Mensal'], data=faturamento_mensal)
    #     fat.insert(0, 'Faixa', np.nan)
    #     fat['Faturamento acumulado'] = np.nan
    #     fat['Alíquota nominal'] = np.nan
    #     fat['Alíquota real'] = np.nan
    #     fat['A pagar'] = np.nan
    #
    #     def base():
    #         if fat['Faturamento acumulado'].iat[i] <= 4800000:
    #             info = tabela_anexo.loc[tabela_anexo['Receita bruta'] <= fat['Faturamento acumulado'].values[i]].tail(1)
    #             return info
    #         else:
    #             info = tabela_anexo[-1:]
    #             return info
    #
    #     def preencher(it):
    #         fat['Alíquota nominal'].iat[it] = base()['Alíquota'].values
    #         fat['Alíquota real'].iat[it] = (fat['Faturamento acumulado'].iat[it] * base()['Alíquota'] - base()['Desconto']) / fat['Faturamento acumulado'].values[it]
    #         fat['A pagar'].iat[it] = round(fat['Faturamento mensal'].values[it] * fat['Alíquota real'].values[it], 2)
    #         fat['Faixa'].iat[it] = base()['Faixa']
    #
    #     if acum == 0:
    #         for i in fat.index:
    #             if i == 0:
    #                 fat['Faturamento acumulado'] = fat['Faturamento mensal'] * 12
    #             elif i == 1:
    #                 fat['Faturamento acumulado'].iat[i] = fat['Faturamento acumulado'].iat[0]
    #             else:
    #                 fat['Faturamento acumulado'].iat[i] = fat['Faturamento mensal'][:i].sum() * 12
    #             preencher(i)
    #     else:
    #         for i in fat.index:
    #             fat['Faturamento acumulado'].iat[i] = acum - media_mensal + faturamento_mensal[i]
    #             preencher(i)
    #
    #     return fat
    #
    #
    # def tabela_internacional(faturamento_mi, faturamento_me, nanexo, acum=0, media_mensal=0):
    #     tabela_anexo = anexo(nanexo)
    #
    #     fat_interno = pd.DataFrame({'MI': faturamento_mi})
    #     fat_externo = pd.DataFrame({'ME': faturamento_me})
    #
    #     def colunas(df):
    #         df['Faixa'] = np.nan
    #         df['Faturamento acumulado'] = np.nan
    #         df['Alíquota nominal'] = np.nan
    #         df['Alíquota real'] = np.nan
    #         df['A pagar'] = np.nan
    #
    #     def preencher(it, df):
    #         df['Alíquota nominal'].iat[it] = base()['Alíquota'].values
    #         df['Alíquota real'].iat[it] = (fat['Faturamento acumulado'].iat[it] * base()['Alíquota'] - base()[
    #             'Desconto']) / fat['Faturamento acumulado'].values[it]
    #         df['A pagar'].iat[it] = round(fat['Faturamento mensal'].values[it] * fat['Alíquota real'].values[it], 2)
    #         df['Faixa'].iat[it] = base()['Faixa']
    #
    #     if acum == 0:
    #         for i in fat.index:
    #             if i == 0:
    #                 fat['Faturamento acumulado'] = fat['Faturamento mensal'] * 12
    #             elif i == 1:
    #                 fat['Faturamento acumulado'].iat[i] = fat['Faturamento acumulado'].iat[0]
    #             else:
    #                 fat['Faturamento acumulado'].iat[i] = fat['Faturamento mensal'][:i].sum() * 12
    #             preencher(i)
    #     else:
    #         for i in fat.index:
    #             fat['Faturamento acumulado'].iat[i] = acum - media_mensal + faturamento_mensal[i]
    #             preencher(i)
    #     colunas(fat_interno)
    #     print(fat_interno)
