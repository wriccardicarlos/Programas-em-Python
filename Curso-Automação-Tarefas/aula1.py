import pyautogui as pg
import time
import pyscreeze
import pandas as pd

posx=900
posy=1078
email='cwriccardif@gmail.com'
senha='carlos123'
link='https://dlp.hashtagtreinamentos.com/python/intensivao/login'
tabelaProdutos=pd.read_csv("produtos.csv")

def login():
    time.sleep(1)
    pg.press('tab')
    pg.write(email)
    pg.PAUSE=0.5
    pg.press('tab')
    pg.write(senha)
    pg.PAUSE=0.5
    pg.press('tab')
    pg.press('enter')

def cadastrarProduto():
    time.sleep(1)
    pg.press('tab')
    i=0
    for i in tabelaProdutos.index   :
        time.sleep(1)
        pg.write(tabelaProdutos.loc[[i],'codigo'].values[0])
        pg.PAUSE=0.5
        pg.press('tab')
        pg.write(tabelaProdutos.loc[[i],'marca'].values[0])
        pg.PAUSE=0.5
        pg.press('tab')
        pg.write(tabelaProdutos.loc[[i],'tipo',].values[0])
        pg.PAUSE=0.5
        pg.press('tab')
        pg.write(str(tabelaProdutos.loc[[i],'categoria'].values[0]))
        pg.PAUSE=0.5
        pg.press('tab')
        pg.write('R$'+str(tabelaProdutos.loc[[i],'preco_unitario'].values[0]))
        pg.PAUSE=0.5
        pg.press('tab')
        pg.write('R$'+str(tabelaProdutos.loc[[i],'custo'].values[0]))
        pg.PAUSE=0.5
        pg.press('tab')
        if not pd.isna(tabelaProdutos.loc[[i],'obs'].values[0]):
            pg.write(str(tabelaProdutos.loc[[i],'obs'].values[0]))
            pg.PAUSE=0.5
        pg.press('enter')
        pg.scroll(5000)
        time.sleep(2)
        pg.click(x=1000, y=310)

def operaFechado():
    pg.press('win')
    pg.write('Opera')
    pg.press('enter')

def operaAberto():
    pg.hotkey('ctrl','t')

def codigo():
    time.sleep(3)
    if pyscreeze.pixelMatchesColor(posx,posy,(179,178,175)):
        operaAberto()
    else:
        operaFechado()
    time.sleep(1)
    pg.write(link)
    pg.press('enter')
    pg.PAUSE=0.5
    login()
    cadastrarProduto()

codigo()