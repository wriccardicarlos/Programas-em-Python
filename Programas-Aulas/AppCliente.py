from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import  pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

window = Tk()

class Validadores:
    def valEntry2(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <=100

class Relatorios():
# define o arquivo e o local onde o relatorio sera armazenado
    def printCliente(self):
        webbrowser.open(r"Relatorios\cliente.pdf")
# gera os relatorios
    def geraRelatorio(self):
        self.c = canvas.Canvas(r"Relatorios\cliente.pdf")

        self.codigoRel = self.codigo_in.get()
        self.nomeRel = self.nome_in.get()
        self.telefoneRel = self.telefone_in.get()
        self.cidadeRel = self.cidade_in.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, "Ficha do Cliente")

        self.c.rect(25, 775, 550, 50, fill=False, stroke= True)

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, "Codigo: ")
        self.c.drawString(50, 670, "Nome: ")
        self.c.drawString(50, 640, "Telefone: ")
        self.c.drawString(50, 610, "Cidade: ")

        self.c.setFont("Helvetica", 18)
        self.c.drawString(150, 700, self.codigoRel)
        self.c.drawString(150, 670, self.nomeRel)
        self.c.drawString(150, 640, self.telefoneRel)
        self.c.drawString(150, 610, self.cidadeRel)

        self.c.showPage()
        self.c.save()
        self.printCliente()        

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
## criar tabela
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
        if self.nome_in.get() == "":
            msg = "É necessário um nome"
            messagebox.showinfo("Erro no cadastro",msg)
        else:
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
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""", (self.codigo))
        self.conn.commit()
        self.desconectaBd()
        self.limpar()
        self.selectLista()
    def altera(self):
        self.variaveis()
        self.conectaBd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ? """, (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconectaBd()
        self.selectLista()
        self.limpar()
    def buscar(self):
        self.conectaBd()
        self.listaNome.delete(*self.listaNome.get_children())
        
        self.nome_in.insert(END, "%")
        nome = self.nome_in.get()
        self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, cidade FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)
        buscarNome = self.cursor.fetchall()
        for i in buscarNome:
            self.listaNome.insert("", END, values=i)
        self.limpar()
        self.desconectaBd()

class Application(Funcs,Relatorios,Validadores):
# inicializa a tela
    def  __init__(self):
        self.root = window
        self.validar()
        self.tela()
        self.frames()
        self.botoes()
        self.lista_usuarios()
        self.tabelasBd()
        self.selectLista()
        self.menu()
        window.mainloop()
# define a configuracao da tela
    def tela(self):
        self.root.title("Cadastro Clientes")
        self.root.configure(background= '#1C1C1C')
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=600)
        self.root.minsize(width=500, height=500)
# criar os frames
    def frames(self):
        self.frame_superior = Frame(self.root, bd=4, bg='#4F4F4F', highlightbackground='#363636', highlightthickness=2)
        self.frame_superior.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46 )
        self.frame_inferior = Frame(self.root, bd=4, bg='#4F4F4F', highlightbackground='#363636', highlightthickness=2)
        self.frame_inferior.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46 )
