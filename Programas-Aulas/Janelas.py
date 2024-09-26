from tkinter import *
from tkinter import ttk
import sqlite3


window = Tk()

class Funcs():
# comando botão limpar
    def limpar(self):
        self.codigo_in.delete(0,END)
        self.nome_in.delete(0,END)
        self.telefone_in.delete(0,END)
        self.cidade_in.delete(0,END)
# conecta ao banco de dados
    def  conectaBd(self):
        self.conn = sqlite3.connect("Clientes.bd")
        self.cursor = self.conn.cursor()
# desconecta do banco de dados
    def desconectaBd(self):
        self.conn.close()
# cria tabela do banco de dados
    def tabelasBd(self):
        self.conectaBd(); print("Conectando ao banco de dados")
# criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconectaBd()
    def variaveis(self):
        self.codigo = self.codigo_in.get()
        self.nome = self.nome_in.get()
        self.telefone = self.telefone_in.get()
        self.cidade = self.cidade_in.get()
# adiciona os clientes
    def add_clientes(self):
        self.variaveis()
        self.conectaBd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.desconectaBd()
        self.selectLista()
        self.limpar()
# seleciona a lista
    def selectLista(self):
        self.listaNome.delete(*self.listaNome.get_children())
        self.conectaBd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaNome.insert("", END, values=i)
        self.desconectaBd()
    def onDoubleClick(self,event):
        self.limpar()
        self.listaNome.selection()

        for n in self.listaNome.selection():
            col1, col2, col3, col4 = self.listaNome.item(n, 'values')
            self.codigo_in.insert(END, col1)
            self.nome_in.insert(END, col2)
            self.telefone_in.insert(END, col3)
            self.cidade_in.insert(END, col4)
    def deleta(self):
        self.variaveis()
        self.conectaBd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""",(self.codigo))
        self.conn.commit()
        self.desconectaBd()
        self.limpar()
        self.selectLista()

class Application(Funcs):
# inicializa a tela
    def  __init__(self):
        self.root = window
        self.tela()
        self.frames()
        self.botoes()
        self.lista_usuarios()
        self.tabelasBd()
        self.selectLista()
        window.mainloop()
# define a configuracao da tela
    def tela(self):
        self.root.title("Cadastro Clientes")
        self.root.configure(background= '#5F9EA0')
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=600)
        self.root.minsize(width=500, height=500)
# criar os frames
    def frames(self):
        self.frame_superior = Frame(self.root, bd=4, bg='#c0c0c0', highlightbackground='#808080', highlightthickness=2)
        self.frame_superior.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46 )
        self.frame_inferior = Frame(self.root, bd=4, bg='#c0c0c0', highlightbackground='#808080', highlightthickness=2)
        self.frame_inferior.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46 )
# criar botoes
    def botoes(self):
    # criacao botao limpar
        self.bt_limpar = Button(self.frame_superior, text="Limpar", command=self.limpar)
        self.bt_limpar.place(relx=0.0, rely= 0.0, relwidth=0.1, relheight=0.15)
    # criacao botao buscar
        self.bt_buscar = Button(self.frame_superior, text='Buscar')
        self.bt_buscar.place(relx=0.1, rely= 0.0, relwidth=0.1, relheight=0.15)
    # criacao botao criar
        self.bt_criar = Button(self.frame_superior, text='Criar', command=self.add_clientes)
        self.bt_criar.place(relx=0.7, rely= 0.0, relwidth=0.1, relheight=0.15)
    # criacao botao alterar
        self.bt_voltar = Button(self.frame_superior, text='Alterar')
        self.bt_voltar.place(relx=0.8, rely= 0.0, relwidth=0.1, relheight=0.15)
    # criacao botao apagar
        self.bt_apagar = Button(self.frame_superior, text='Apagar', command=self.deleta)
        self.bt_apagar.place(relx=0.9, rely= 0.0, relwidth=0.1, relheight=0.15)

    # criacao label codigo
        self.lb_codigo = Label(self.frame_superior, text = 'Código', background='#c0c0c0' )
        self.lb_codigo.place(relx=0.05, rely=0.25)

        self.codigo_in = Entry(self.frame_superior)
        self.codigo_in.place(relx=0.05, rely=0.35, relwidth= 0.1, relheight=0.1)
     # criacao label nome
        self.lb_nome = Label(self.frame_superior, text = 'Nome', background='#c0c0c0' )
        self.lb_nome.place(relx=0.25, rely=0.25)

        self.nome_in = Entry(self.frame_superior)
        self.nome_in.place(relx=0.25, rely=0.35, relwidth= 0.5, relheight=0.1)
     # criacao label telefone
        self.lb_telefone = Label(self.frame_superior, text = 'Telefone', background='#c0c0c0' )
        self.lb_telefone.place(relx=0.05, rely=0.55)

        self.telefone_in = Entry(self.frame_superior)
        self.telefone_in.place(relx=0.05, rely=0.65, relwidth= 0.27, relheight=0.1)
     # criacao label cidade
        self.lb_cidade = Label(self.frame_superior, text = 'Cidade', background='#c0c0c0' )
        self.lb_cidade.place(relx=0.42, rely=0.55)

        self.cidade_in = Entry(self.frame_superior)
        self.cidade_in.place(relx=0.42, rely=0.65, relwidth= 0.2, relheight=0.1)
# criar lista usuarios
    def lista_usuarios(self):
        self.listaNome = ttk.Treeview(self.frame_inferior, height= 3, column=("col1", "col2","col3","col4"))
        self.listaNome.heading("#0", text="")
        self.listaNome.heading("#1", text="Código")
        self.listaNome.heading("#2", text="Nome")
        self.listaNome.heading("#3", text="Telefone")
        self.listaNome.heading("#4", text="Cidade")

        self.listaNome.column("#0",width=1)
        self.listaNome.column("#1",width=50)
        self.listaNome.column("#2",width=200)
        self.listaNome.column("#3",width=125)
        self.listaNome.column("#4",width=125)

        self.listaNome.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.9)

        self.scroolLista = Scrollbar(self.frame_inferior)
        self.listaNome.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.05, relwidth=0.03, relheight=0.9)
        self.listaNome.bind("<Double-1>", self.onDoubleClick)

Application()