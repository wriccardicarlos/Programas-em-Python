import os

diretorio_atual = os.getcwd()
print('caminho atual:',diretorio_atual)

diretorio_arquivo = os.path.abspath(os.path.dirname(__file__))
os.chdir(diretorio_arquivo)
print('caminho do arquivo:', diretorio_arquivo)

lista = os.listdir()
print(lista)