'''
Sistema de Gestão - Tkinter + SQLite3
Autor: Augusto Domingos (Aghasty GD)
Data de Ínicio: 02 de Fevereiro de 2022
Última actualização: 11 de Maio de 2022

'''


from cProfile import label
from distutils import command
from email import message
from email.message import EmailMessage
from msilib.schema import Font
from operator import iconcat
from tkinter import *
from tkinter import messagebox
from numpy import column_stack
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from turtle import width
import os
import sqlite3
from sqlite3 import Error
import tkinter.messagebox as tkMessageBox
import subprocess


pastaApp1=os.path.dirname(__file__)
caminho = pastaApp1 + "\\system\\data\\Database_01.db"


# VARIAVEIS
class MyApp:

    def __init__(self, myapp):
        self.LogoTela = PhotoImage(file=pastaApp1 + "\\assets\\GD_USER.png")
        self.barraDeMenus=Menu(myapp)
        self.menuContatos=Menu(self.barraDeMenus, tearoff=0)
        self.menuContatos.add_command(label = "Novo", command=self.novaJanela)
        self.menuContatos.add_command(label = "Entrar", command=self.novaJanela1)
        self.menuContatos.add_command(label = "Pesquisar")
        self.menuContatos.add_command(label = "Deletar",)
        self.menuContatos.add_separator()
        self.menuContatos.add_command(label = "Fechar", command=app.quit)
        self.barraDeMenus.add_cascade(label = "Contatos", menu=self.menuContatos)
        self.menuManutencao=Menu(self.barraDeMenus, tearoff=0)
        self.menuManutencao.add_command(label = "Gerir Usuários", command=self.GerirDados)
        self.barraDeMenus.add_cascade(label = "Manutenção", menu=self.menuManutencao)

        self.menuSobre=Menu(self.barraDeMenus, tearoff=0)
        self.menuSobre.add_command(label="Aghasty GD Productions", command=self.sobrenosTELA)
        self.barraDeMenus.add_cascade(label="Sobre",menu=self.menuSobre)
        app.config(menu=self.barraDeMenus)

    # Janela para criação de Conta  
    def novaJanela(self):
        self.loginform = Toplevel()
        self.loginform.title("NOVA CONTA")
        self.loginform.iconbitmap(pastaApp1 + "\\icons\\GD_ICON.ico")
        width = 650
        height = 620
        self.screen_width = app.winfo_screenmmwidth()
        self.screen_height = app.winfo_screenmmheight()
        x = (self.screen_width /1) - (width / 400)
        y = (self.screen_height / 1) - (height / 400)
        self.loginform.geometry("%dx%d+%d+%d" %  (width, height, x, y))
        self.loginform.resizable(0,0)
        self.AddNeW()

    # Frame para criação de Conta
    def AddNeW(self):
        TopAddNew = Frame(self.loginform, width=50, height=100, bd=0, relief=SOLID)
        TopAddNew.pack(side=TOP, pady=2)
        TopImage = Label(TopAddNew, image=self.LogoTela)
        TopImage.pack(fill=X)
        TopText = Label(TopAddNew, text= "DIGITE OS SEUS DADOS", font=('Cooper Black', 20), background="red", width=100)
        TopText.pack(fill=X)
        MidAddNew=Frame(self.loginform, width=600)
        MidAddNew.pack(side=TOP, pady=50)
        self.u_email = StringVar()
        self.u_senha1 = StringVar()
        self.genero = StringVar()
        self.u_nome1 = StringVar()
        self.u_nome2 = StringVar()
        self.user_name = StringVar()
        self.u_senha1 = StringVar()

        # =======================LABELS=============================

        self.u_nome1 = Label (MidAddNew,text="NOME", font =("Arial", 12, "bold"), bd=18)
        self.u_nome1.grid (row=0)

        self.u_nome2 = Label(MidAddNew,text="APELIDO", font =("Arial", 12, "bold"), bd=18)
        self.u_nome2.grid (row=1)

        txt_genero = Label(MidAddNew, text="GENÊRO", font = ("Arial", 12, "bold"), bd=18)
        txt_genero.grid(row=2)

        Male = ttk.Radiobutton(MidAddNew, text="Masculino", variable=self.genero, value="Masculino").grid(row=2, columnspan=2)
        Female = ttk.Radiobutton(MidAddNew, text="Feminino", variable=self.genero, value="Feminino").grid(row=2, column=1, sticky="e")

        self.u_email = Label(MidAddNew,text="E-MAIL", font =("Arial", 12, "bold"), bd=18)
        self.u_email.grid (row=3)

        self.user_name = Label(MidAddNew, text="USUÁRIO", font = ("Arial", 12, "bold"), bd=18)
        self.user_name.grid (row=4)

        self.u_senha1 = Label(MidAddNew, text ="SENHA", font =("Arial", 12, "bold"), bd=18)
        self.u_senha1.grid (row=5)


        #======================CAIXA PARA INSERÇÃO DE TEXTO========================

        self.u_nome1= Entry(MidAddNew, textvariable=self.u_nome1, font=('Arial', 12),width=35)
        self.u_nome1.grid(row=0, column=1)

        self.u_nome2= Entry(MidAddNew, textvariable=self.u_nome2, font=('Arial', 12), width=35)
        self.u_nome2.grid(row=1, column=1)

        self.u_email = Entry (MidAddNew, textvariable= self.u_email, font = ('Arial', 12), width=35)
        self.u_email.grid(row=3, column=1)

        self.user_name = Entry(MidAddNew, textvariable=self.user_name, font = ("Arial", 12), width=35)
        self.user_name.grid(row=4, column=1)

        self.u_senha1 = Entry (MidAddNew, textvariable=self.u_senha1, font = ('Arial', 12), width=35, show='*')
        self.u_senha1.grid(row=5, column=1)

        self.btn_criar = ttk.Button (MidAddNew, text="CRIAR CONTA", bootstyle = PRIMARY, width=15, command=self.Criacao_de_Conta)
        self.btn_criar.grid(row=6, column=1, sticky="e")

        self.btn_sair = ttk.Button (MidAddNew, text="SAIR", bootstyle = DANGER, width=15)
        self.btn_sair.grid(row=6)

        self.Saida1 = StringVar()
        self.lugar1 = Label(MidAddNew, textvariable=self.Saida1, font= ('Face Off M54 Regular', 14, "bold"),fg="black", bg="#0CF").grid(row=6, columnspan=2, pady=20)

 # ========================================== CRIAÇÃO DE CONTA =================================================
    def Criacao_de_Conta(self):

        if self.u_nome1.get() != "":
            self.vnome=self.u_nome1.get()
            self.vnome2=self.u_nome2.get()
            self.vemail=self.u_email.get()
            self.vnomeu = self.user_name.get()
            self.vgenero = self.genero.get()
            self.vsenha1=self.u_senha1.get()
            self.u_nome1.delete(0, END)
            self.u_nome2.delete(0, END)
            self.u_email.delete(0, END)
            self.user_name.delete(0, END)
            self.u_senha1.delete(0, END)
            self.Database()

            print("Dados Gravados")
            messagebox.showinfo(title="Aghasty GD Productions", message="Cadastro realizado com sucesso!")
        else:
            messagebox.showwarning(title="Aghasty GD Productions", message="Insira com os campos válidos")      

        if self.cursor.fetchone() is None:
            self.cursor.execute("INSERT INTO usuario (NOME, APELIDO, GENERO, EMAIL, NOME_DE_USUARIO, SENHA) values ('"+self.vnome+"','"+self.vnome2+"', '"+self.vgenero+"', '"+self.vemail+"', '"+self.vnomeu+"', '"+self.vsenha1+"')")
            self.conn.commit()

