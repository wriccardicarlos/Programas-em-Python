import pandas as pd

tabelaVendas=pd.read_excel('Vendas.xlsx')
arquivoExcel=pd.ExcelFile('Vendas.xlsx')

#print(arquivoExcel.sheet_names)
arquivoExcel.parse("Plan1")

#faturamento=tabelaVendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()   # soma os valores de cada loja
#prodVendidos=tabelaVendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()   # soma as quantidades de cada loja
#print(tabelaVendas.loc[[0,2,6], 'ID Loja':'Valor Final'])                      # mostra apenas as linhas e colunas selecionadas
#print(tabelaVendas.info())                                                     # info da tabela
#print(tabelaVendas.sort_values(["ID Loja","Quantidade"]))                      # organiza os valores em ordem
#print(tabelaVendas.isnull().sum())                                             # verifica quantos dados estão faltando em cada coluna
#print(tabelaVendas['ID Loja'].unique())                                        # mostra os valores únicos de cada coluna
#print(tabelaVendas.describe())                                                 # dados estatisticos