# criar botoes
    def botoes(self):
        self.abas = ttk.Notebook(self.frame_superior)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background="#4F4F4F")
        self.aba2.configure(background="#4F4F4F")

        self.abas.add(self.aba1, text = "Usuários")
        self.abas.add(self.aba2, text = "Serviços")

        self.abas.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    ## criacao botao limpar
        self.bt_limpar = Button(self.aba1, text="Limpar", command=self.limpar, background='#D3D3D3',cursor='hand2')
        self.bt_limpar.place(relx=0.01, rely= 0.02, relwidth=0.1, relheight=0.15)

        self.bt_limpar.bind("<Enter>", func=lambda e: self.bt_limpar.config(
            background='white'))
        self.bt_limpar.bind("<Leave>", func=lambda e: self.bt_limpar.config(
            background='#D3D3D3'))
    ## criacao botao buscar
        self.bt_buscar = Button(self.aba1, text='Buscar', command=self.buscar, background='#D3D3D3',cursor='hand2')
        self.bt_buscar.place(relx=0.11, rely= 0.02, relwidth=0.1, relheight=0.15)

        self.bt_buscar.bind("<Enter>", func=lambda e: self.bt_buscar.config(
            background='white'))
        self.bt_buscar.bind("<Leave>", func=lambda e: self.bt_buscar.config(
            background='#D3D3D3'))
    ## criacao botao criar
        self.bt_criar = Button(self.aba1, text='Criar', command=self.add_clientes, background='#D3D3D3',cursor='hand2')
        self.bt_criar.place(relx=0.695, rely= 0.02, relwidth=0.1, relheight=0.15)

        self.bt_criar.bind("<Enter>", func=lambda e: self.bt_criar.config(
            background='white'))
        self.bt_criar.bind("<Leave>", func=lambda e: self.bt_criar.config(
            background='#D3D3D3'))
    ## criacao botao alterar
        self.bt_voltar = Button(self.aba1, text='Alterar', command=self.altera, background='#D3D3D3',cursor='hand2')
        self.bt_voltar.place(relx=0.795, rely= 0.02, relwidth=0.1, relheight=0.15)

        self.bt_voltar.bind("<Enter>", func=lambda e: self.bt_voltar.config(
            background='white'))
        self.bt_voltar.bind("<Leave>", func=lambda e: self.bt_voltar.config(
            background='#D3D3D3'))
    ## criacao botao apagar
        self.bt_apagar = Button(self.aba1, text='Apagar', command=self.deleta, background='#D3D3D3',cursor='hand2')
        self.bt_apagar.place(relx=0.895, rely= 0.02, relwidth=0.1, relheight=0.15)

        self.bt_apagar.bind("<Enter>", func=lambda e: self.bt_apagar.config(
            background='white'))
        self.bt_apagar.bind("<Leave>", func=lambda e: self.bt_apagar.config(
            background='#D3D3D3'))

    ## criacao label codigo
        self.lb_codigo = Label(self.aba1, text = 'Código', background='#4F4F4F', foreground='#A9A9A9')
        self.lb_codigo.place(relx=0.05, rely=0.25)

        self.codigo_in = Entry(self.aba1, validate= "key", validatecommand=self.vcmd2 )
        self.codigo_in.place(relx=0.05, rely=0.35, relwidth= 0.1, relheight=0.1)
    ## criacao label nome
        self.lb_nome = Label(self.aba1, text = 'Nome', background='#4F4F4F', foreground='#A9A9A9')
        self.lb_nome.place(relx=0.25, rely=0.25)

        self.nome_in = Entry(self.aba1)
        self.nome_in.place(relx=0.25, rely=0.35, relwidth= 0.5, relheight=0.1)
    ## criacao label telefone
        self.lb_telefone = Label(self.aba1, text = 'Telefone', background='#4F4F4F', foreground='#A9A9A9')
        self.lb_telefone.place(relx=0.05, rely=0.55)

        self.telefone_in = Entry(self.aba1)
        self.telefone_in.place(relx=0.05, rely=0.65, relwidth= 0.27, relheight=0.1)
    ## criacao label cidade
        self.lb_cidade = Label(self.aba1, text = 'Cidade', background='#4F4F4F', foreground='#A9A9A9')
        self.lb_cidade.place(relx=0.42, rely=0.55)

        self.cidade_in = Entry(self.aba1)
        self.cidade_in.place(relx=0.42, rely=0.65, relwidth= 0.2, relheight=0.1)
    ## criacao botao drop down
        self.tipVar = StringVar()
        self.tipV = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viuvo(a)")
        self.tipVar.set("Solteiro(a)")
        self.popupMenu = OptionMenu(self.aba2, self.tipVar, *self.tipV)
        self.popupMenu.place(relx= 0.01, rely= 0.02, relwidth=0.2, relheight=0.2)
        self.popupMenu.configure(background='#D3D3D3', foreground='black')
        self.estadoCivil = self.tipVar.get()

        self.popupMenu.bind("<Enter>", func=lambda e: self.popupMenu.config(
            background='white'))
        self.popupMenu.bind("<Leave>", func=lambda e: self.popupMenu.config(
            background='#D3D3D3'))
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
# criar barra menu
    def menu(self):
        menuBar = Menu(self.root)
        self.root.config(menu=menuBar)
        fileMenu1 = Menu(menuBar)
        fileMenu2 = Menu(menuBar)

        def quit(): self.root.destroy()

        menuBar.add_cascade(label = "Opções", menu = fileMenu1)
        menuBar.add_cascade(label = "Relatório", menu = fileMenu2)

        fileMenu1.add_command(label = "Sair",command= quit)
        fileMenu1.add_command(label = "Janela 2",command= self.janelas)

        fileMenu2.add_command(label = "Ficha do Cliente", command= self.geraRelatorio)
# criar janelas
    def janelas(self):
        self.root2 = Toplevel()
        self.root2.title("Janela 2")
        self.root2.configure(background= "#1C1C1C")
        self.root.geometry("400x200")
        self.root2.resizable(False,False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()
# chamar os validadores
    def validar(self):
        self.vcmd2 = (self.root.register(self.valEntry2), "%P")

Application()