#=================================== BANCO DE DADOS ================================
    def Database(self):
        self.conn = sqlite3.connect(caminho)
        self.cursor = self.conn.cursor()
        self.cursor.execute("create table if not exists usuario (admin_id integer primary key, NOME text, APELIDO text, GENERO text, EMAIL text, NOME_DE_USUARIO text, SENHA text)")
       

    # ========================== CRIAÇÃO DA JANELA DO LOGIN =========================
    def novaJanela1(self):
        self.janelalogin = Toplevel()
        self.janelalogin.title("FAZER LOGIN")
        self.janelalogin.iconbitmap(pastaApp1 + "\\icons\\GD_ICON.ico")
        width = 516
        height = 265
        self.screen_width = app.winfo_screenmmwidth()
        self.screen_height = app.winfo_screenmmheight()
        x = (self.screen_width /1) - (width / 400)
        y = (self.screen_height / 1) - (height / 297)
        self.janelalogin.geometry("%dx%d+%d+%d" %  (width, height, x, y))
        self.janelalogin.resizable(0,0)
        self.teladelogin()

    def semComando():
        print("")

   
    def teladelogin(self):
  
        self.user_name = StringVar()
        self.u_senha1 = StringVar()
        FormadeLogin = Frame(self.janelalogin, width=600)
        FormadeLogin.pack(side=TOP, pady=50)
        self.l_usuario = Label(FormadeLogin, text = "USUÁRIO", font=('Arial', 15, 'bold'), fg='black', bg="white", bd=18)
        self.l_usuario.grid(row=0)

        self.l_senha = Label(FormadeLogin, text = "SENHA", font=('Arial', 15, 'bold'), fg='black', bg="white", bd=18)
        self.l_senha.grid(row=1)

        self.l_result = Label(FormadeLogin, text = "", font=('Arial, 18'),bg="white")
        self.l_result.grid(row=3, columnspan=2)

        self.userNAME = Entry(FormadeLogin, textvariable=self.user_name, font=('Arial',15), width=30)
        self.userNAME.grid(row=0, column=1)

        self.userSENHA = Entry(FormadeLogin, textvariable=self.u_senha1, font = ('Arial', 15), width=30, show = '*')
        self.userSENHA.grid(row=1, column=1)

        self.btn_login = ttk.Button(FormadeLogin, text="LOGIN", bootstyle=PRIMARY, width=15, command=self.entrada_de_dados)
        self.btn_login.grid(row=2, column=1, sticky="e")

        self.btn_sair1 =ttk.Button(FormadeLogin, text= "SAIR", bootstyle=DANGER, width=15)
        self.btn_sair1.grid(row=2, column=1, sticky="w")

        self.Saida = StringVar()
        self.lugar = Label(FormadeLogin, textvariable=self.Saida, font = ('Face Off M54 Regular', 14, "bold"),fg="black", bg="#0CF").grid(row=3, columnspan=2, pady=40)


    # Validação de dados no Login

    def entrada_de_dados(self):
        global admin_id
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()
        if self.user_name.get == "" or self.u_senha1.get() == "":
            messagebox.showwarning(title="Aghasty GD Productions", message="Por favor, entre com os campos válidos")
        else:
            cursor.execute("SELECT * FROM usuario WHERE NOME_DE_USUARIO = ? and SENHA = ?", (self.user_name.get(), self.u_senha1.get()))
            if cursor.fetchone() is not None:
                cursor.execute("SELECT * FROM usuario WHERE NOME_DE_USUARIO = ? and SENHA = ?", (self.user_name.get(), self.u_senha1.get()))
                data = cursor.fetchone()
                admin_id = data[0]
                self.user_name.set("")
                self.u_senha1.set("")
                messagebox.showinfo(title="Aghasty GD Productions", message="Seja Bem Vindo!")
                self.Saida.set("SEJA BEM VINDO!\n ACESSE O UTILITÁRIO NO CONSOLE")
                MyUtil()
            else:
                messagebox.showerror(title="Aghasty GD Producions", message="Usuário ou Senha Inválida, Tente Novamente")
                self.user_name.set("")
                self.u_senha1.set("")
        cursor.close()
        conn.close()

    #======================================= GRENCIAMENTO DE DADOS =====================================

    def GerirDados(self):
        root = Toplevel()
        root.title("Gerenciador de Dados")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        width = 1200
        height = 600
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        root.resizable(0, 0)


        pastaApp1=os.path.dirname(__file__)
        caminho = pastaApp1 + "\\system\\data\\Database_01.db"

        #==================================METHODS============================================
        def Database():
            global conn, cursor
            conn = sqlite3.connect(caminho)
            cursor = conn.cursor()
            cursor.execute ("create table if not exists usuario (admin_id integer primary key, NOME text, APELIDO text, GENERO text, EMAIL text, NOME_DE_USUARIO text, SENHA text)")
            
            
        def Create():
            if  PRIMEIRO__NOME.get() == "" or ULTIMO__NOME.get() == "" or GENERO.get() == "" or E__MAIL.get() == "" or NOME__DE__USUARIO.get() == "" or SENHA.get() == "":
                txt_result.config(text="Por favor, preencha os campos requeridos", fg="red")
            else:
                Database()
                cursor.execute("INSERT INTO `usuario` (NOME, APELIDO, GENERO, EMAIL, NOME_DE_USUARIO, SENHA) VALUES(?, ?, ?, ?, ?, ?)", (str(PRIMEIRO__NOME.get()), str(ULTIMO__NOME.get()), str(GENERO.get()), str(E__MAIL.get()), str(NOME__DE__USUARIO.get()), str(SENHA.get())))
                tree.delete(*tree.get_children())
                cursor.execute("SELECT * FROM `usuario` ORDER BY `APELIDO` ASC")
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
                conn.commit()
                PRIMEIRO__NOME.set("")
                ULTIMO__NOME.set("")
                GENERO.set("")
                E__MAIL.set("")
                NOME__DE__USUARIO.set("")
                SENHA.set("")
                cursor.close()
                conn.close()
                txt_result.config(text="Criou um dado!", fg="green")

        def Read():
            tree.delete(*tree.get_children())
            Database()
            cursor.execute("SELECT * FROM `usuario` ORDER BY `APELIDO` ASC")
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
            cursor.close()
            conn.close()
            txt_result.config(text="Dados verificados com sucesso!",  fg="white")

        def Update():
            Database()
            if GENERO.get() == "":
                txt_result.config(text="Por favor selecione um genêro", fg="red")
            else:
                tree.delete(*tree.get_children())
                cursor.execute("UPDATE `usuario` SET `NOME` = ?, `APELIDO` = ?, `GENERO` =?,  `EMAIL` = ?,  `NOME_DE_USUARIO` = ?, `SENHA` = ? WHERE `admin_id` = ?", (str(PRIMEIRO__NOME.get()), str(ULTIMO__NOME.get()), str(GENERO.get()), str(E__MAIL.get()), str(NOME__DE__USUARIO.get()), str(SENHA.get()), int(admin_id)))
                conn.commit()
                cursor.execute("SELECT * FROM `usuario` ORDER BY `APELIDO` ASC")
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
                cursor.close()
                conn.close()
                PRIMEIRO__NOME.set("")
                ULTIMO__NOME.set("")
                GENERO.set("")
                E__MAIL.set("")
                NOME__DE__USUARIO.set("")
                SENHA.set("")
                btn_create.config(state=NORMAL)
                btn_read.config(state=NORMAL)
                btn_update.config(state=DISABLED)
                btn_delete.config(state=NORMAL)
                txt_result.config(text="Dados atualizados com sucesso!", fg="black")


        def OnSelected(event):
            global admin_id;
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            admin_id = selecteditem[0]
            PRIMEIRO__NOME.set("")
            ULTIMO__NOME.set("")
            GENERO.set("")
            E__MAIL.set("")
            NOME__DE__USUARIO.set("")
            SENHA.set("")
            PRIMEIRO__NOME.set(selecteditem[1])
            ULTIMO__NOME.set(selecteditem[2])
            E__MAIL.set(selecteditem[4])
            NOME__DE__USUARIO.set(selecteditem[5])
            SENHA.set(selecteditem[6])
            btn_create.config(state=DISABLED)
            btn_read.config(state=DISABLED)
            btn_update.config(state=NORMAL)
            btn_delete.config(state=DISABLED)

        def Delete():
            if not tree.selection():
                txt_result.config(text="Por favor, selecione um item primeiro", fg="red")
            else:
                result = tkMessageBox.askquestion('Gerenciador de Dados', 'Tem certeza que quer apagar este dado?', icon="warning")
                if result == 'yes':
                        curItem = tree.focus()
                        contents =(tree.item(curItem))
                        selecteditem = contents['values']
                        tree.delete(curItem)
                        Database()
                        cursor.execute("DELETE FROM `usuario` WHERE `admin_id` = %d" % selecteditem[0])
                        conn.commit()
                        cursor.close()
                        conn.close()
                        txt_result.config(text="Dado deletado com sucesso!", fg="black")
                    
            
        def Exit():
            result = tkMessageBox.askquestion('Gerenciador de Dados', 'Tem certeza que quer sair?', icon="warning")
            if result == 'yes':
                root.destroy()
                exit()

        #==================================VARIAVÉIS==========================================
        PRIMEIRO__NOME = StringVar()
        ULTIMO__NOME = StringVar()
        GENERO = StringVar()
        E__MAIL = StringVar()
        NOME__DE__USUARIO = StringVar()
        SENHA = StringVar()

        #==================================FRAME==============================================
        Top = ttk.Frame(root, width=900, height=50,  relief="raise")
        Top.pack(side=TOP)
        Left = ttk.Frame(root, width=300, height=500,  relief="raise")
        Left.pack(side=LEFT)
        Right = ttk.Frame(root, width=600, height=500, relief="raise")
        Right.pack(side=RIGHT)
        Forms = ttk.Frame(Left, width=300, height=450)
        Forms.pack(side=TOP)
        Buttons = ttk.Frame(Left, width=300, height=100,  relief="raise")
        Buttons.pack(side=BOTTOM)
        RadioGroup = ttk.Frame(Forms)
        Male = ttk.Radiobutton(RadioGroup, text="Masculino", variable=GENERO, value="Masculino", ).pack(side=LEFT)
        Female = ttk.Radiobutton(RadioGroup, text="Feminino", variable=GENERO, value="Feminino", ).pack(side=LEFT)

        #==================================LABEL WIDGET=======================================
        txt_title = Label(Top, width=900, font=('Cooper Black', 24), text = "GERENCIE OS DADOS REGISTRADOS ")
        txt_title.pack()
        txt_firstname = Label(Forms, text="Nome:", font=('arial', 16), bd =18)
        txt_firstname.grid(row=0, sticky="e")
        txt_lastname = Label(Forms, text="Apelido:", font=('arial', 16), bd = 18)
        txt_lastname.grid(row=1, sticky="e")
        txt_gender = Label(Forms, text="Genêro:", font=('arial', 16), bd = 18)
        txt_gender.grid(row=2, sticky="e")
        txt_address = Label(Forms, text="E-Mail:", font=('arial', 16), bd = 18)
        txt_address.grid(row=3, sticky="e")
        txt_username = Label(Forms, text="Nome de Usuário:", font=('arial', 16), bd = 18)
        txt_username.grid(row=4, sticky="e")
        txt_password = Label(Forms, text="Senha:", font=('arial', 16), bd = 18)
        txt_password.grid(row=5, sticky="e")
        txt_result = Label(Buttons)
        txt_result.pack(side=TOP)

        #==================================ENTRY WIDGET=======================================
        firstname = Entry(Forms, textvariable=PRIMEIRO__NOME, width=30)
        firstname.grid(row=0, column=1)
        lastname = Entry(Forms, textvariable=ULTIMO__NOME, width=30)
        lastname.grid(row=1, column=1)
        RadioGroup.grid(row=2, column=1)
        address = Entry(Forms, textvariable=E__MAIL, width=30)
        address.grid(row=3, column=1)
        username = Entry(Forms, textvariable=NOME__DE__USUARIO, width=30)
        username.grid(row=4, column=1)
        password = Entry(Forms, textvariable=SENHA, show="*", width=30)
        password.grid(row=5, column=1)

        #==================================BUTTONS WIDGET=====================================
        btn_create = ttk.Button(Buttons, width=10, text="Criar", bootstyle = PRIMARY, command=Create)
        btn_create.pack(side=LEFT)
        btn_read = ttk.Button(Buttons, width=10, text="Verificar", bootstyle = SUCCESS, command=Read )
        btn_read.pack(side=LEFT)
        btn_update = ttk.Button(Buttons, width=10, text="Atualizar", bootstyle = INFO, command=Update, state=DISABLED)
        btn_update.pack(side=LEFT)
        btn_delete = ttk.Button(Buttons, width=10, text="Deletar", bootstyle = DANGER, command=Delete)
        btn_delete.pack(side=LEFT)
        btn_exit = ttk.Button(Buttons, width=10, text="Sair", bootstyle = SECONDARY, command=Exit)
        btn_exit.pack(side=LEFT)

        #==================================LIST WIDGET========================================
        scrollbary = ttk.Scrollbar(Right, orient=VERTICAL)
        scrollbarx = ttk.Scrollbar(Right, orient=HORIZONTAL)
        tree = ttk.Treeview(Right, columns=("ID do Membro", "Nome", "Apelido", "Genêro", "E-Mail", "Nome de Usuário", "Senha"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('ID do Membro', text="ID do Membro", anchor=W)
        tree.heading('Nome', text="Nome", anchor=W)
        tree.heading('Apelido', text="Apelido", anchor=W)
        tree.heading('Genêro', text="Genêro", anchor=W)
        tree.heading('E-Mail', text="E-Mail", anchor=W)
        tree.heading('Nome de Usuário', text="Nome de Usuário", anchor=W)
        tree.heading('Senha', text="Senha", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=0)
        tree.column('#2', stretch=NO, minwidth=0, width=80)
        tree.column('#3', stretch=NO, minwidth=0, width=120)
        tree.column('#4', stretch=NO, minwidth=0, width=80)
        tree.column('#5', stretch=NO, minwidth=0, width=150)
        tree.column('#6', stretch=NO, minwidth=0, width=120)
        tree.column('#7', stretch=NO, minwidth=0, width=120)
        tree.pack()
        tree.bind('<Double-Button-1>', OnSelected)

        #==================================INITIALIZATION=====================================
        if __name__ == '__main__':
            root.mainloop()


    def sobrenosTELA(self):
        self.janelasobre = Toplevel()
        self.janelasobre.title("SOBRE NOS")
        width = 850
        height = 550
        self.screen_width = app.winfo_screenmmwidth()
        self.screen_height = app.winfo_screenmmheight()
        x = (self.screen_width /1) - (width / 400)
        y = (self.screen_height / 1) - (height / 400)
        self.janelasobre.geometry("%dx%d+%d+%d" %  (width, height, x, y))
        self.sobrenosFrame()

    def sobrenosFrame(self):

        FormadaJanela = Frame(self.janelasobre, width=600)
        FormadaJanela.pack(side=TOP, pady=60)
        fundo = StringVar()
        Label(FormadaJanela, textvariable=fundo).place(x=0, y=0,width=500, height=300)
        Saida1 = StringVar()
        Label(FormadaJanela, textvariable=Saida1, font= "9").grid(row=1)
    
        Saida2 = StringVar()
        Label(FormadaJanela, textvariable=Saida2, font="9").grid(row=2)
        Saida1.set("""Este aqui é apenas um pequeno sistema que desenvolvi com o Tkinter e SQLite para praticar o Python.
        Nele é possível você fazer cadastros, consultar dados, atualizar e remover. Também com a possibilidade de fazer
        login e acessar alguns programas ou jogos desenvolvidos por mim.""")
        Saida2.set("Obrigado por executar e tenha uma boa experiência!")


def MyUtil():
    from cgitb import text
    from turtle import width
    import numpy as np
    import ttkbootstrap as ttk
   
    pastaApp1=os.path.dirname(__file__)

    def Calculo_de_Media():   
        n1 = float (input ('Por favor, Digite o primeira nota: '))
        n2 = float (input ('Segunda nota: '))
        n3 = float (input ('Terceira nota: '))
        s = n1 + n2 + n3
        d = s / 3
        print ('A média entre {}, {} e {} é igual a {}'.format(n1, n2, n3, d))

    def Conversor_de_Metical():
        metical = float (input ('Quantos meticais você tem na carteira: '))
        dolar = metical / 63
        print ('Com {} MT, você pode comprar {} USD'.format(metical, dolar))

    def tabuada():
        numero = int (input ('Digite um número para ver a sua tabuada: '))
        for sequencia in range (1,13):
            print ('%2d x %2d = %3d' % (sequencia, numero, sequencia*numero))

    def Calcular_Quantidade_de_Tinta():
        larg = float (input ('Forneça a Largura da parede: '))
        alt = float (input('Altura da parede: '))
        area = larg * alt
        print ('Sua parede tem a dimensão de {}x{} e a sua área é de {}m2'.format(larg, alt, area))
        tinta = area / 2
        print ('Para pintar essa parede, você pricisará de {}l de tinta'.format(tinta))

    def Contador_de_Letras():
        frase = input('Digite a sua frase ')
        letra = len(frase)
        print("Otimo!\nAqui esta a quantidade de caracteres na sua frase:",letra)
            

    def Jogo_Da_Velha():
            from tkinter import messagebox
            from turtle import width
            import numpy as np

            size_of_board = 600
            symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
            symbol_thickness = 50
            symbol_X_color = '#EE4035'
            symbol_O_color = '#0492CF'
            Green_color = '#7BC043'

            class Tic_Tac_Toe():
                # ------------------------------------------------------------------
                # Funções para Inicialização do Jogo:
                # ------------------------------------------------------------------
                def __init__(self):
                    self.window = Tk()
                    self.window.title('Jogo da Velha')
                    self.window.configure(background="white")
                    self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
                    self.canvas.pack()
                    # Entra do usuário em forma do clique do Mouse
                    self.window.bind('<Button-1>', self.click)

                    self.initialize_board()
                    self.player_X_turns = True
                    self.board_status = np.zeros(shape=(3, 3))

                    self.player_X_starts = True
                    self.reset_board = False
                    self.gameover = False
                    self.tie = False
                    self.X_wins = False
                    self.O_wins = False

                    self.X_score = 0
                    self.O_score = 0
                    self.tie_score = 0

                def mainloop(self):
                    self.window.mainloop()

                def initialize_board(self):
                    for i in range(2):
                        self.canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

                    for i in range(2):
                        self.canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

                def play_again(self):
                    self.initialize_board()
                    self.player_X_starts = not self.player_X_starts
                    self.player_X_turns = self.player_X_starts
                    self.board_status = np.zeros(shape=(3, 3))

                # ------------------------------------------------------------------
                # FUNÇÕES PARA DESENHO:
                # Os modúlos requeridos para desenhar o jogo baseado nos objetos em canva
                # ------------------------------------------------------------------

                def draw_O(self, logical_position):
                    logical_position = np.array(logical_position)
                    # logical_position = grid value on the board
                    # grid_position = actual pixel values of the center of the grid
                    grid_position = self.convert_logical_to_grid_position(logical_position)
                    self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                            grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                            outline=symbol_O_color)

                def draw_X(self, logical_position):
                    grid_position = self.convert_logical_to_grid_position(logical_position)
                    self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                            grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                            fill=symbol_X_color)
                    self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                            grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=symbol_thickness,
                                            fill=symbol_X_color)

                def display_gameover(self):

                    if self.X_wins:
                        self.X_score += 1
                        text = messagebox.showinfo("Vencedor", 'Jodador 1 venceu a rodada!')
                        color = symbol_X_color
                        
                    elif self.O_wins:
                        self.O_score += 1
                        text = messagebox.showinfo("Vencedor", 'Jodador 2 venceu a rodada!')
                        color = symbol_O_color
                    else:
                        self.tie_score += 1
                        text = messagebox.showinfo('Empate', "Jogo empatado")
                        color = 'gray'

                    self.canvas.delete("all")
                    self.canvas.create_text(size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=color, text=text)

                    score_text = 'Pontuação \n'
                    self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                            text=score_text)

                    score_text = 'Jogador 1 (X) : ' + str(self.X_score) + '\n'
                    score_text += 'Jogador 2 (O) : ' + str(self.O_score) + '\n'
                    score_text += 'Empate     : ' + str(self.tie_score)
                    self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                            text=score_text)
                    self.reset_board = True

                    score_text = 'Clique para jogar novamente \n'
                    self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="white",
                                            text=score_text)

                # ------------------------------------------------------------------
                # LÓGICA DO JOGO:
                # The modules required to carry out game logic
                # ------------------------------------------------------------------

                def convert_logical_to_grid_position(self, logical_position):
                    logical_position = np.array(logical_position, dtype=int)
                    return (size_of_board / 3) * logical_position + size_of_board / 6

                def convert_grid_to_logical_position(self, grid_position):
                    grid_position = np.array(grid_position)
                    return np.array(grid_position // (size_of_board / 3), dtype=int)

                def is_grid_occupied(self, logical_position):
                    if self.board_status[logical_position[0]][logical_position[1]] == 0:
                        return False
                    else:
                        return True

                def is_winner(self, player):

                    player = -1 if player == 'X' else 1

                    # Three in a row
                    for i in range(3):
                        if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                            return True
                        if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                            return True

                    # Diagonais
                    if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
                        return True

                    if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
                        return True

                    return False

                def is_tie(self):

                    r, c = np.where(self.board_status == 0)
                    tie = False
                    if len(r) == 0:
                        tie = True

                    return tie

                def is_gameover(self):
                    # Either someone wins or all grid occupied
                    self.X_wins = self.is_winner('X')
                    if not self.X_wins:
                        self.O_wins = self.is_winner('O')

                    if not self.O_wins:
                        self.tie = self.is_tie()

                    gameover = self.X_wins or self.O_wins or self.tie

                    if self.X_wins:
                        print('X ganhou')
                    if self.O_wins:
                        print('O ganhou')
                    if self.tie:
                        print('Empate')

                    return gameover


                def click(self, event):
                    grid_position = [event.x, event.y]
                    logical_position = self.convert_grid_to_logical_position(grid_position)

                    if not self.reset_board:
                        if self.player_X_turns:
                            if not self.is_grid_occupied(logical_position):
                                self.draw_X(logical_position)
                                self.board_status[logical_position[0]][logical_position[1]] = -1
                                self.player_X_turns = not self.player_X_turns
                        else:
                            if not self.is_grid_occupied(logical_position):
                                self.draw_O(logical_position)
                                self.board_status[logical_position[0]][logical_position[1]] = 1
                                self.player_X_turns = not self.player_X_turns

                        # Check if game is concluded
                        if self.is_gameover():
                            self.display_gameover()
                            # print('Done')
                    else:  # Play Again
                        self.canvas.delete("all")
                        self.play_again()
                        self.reset_board = False


            game_instance = Tic_Tac_Toe()
            game_instance.mainloop()

    opc = Toplevel()
    screen_width = opc.winfo_screenwidth()
    screen_height = opc.winfo_screenheight()
    width = 500
    height = 300
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    opc.geometry('%dx%d+%d+%d' % (width, height, x, y))
    menuprincipal = Label(opc, text="SEJA BEM VINDO AO MENU\n POR FAVOR, SELECIONE UMA OPÇÃO\n").pack(side=TOP)
    Botao1 = ttk.Button(opc,text="CALCULADOR DE MEDIA", width=30, command=Calculo_de_Media).pack(pady=2)
    Botao2 = ttk.Button(opc,text="CONVERSOR DE MOEDA", width=30, command=Conversor_de_Metical).pack(pady=2)
    Botao3 = ttk.Button(opc,text="CÁLCULO DE DIMENSÕES", width=30, command=Calcular_Quantidade_de_Tinta).pack(pady=2)
    Botao4 = ttk.Button(opc,text="CONTADOR DE CARACTÉRES", width=30, command=Contador_de_Letras).pack(pady=2)
    Botao5 = ttk.Button(opc,text="TABUADA", width=30, command=tabuada).pack(pady=2)
    Botao6 = ttk.Button(opc,text="JOGO DA VELHA", width=30, command=Jogo_Da_Velha).pack(pady=2)
    Botao7 = ttk.Button(opc,text="SAIR", bootstyle= DANGER, width=30, command=exit).pack(pady=2)

    
app = ttk.Window(themename="superhero")
myapp = MyApp(app)
app.title("Aghasty GD Productions")
app.iconbitmap(pastaApp1+"\\icons\\GD_ICON.ico")
app.geometry("800x520")
app.resizable(0, 0)
inforTitulo = ttk.Label(app, text="SEJA BEM VINDO AO SISTEMA DA AGHASTY GD PRODUCTIONS\n", font = "BAUHS93 18 bold", bootstyle = DANGER).pack()
infor = ttk.Label (app, text="Faça o seu Cadastro\n\nGerencie Usuários\n\nFaça Login em sua Conta\n\nAcesse o Menu Principal e:\n\nJogue Video Games\n\nFaça Cálculos\n\nFaça Câmbio de Moedas\n\ne muitas outras utilidades", font="comic 19 bold", bootstyle=SUCCESS).pack(padx=0, pady=0)

app.mainloop()