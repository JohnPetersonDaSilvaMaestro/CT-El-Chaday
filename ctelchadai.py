from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import datetime, subprocess, sqlite3, os, pathlib, base64
from base64 import b64decode

janela = Tk()
banco = sqlite3.connect('ctelchadai.db')
cursor = banco.cursor()

class Application():
    def __init__(self):
        self.janela = janela
        self.tela()        
        janela.mainloop()

    def tela(self):        
        self.janela.title("Centro de Tratamento Elchadai")
        window_height = 700
        window_width = 915
        self.janela.resizable(False, False)
        screen_width = self.janela.winfo_screenwidth()
        screen_height = self.janela.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.janela.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.janela.configure(background="#22aaee")

def cadastrarInterno(self):
    print(1)

def placeholder(entrada):    
    entrada.delete(0, 'end')
    entrada.config(fg='black')

def estavazio(entrada, mensagem):
    if entrada.get() == '':
        entrada.insert(0, mensagem)
        entrada.config(fg='dark gray')

def dataAtual():
    hoje = datetime.datetime.now()
    if hoje.date().month == 1 :  mês = 'janeiro'
    if hoje.date().month == 2 :  mês = 'fevereiro'
    if hoje.date().month == 3 :  mês = 'março'
    if hoje.date().month == 4 :  mês = 'abril'
    if hoje.date().month == 5 :  mês = 'maio'
    if hoje.date().month == 6 :  mês = 'junho'
    if hoje.date().month == 7 :  mês = 'julho'
    if hoje.date().month == 8 :  mês = 'agosto'
    if hoje.date().month == 9 :  mês = 'setembro'
    if hoje.date().month == 10 : mês = 'outubro'
    if hoje.date().month == 11 : mês = 'novembro'
    if hoje.date().month == 12 : mês = 'dezembro'
    return str(hoje.date().day) + ' de ' + mês + ' de ' + str(hoje.date().year)

def gerarFichaCadastro():
    mensagem = ''
    if simNao.get() == 'Filhos' : mensagem += 'Selecione se possui filhos\n'
    if escolaridade.get() == 'Escolaridade' : mensagem += 'Selecione a escolaridade\n'
    if estadoCivil.get() == 'Estado Civil' : mensagem += 'Selecione o estado civil\n'
    if dependencias.get() == 'Tipo de dependência' : mensagem += 'Selecione o tipo de dependência\n'

    if mensagem != '':
        messagebox.showerror('Campos vazios', message=mensagem)
    else:
        cnv = canvas.Canvas("Inscrição.pdf")
        cnv.setTitle("Relatório")    
        cnv.drawCentredString(text='Termo de Adesão', x=105*mm,y= 280*mm)
        cnv.drawString(text='I. Identificação da Entidade', x=50,y=275*mm)
        cnv.drawString(text='Nome: Centro de Reabilitação Desafio do Jovem', x=50,y=270*mm)
        cnv.drawString(text='CNPJ: 10.770.476/0001-65', x=50,y=265*mm)
        nomeAcolhido = inputAcolhidoNome.get() if inputAcolhidoNome.get() != "Nome do(a) acolhido(a)" else ''
        dataNascimentoAcolhido = inputAcolhidoDataNascimento.get() if inputAcolhidoDataNascimento.get() != "Nascimento: 00/00/0000" else ''
        identidadeAcolhido = inputAcolhidoIdentidade.get() if inputAcolhidoIdentidade.get() != "Número do RG" else ''
        cpfAcolhido = inputAcolhidoCpf.get() if inputAcolhidoCpf.get() != "Número do CPF" else ''
        cepAcolhido = inputAcolhidoCep.get() if inputAcolhidoCep.get() != "CEP" else ''
        enderecoAcolhido = inputAcolhidoEndereço.get() if inputAcolhidoEndereço.get() != "Endereço" else ''
        bairroAcolhido = inputAcolhidoBairro.get() if inputAcolhidoBairro.get() != "Bairro" else ''
        municipioAcolhido = inputAcolhidoMunicípio.get() if inputAcolhidoMunicípio.get() != "Município" else ''
        ufAcolhido = inputAcolhidoUf.get() if inputAcolhidoUf.get() != "UF" else ''
        telefoneAcolhido = inputAcolhidoTelefone.get() if inputAcolhidoTelefone.get() != "Número do Telefone" else ''
        nomeResponsavel = inputResponsavelNome.get() if inputResponsavelNome.get() != "Nome do(a) Responsável" else ''
        identidadeResponsavel = inputResponsávelIdentidade.get() if inputResponsávelIdentidade.get() != "Número do RG" else ''
        cpfResponsavel = inputResponsávelCpf.get() if inputResponsávelCpf.get() != "Número do CPF" else ''
        enderecoResponsavel = inputResponsávelEndereço.get() if inputResponsávelEndereço.get() != "Endereço" else ''
        bairroResponsavel = inputResponsávelBairro.get() if inputResponsávelBairro.get() != "Bairro" else ''
        municipioResponsavel = inputResponsávelMunicípio.get() if inputResponsávelMunicípio.get() != "Município" else ''
        ufResponsavel = inputResponsávelUf.get() if inputResponsávelUf.get() != "UF" else ''
        telefoneResponsavel = inputResponsávelTelefone.get() if inputResponsávelTelefone.get() != "Número do Telefone" else ''
        parentesco = inputResponsávelParentesco.get() if inputResponsávelParentesco.get() != "Parentesco" else ''
        cnv.drawString(text='II. Dados da pessoa acolhida', x=50,y=255*mm)
        cnv.drawString(text='Nome de Registro:', x=50,y=250*mm)
        cnv.drawString(text=nomeAcolhido, x=162, y=250*mm)
        cnv.drawString(text='Data de Nascimento:', x=50, y=245*mm)
        cnv.drawString(text=dataNascimentoAcolhido, x=174, y=245*mm)
        cnv.drawString(text='Identidade:', x=50, y=240*mm)
        cnv.drawString(text=identidadeAcolhido, x=126, y=240*mm)
        cnv.drawString(text='CPF:', x=400, y=240*mm)
        cnv.drawString(text=cpfAcolhido, x=429, y=240*mm)
        cnv.drawString(text='Endereço:', x=50, y=235*mm)
        cnv.drawString(text=enderecoAcolhido, x=109, y=235*mm)
        cnv.drawString(text='Bairro:', x=400, y=235*mm)
        cnv.drawString(text=bairroAcolhido, x=447, y=235*mm)
        cnv.drawString(text='Município:', x=50, y=230*mm)
        cnv.drawString(text=municipioAcolhido, x=115, y=230*mm)
        cnv.drawString(text='UF:', x=400, y=230*mm)
        cnv.drawString(text=ufAcolhido, x=423, y=230*mm)
        cnv.drawString(text='Telefone:', x=50, y=225*mm)
        cnv.drawString(text=telefoneAcolhido, x=109, y=225*mm)
        cnv.drawString(text='Cep:', x=400, y=225*mm)
        cnv.drawString(text=cepAcolhido, x=429, y=225*mm)
        cnv.drawString(text='III. Dados do responsável legal (se for o caso)', x=50,y=215*mm)
        cnv.drawString(text='Nome:', x=50,y=210*mm)
        cnv.drawString(text=nomeResponsavel, x=135, y=210*mm)
        cnv.drawString(text='Identidade:', x=50, y=205*mm)
        cnv.drawString(text=identidadeResponsavel, x=121, y=205*mm)
        cnv.drawString(text='CPF:', x=400, y=205*mm)
        cnv.drawString(text=cpfResponsavel, x=429, y=205*mm)
        cnv.drawString(text='Endereço:', x=50, y=200*mm)
        cnv.drawString(text=enderecoResponsavel, x=109, y=200*mm)
        cnv.drawString(text='Bairro:', x=400, y=200*mm)
        cnv.drawString(text=bairroResponsavel, x=447, y=200*mm)
        cnv.drawString(text='Município:', x=50, y=195*mm)
        cnv.drawString(text=municipioResponsavel, x=115, y=195*mm)
        cnv.drawString(text='UF:', x=400, y=195*mm)
        cnv.drawString(text=ufResponsavel, x=420, y=195*mm)
        cnv.drawString(text='Telefone:', x=50, y=190*mm)
        cnv.drawString(text=telefoneResponsavel, x=109, y=190*mm)
        cnv.drawString(text='Grau de parentesco:', x=50, y=185*mm)
        cnv.drawString(text=parentesco, x=169, y=185*mm)
        cnv.drawString(text='IV. Declaração da pessoa acolhida e/ou responsável', x=50, y=175*mm)
        estiloParagrafo = ParagraphStyle('f',firstLineIndent=50, alignment=4)
        declaracao = Paragraph('Declaro que tomei conhecimento das normas da entidade especificada, com as quais concordo, e que tomei conhecimento do caráter gratuito e voluntário do acolhimento.', style=estiloParagrafo)

        declaracao.wrapOn(cnv, 515, 30)
        declaracao.drawOn(cnv, 50, 165*mm)

        cnv.drawAlignedString(565, 150*mm, 'Marau, ' + dataAtual(), direction='LTR')
        cnv.line(150, 125*mm, 450, 125*mm)
        cnv.drawCentredString(105*mm, 120*mm, 'Assinatura da pessoa acolhida e/ou responsável')

        cnv.save()
        subprocess.Popen(['Inscrição.pdf'], shell=True)
        botaoInserirFichaAssinada.place(x= 730, y=280)

def recuperarPdf():
    cursor.execute("SELECT * FROM receitas")
    l = cursor.fetchall()
    b64 = l[0][2]
    base64EncodedStr = base64.b64encode(b64)
    bytes = b64decode(base64EncodedStr, validate=True)
    if bytes[0:4] != b'%PDF':
        raise ValueError('Missing the PDF file signature')
    f = open('file.pdf', 'wb')
    f.write(bytes)
    f.close()
    subprocess.Popen(['file.pdf'], shell=True)

def gerarRelatorioAcolhimento(evento):
    cpf = inputInterno.get()    
    cursor.execute("SELECT * FROM internos WHERE cpf = '"+cpf+"'" )
    banco.commit()
    dados = cursor.fetchall()    
    for i in l:
        c = i[0]
        n = i[1]
        dN = i[2]
        rg = i[3]
        cep = i[4]
        uf = i[5]
        mu = i[6]
        ba = i[7]
        e = i[8]
        t = i[9]
        f = i[10]
        r = i[11]
        d = i[12]
        esc = i[13]
        dE = i[14]
        dS = i[15]
        mS = i[16]
        eC = i[17]
        rN = i[18]
        rP = i[19]
        rI = i[20]
        rCPF = i[21]
        rCep = i[22]
        rUf = i[23]
        rMu = i[24]
        rB = i[25]
        rE = i[26]       
        #print(c + "|" + n+ "|" +dN+ "|" +rg+ "|" +cep+ "|" +uf+ "|" +mu+ "|" +ba+ "|" +e+ "|" +t+ "|" +f+ "|" +r+ "|" +d+ "|" +esc+ "|" +dE+ "|" +dS+ "|" +mS+ "|" +eC+ "|" +rN+ "|" +rP+ "|" +rI+ "|" +rCPF+ "|" +rCep+ "|" +rUf+ "|" +rMu+ "|" +rB+ "|" +rE)
    med = cursor.execute("SELECT * FROM medicamentos WHERE cpf = '"+cpf+"'")
    for l in med:
        nMed = l[1]
        remedio = l[2]
        medicoMed = l[3]
        receitaMed = l[4]
        
    reg = cursor.execute("SELECT * FROM registro WHERE cpf = '"+cpf+"'")
    for k in reg:
        nomeRegistro = k[1]
        registro = k[2]
        dataRegistro = k[3]
        registrador = k[4]   
       

listaSimNao = ['Filhos', 'Sim', 'Não']
listaEscolaridade = ['Escolaridade','Analfabeto', 'Lê e escreve', 'Ensino Fundamental Incompleto', 'Ensino Fundamental Completo', 'Ensino Médio Incompleto', 'Ensino Médio Completo', 'Ensino Superior Incompleto', 'Ensino Superior Completo']
listaEstadoCivil = ['Estado Civil','Solteiro(a)', 'Casado(a)', 'Separado(a) Judicialmente', 'Divorciado(a)', 'Viúvo(a)']
listaDependencias = ['Tipo de dependência','Álcool', 'Maconha / Haxixe','Cocaína', 'Crack', 'Inalantes / Cola / Solvente / Tiner', 'Benzodiazepínico / Diazepan', 'Anfetaminas / Remédios para Emagrecer', 'Ecstasy / MDMA', 'LSD', 'Heroína / Morfina / Metadona']

##########__________________________________________________________________________________________Tela de cadastro

simNao = StringVar()
simNao.set(listaSimNao[0])
escolaridade = StringVar()
escolaridade.set(listaEscolaridade[0])
estadoCivil = StringVar()
estadoCivil.set(listaEstadoCivil[0])
dependencias = StringVar()
dependencias.set(listaDependencias[0])

abas = ttk.Notebook(janela)
abas.place(x=0, y=0, width=915, height=700)

abaDados = Frame(abas)
abaEntradas = Frame(abas)
abaSaidas = Frame(abas)
abaVisitas = Frame(abas)
abaPIA = Frame(abas)
abaInternos = Frame(abas)

abas.add(abaDados, text='Dados Pessoais')
abas.add(abaEntradas, text='Entradas')
abas.add(abaSaidas, text="Saídas")
abas.add(abaVisitas, text='Visitas')
abas.add(abaPIA, text='PIA - Plano Individual de Atendimento')
abas.add(abaInternos, text='Internos')
abas.enable_traversal()

tabela = ttk.Treeview(abaPIA, selectmode='browse', column=('Coluna 1', '2', '3',), show='headings', height=10)
tabelaEntradaMunicipio = ttk.Treeview(abaEntradas, selectmode="browse", columns=('1', '2', '3','4'), show='headings', height=29)
tabelaSaidas = ttk.Treeview(abaSaidas, selectmode="browse", columns=('1', '2', '3','4'), show='headings', height= 29)
tabelaVisitas = ttk.Treeview(abaVisitas, selectmode="browse", columns=('1', '2', '3'), show='headings', height=28)
tabelaInternos = ttk.Treeview(abaInternos, selectmode="browse", columns=('1', '2', '3'), show='headings', height=31)
tabelaRegistros = ttk.Treeview(abaPIA, selectmode="browse", columns=('1', '2', '3'), show='headings', height=10)

labelDadosAcolhido = Label(abaDados, text="DADOS DO(A) ACOLHIDO(A): ").place(x=100, y=10)

inputAcolhidoNome = Entry(abaDados, width=74, fg='dark gray')
inputAcolhidoNome.insert(0, "Nome do(a) acolhido(a)")
inputAcolhidoNome.bind('<FocusIn>', lambda p:placeholder(inputAcolhidoNome))
inputAcolhidoNome.bind('<FocusOut>', lambda p:estavazio(inputAcolhidoNome, "Nome do(a) acolhido(a)"))
inputAcolhidoNome.place(x=10, y=40)

inputAcolhidoDataNascimento = Entry(abaDados, width=22, fg='dark gray')
inputAcolhidoDataNascimento.place(x=464, y=40)
inputAcolhidoDataNascimento.insert(0, "Nascimento: 00/00/0000")
inputAcolhidoDataNascimento.bind('<FocusIn>', lambda p:placeholder(inputAcolhidoDataNascimento))
inputAcolhidoDataNascimento.bind('<FocusOut>', lambda p:estavazio(inputAcolhidoDataNascimento, "Nascimento: 00/00/0000"))

inputAcolhidoCpf = Entry(abaDados, width=15, fg='dark gray')
inputAcolhidoCpf.place(x=606, y=40)
inputAcolhidoCpf.insert(0, "Número do CPF")
inputAcolhidoCpf.bind('<FocusIn>', lambda p:placeholder(inputAcolhidoCpf))
inputAcolhidoCpf.bind('<FocusOut>', lambda p:estavazio(inputAcolhidoCpf, "Número do CPF"))

inputAcolhidoIdentidade = Entry(abaDados, width=20, fg='dark gray')
inputAcolhidoIdentidade.place(x=706, y=40)
inputAcolhidoIdentidade.insert(0, "Número do RG")
inputAcolhidoIdentidade.bind('<FocusIn>', lambda p:placeholder(inputAcolhidoIdentidade))
inputAcolhidoIdentidade.bind('<FocusOut>', lambda p:estavazio(inputAcolhidoIdentidade, "Número do RG"))

inputAcolhidoTelefone = Entry(abaDados, width=20, fg='dark gray')
inputAcolhidoTelefone.place(x=10, y=70)
inputAcolhidoTelefone.insert(0, "Número do Telefone")
inputAcolhidoTelefone.bind('<FocusIn>', lambda p:placeholder(inputAcolhidoTelefone))
inputAcolhidoTelefone.bind('<FocusOut>', lambda p:estavazio(inputAcolhidoTelefone, "Número do Telefone"))

inputAcolhidoCep = Entry(abaDados, width=10, fg='dark gray')
inputAcolhidoCep.place(x=140, y=70)
inputAcolhidoCep.insert(0, "CEP")
inputAcolhidoCep.bind('<FocusIn>', lambda p:placeholder(inputAcolhidoCep))
inputAcolhidoCep.bind('<FocusOut>', lambda p:estavazio(inputAcolhidoCep, "CEP"))

inputAcolhidoUf = Entry(abaDados, width=3, fg='dark gray')
inputAcolhidoUf.place(x=210, y=70)
inputAcolhidoUf.insert(0, "UF")
inputAcolhidoUf.bind('<FocusIn>', lambda p:placeholder(inputAcolhidoUf))
inputAcolhidoUf.bind('<FocusOut>', lambda p:estavazio(inputAcolhidoUf, "UF"))

inputAcolhidoMunicípio = Entry(abaDados, width=20, fg='dark gray')
inputAcolhidoMunicípio.place(x=238, y=70)
inputAcolhidoMunicípio.insert(0, "Município")
inputAcolhidoMunicípio.bind('<FocusIn>', lambda p:placeholder(inputAcolhidoMunicípio))
inputAcolhidoMunicípio.bind('<FocusOut>', lambda p:estavazio(inputAcolhidoMunicípio, "Município"))

inputAcolhidoBairro = Entry(abaDados, width=30, fg='dark gray')
inputAcolhidoBairro.place(x=368, y=70)
inputAcolhidoBairro.insert(0, "Bairro")
inputAcolhidoBairro.bind('<FocusIn>', lambda p:placeholder(inputAcolhidoBairro))
inputAcolhidoBairro.bind('<FocusOut>', lambda p:estavazio(inputAcolhidoBairro, "Bairro"))

inputAcolhidoEndereço = Entry(abaDados, width=45, fg='dark gray')
inputAcolhidoEndereço.place(x=558, y=70)
inputAcolhidoEndereço.insert(0, "Endereço")
inputAcolhidoEndereço.bind('<FocusIn>', lambda p:placeholder(inputAcolhidoEndereço))
inputAcolhidoEndereço.bind('<FocusOut>', lambda p:estavazio(inputAcolhidoEndereço, "Endereço"))

inputAcolhidoCredo = Entry(abaDados, width=20, fg='dark gray')
inputAcolhidoCredo.place(x=10, y=100)
inputAcolhidoCredo.insert(0, "Crença Religiosa")
inputAcolhidoCredo.bind('<FocusIn>', lambda p:placeholder(inputAcolhidoCredo))
inputAcolhidoCredo.bind('<FocusOut>', lambda p:estavazio(inputAcolhidoCredo, "Crença Religiosa"))

menuAcolhidoEstadoCivil = OptionMenu(abaDados, estadoCivil, *listaEstadoCivil)
menuAcolhidoEstadoCivil.place(x=140, y=100)

menuListaFilhos = OptionMenu(abaDados, simNao,*listaSimNao)
menuListaFilhos.place(x=250, y=100)

menuListaEscolaridade = OptionMenu(abaDados, escolaridade, *listaEscolaridade)
menuListaEscolaridade.place(x=340,y=100)

menuAcolhidoTipoDependencia = OptionMenu(abaDados, dependencias, *listaDependencias)
menuAcolhidoTipoDependencia.place(x=458, y=100)

##########__________________________________________________________________________________________Dados do responsável
labelDadosResponsavel = Label(abaDados, text="DADOS DO(A) RESPONSAVEL: ").place(x=100, y=150)

inputResponsavelNome = Entry(abaDados, width=74, fg='dark gray')
inputResponsavelNome.place(x=10, y=180)
inputResponsavelNome.insert(0, "Nome do(a) Responsável")
inputResponsavelNome.bind('<FocusIn>', lambda p:placeholder(inputResponsavelNome))
inputResponsavelNome.bind('<FocusOut>', lambda p:estavazio(inputResponsavelNome, "Nome do(a) Responsável"))

inputResponsávelParentesco = Entry(abaDados, width=22, fg='dark gray')
inputResponsávelParentesco.place(x=464, y=180)
inputResponsávelParentesco.insert(0, "Parentesco")
inputResponsávelParentesco.bind('<FocusIn>', lambda p:placeholder(inputResponsávelParentesco))
inputResponsávelParentesco.bind('<FocusOut>', lambda p:estavazio(inputResponsávelParentesco, "Parentesco"))

inputResponsávelCpf = Entry(abaDados, width=15, fg='dark gray')
inputResponsávelCpf.place(x=606, y=180)
inputResponsávelCpf.insert(0, "")
inputResponsávelCpf.bind('<FocusIn>', lambda p:placeholder(inputResponsávelCpf))
inputResponsávelCpf.bind('<FocusOut>', lambda p:estavazio(inputResponsávelCpf, "Número do CPF"))

inputResponsávelIdentidade = Entry(abaDados, width=20, fg='dark gray')
inputResponsávelIdentidade.place(x=706, y=180)
inputResponsávelIdentidade.insert(0, "Número do RG")
inputResponsávelIdentidade.bind('<FocusIn>', lambda p:placeholder(inputResponsávelIdentidade))
inputResponsávelIdentidade.bind('<FocusOut>', lambda p:estavazio(inputResponsávelIdentidade, "Número do RG"))

inputResponsávelTelefone = Entry(abaDados, width=20, fg='dark gray')
inputResponsávelTelefone.place(x=10, y=210)
inputResponsávelTelefone.insert(0, "Número do Telefone")
inputResponsávelTelefone.bind('<FocusIn>', lambda p:placeholder(inputResponsávelTelefone))
inputResponsávelTelefone.bind('<FocusOut>', lambda p:estavazio(inputResponsávelTelefone, "Número do Telefone"))

inputResponsávelCep = Entry(abaDados, width=10, fg='dark gray')
inputResponsávelCep.place(x=140, y=210)
inputResponsávelCep.insert(0, "CEP")
inputResponsávelCep.bind('<FocusIn>', lambda p:placeholder(inputResponsávelCep))
inputResponsávelCep.bind('<FocusOut>', lambda p:estavazio(inputResponsávelCep, "CEP"))

inputResponsávelUf = Entry(abaDados, width=3, fg='dark gray')
inputResponsávelUf.place(x=210, y=210)
inputResponsávelUf.insert(0, "UF")
inputResponsávelUf.bind('<FocusIn>', lambda p:placeholder(inputResponsávelUf))
inputResponsávelUf.bind('<FocusOut>', lambda p:estavazio(inputResponsávelUf, "UF"))

inputResponsávelMunicípio = Entry(abaDados, width=20, fg='dark gray')
inputResponsávelMunicípio.place(x=238, y=210)
inputResponsávelMunicípio.insert(0, "Município")
inputResponsávelMunicípio.bind('<FocusIn>', lambda p:placeholder(inputResponsávelMunicípio))
inputResponsávelMunicípio.bind('<FocusOut>', lambda p:estavazio(inputResponsávelMunicípio, "Município"))

inputResponsávelBairro = Entry(abaDados, width=30, fg='dark gray')
inputResponsávelBairro.place(x=368, y=210)
inputResponsávelBairro.insert(0, "Bairro")
inputResponsávelBairro.bind('<FocusIn>', lambda p:placeholder(inputResponsávelBairro))
inputResponsávelBairro.bind('<FocusOut>', lambda p:estavazio(inputResponsávelBairro, "Bairro"))

inputResponsávelEndereço = Entry(abaDados, width=45, fg='dark gray')
inputResponsávelEndereço.place(x=558, y=210)
inputResponsávelEndereço.insert(0, "Endereço")
inputResponsávelEndereço.bind('<FocusIn>', lambda p:placeholder(inputResponsávelEndereço))
inputResponsávelEndereço.bind('<FocusOut>', lambda p:estavazio(inputResponsávelEndereço, "Endereço"))


labelDataEntrada = Label(abaDados, text='Data de entrada:').place(x=10, y=280)
h = datetime.datetime.now()
inputDataEntrada = Entry(abaDados, width=10)
inputDataEntrada.place(x=105, y=280)
inputDataEntrada.insert(0, h.strftime("%d/%m/%Y"))

botaoRegistrarEntrada = Button(abaDados, text='Registrar entrada', command=gerarFichaCadastro).place(x= 175, y=280)
botaoInserirFichaAssinada = Button(abaDados, text='Inserir formulário assinado', command=cadastrarInterno)

##########__________________________________________________________________________________________Aba Entradas

def pesquisarEntradas():
    for n in tabelaEntradaMunicipio.get_children():
        tabelaEntradaMunicipio.delete(n)
        
    cidade = entryMunicipio.get()
    cursor.execute("SELECT nome, dataEntrada, dataSaida, motivoSaida FROM internos WHERE municipio = '"+cidade+"'")
    listaInternos = cursor.fetchall()
    for i in listaInternos:
        tabelaEntradaMunicipio.insert('','end',values=i)        
        

entryMunicipio = Entry(abaEntradas, width=30, fg='dark gray')
entryMunicipio.place(x=69, y=10)
entryMunicipio.insert(0, "Município")
entryMunicipio.bind('<FocusIn>', lambda p:placeholder(entryMunicipio))
entryMunicipio.bind('<FocusOut>', lambda p:estavazio(entryMunicipio, "Município"))
botaoMunicipio = Button(abaEntradas, text="Pesquisar", command=pesquisarEntradas).place(x=259, y=10)
tabelaEntradaMunicipio.column('1',width=345, stretch=NO)
tabelaEntradaMunicipio.column('2',width=100, stretch=NO)
tabelaEntradaMunicipio.column('3',width=100, stretch=NO)
tabelaEntradaMunicipio.column('4',width=350, stretch=NO)
tabelaEntradaMunicipio.heading('#1', text='Nome do(a) acolhido(a)')
tabelaEntradaMunicipio.heading('#2', text='Data da entrada')
tabelaEntradaMunicipio.heading('#3', text='Data da saída')
tabelaEntradaMunicipio.heading('#4', text='Motivo da saída')
tabelaEntradaMunicipio.place(x=10, y=40)
    
    
##########__________________________________________________________________________________________Aba Saídas
def listarSaidas():
    for n in tabelaSaidas.get_children():
        tabelaSaidas.delete(n)
        
    cidade = entryMunicipioSaida.get()
    cursor.execute("SELECT nome, dataEntrada, dataSaida, motivoSaida FROM internos WHERE municipio = '"+cidade+"'")
    listaInternos = cursor.fetchall()
    for i in listaInternos:
        tabelaSaidas.insert('','end',values=i)

entryMunicipioSaida = Entry(abaSaidas, width=30, fg='dark gray')
entryMunicipioSaida.place(x=69, y=10)
entryMunicipioSaida.insert(0, "Município")
entryMunicipioSaida.bind('<FocusIn>', lambda p:placeholder(entryMunicipioSaida))
entryMunicipioSaida.bind('<FocusOut>', lambda p:estavazio(entryMunicipioSaida, "Município"))

entryAcolhidoSaida = Entry(abaSaidas, width=30, fg='dark gray')
entryAcolhidoSaida.place(x=325, y=10)
entryAcolhidoSaida.insert(0, "Nome do(a) acolhido(a)")
entryAcolhidoSaida.bind('<FocusIn>', lambda p:placeholder(entryAcolhidoSaida))
entryAcolhidoSaida.bind('<FocusOut>', lambda p:estavazio(entryAcolhidoSaida, "Nome do(a) acolhido(a)"))

botaoPesquisarSaida = Button(abaSaidas, text='Pesquisar saída', command=listarSaidas).place(x= 515, y=10)

tabelaSaidas.column('1',width=345, stretch=NO)
tabelaSaidas.column('2',width=100, stretch=NO)
tabelaSaidas.column('3',width=100, stretch=NO)
tabelaSaidas.column('4',width=350, stretch=NO)
tabelaSaidas.heading('#1', text="Nome")
tabelaSaidas.heading('#2', text="Data da entrada")
tabelaSaidas.heading('#3', text="Data da saída")
tabelaSaidas.heading('#4', text="Motivo da saída")
tabelaSaidas.place(x=10,y=40)
##########__________________________________________________________________________________________Aba visitantes

def registrarVisita():
    try:
        nomeAcolhido = entryVisitanteAcolhido.get()
        nomeVisitante = entryVisitanteNome.get()
        parentescoVisitante = entryVisitanteParentesco.get()
        h = datetime.datetime.now()
        data = h.strftime("%d/%m/%Y") + " " + h.time().strftime("%H:%M:%S")    
        cursor.execute("CREATE TABLE IF NOT EXISTS visitas(nomeAcolhido text, nomeVisitante text, parentesco text, dataVisita text)")
        cursor.execute("INSERT INTO visitas VALUES('"+nomeAcolhido+"', '"+nomeVisitante+"', '"+parentescoVisitante+"', '"+data+"')")
        banco.commit()
        cursor.close()
        entryVisitanteAcolhido.delete(0,'end')
        entryVisitanteAcolhido.insert(0, "Nome do(a) Acolhido(a)")
        entryVisitanteAcolhido.config(fg='dark gray')
        entryVisitanteNome.delete(0, 'end')
        entryVisitanteNome.insert(0, 'Nome do(a) visitante')
        entryVisitanteNome.config(fg='dark gray')    
        entryVisitanteParentesco.delete(0, 'end')
        entryVisitanteParentesco.insert(0, 'Parentesco do(a) visitante')
        entryVisitanteParentesco.config(fg='dark gray')
        messagebox.showinfo(title='Sucesso', message="Visita cadastrada com sucesso")
    except Exception as erro:
        messagebox.showerror(title="Erro!", message=erro)

def pesquisarVisitas(e):
    for n in tabelaVisitas.get_children():
        tabelaVisitas.delete(n)
    try:
        nomeAcolhido = entryAcolhidoVisitantes.get()
        cursor.execute("SELECT * FROM visitas WHERE nomeAcolhido = '"+nomeAcolhido+"'")
        visitas = cursor.fetchall()
        if len(visitas) == 0:
            messagebox.showinfo(title="Atenção", message="Não existem visitas cadastradas para " + nomeAcolhido)
        else:
            for i in visitas:
                tabelaVisitas.insert('', 'end', values=i)
    except Exception as erro:
        messagebox.showerror(title="Erro!", message=erro) 

entryVisitanteAcolhido = Entry(abaVisitas, width=40, fg='dark gray')
entryVisitanteAcolhido.place(x=10, y=10)
entryVisitanteAcolhido.insert(0, "Nome do(a) acolhido(a)")
entryVisitanteAcolhido.bind('<FocusIn>', lambda p: placeholder(entryVisitanteAcolhido))
entryVisitanteAcolhido.bind('<FocusOut>', lambda p: estavazio(entryVisitanteAcolhido, "Nome do(a) acolhido(a)"))

entryVisitanteNome = Entry(abaVisitas, width=50, fg='dark gray')
entryVisitanteNome.place(x=260,y=10)
entryVisitanteNome.insert(0, "Nome do(a) visitante")
entryVisitanteNome.bind('<FocusIn>', lambda p: placeholder(entryVisitanteNome))
entryVisitanteNome.bind('<FocusOut>', lambda p: estavazio(entryVisitanteNome, "Nome do(a) visitante"))

entryVisitanteParentesco = Entry(abaVisitas, width=37, fg='dark gray')
entryVisitanteParentesco.place(x=570, y=10)
entryVisitanteParentesco.insert(0, "Parentesco do(a) visitante")
entryVisitanteParentesco.bind('<FocusIn>', lambda p: placeholder(entryVisitanteParentesco))
entryVisitanteParentesco.bind('<FocusOut>', lambda p: estavazio(entryVisitanteParentesco, "Parentesco do(a) visitante"))

botaoRegistrarVisita = Button(abaVisitas, text='Registrar Visita', width=13, command=registrarVisita)
botaoRegistrarVisita.place(x=805, y=10)

entryAcolhidoVisitantes = Entry(abaVisitas, width=130, fg='dark gray')
entryAcolhidoVisitantes.place(x=10, y=40)
entryAcolhidoVisitantes.insert(0, 'Digite o nome do(a) acolhido(a) para pesquisar as visitas e pressione ENTER')
entryAcolhidoVisitantes.bind('<FocusIn>', lambda p:placeholder(entryAcolhidoVisitantes))
entryAcolhidoVisitantes.bind('<FocusOut>', lambda p:estavazio(entryAcolhidoVisitantes, "Digite o nome do(a) acolhido(a) para pesquisar as visitas e pressione ENTER"))
entryAcolhidoVisitantes.bind('<KeyPress-Return>', pesquisarVisitas)

tabelaVisitas.column('1',width=400, stretch=NO)
tabelaVisitas.column('2',width=295, stretch=NO)
tabelaVisitas.column('3',width=200, stretch=NO)
tabelaVisitas.heading('#1', text="Nome")
tabelaVisitas.heading('#2', text="Parentesco")
tabelaVisitas.heading('#3', text="Data da visita")
tabelaVisitas.place(x=10, y=70)
listaInternos = ''

##########__________________________________________________________________________________________aba PIA

def inserirMedicamento():
    cpf = inputInterno.get()    
    nome = nomeEntry.get()
    medicamento = inputInserirMedicamentos.get()
    medico = inputMedico.get()    
    receitaCaminho = filedialog.askopenfilename(title='Selecione o receituário', filetypes = (("Arquivos pdf", "*.pdf"),('','')))
    cursor.execute("CREATE TABLE IF NOT EXISTS medicamento (cpf text, nome text, medicamento text, medico text, receita BLOB)")
    pdf_path = pathlib.Path(receitaCaminho)
    pdf_data = pdf_path.read_bytes()
    banco.execute("INSERT INTO medicamento (cpf, nome, medicamento, medico, receita) VALUES (?, ?, ?, ?, ?)", (cpf, nome, medicamento, medico, pdf_data))
    banco.commit() 
    cursor.execute("SELECT medicamento, medico, receita FROM medicamento WHERE cpf='"+cpf+"'")
    l = cursor.fetchall()
    for n in tabela.get_children():
        tabela.delete(n)
    for i in l:
        tabela.insert("", END, values=i)
    inputInserirMedicamentos.delete(0,'end')
    cursor.close()

def recuperarPdf():
    cursor.execute("SELECT * FROM pdfs")
    l = cursor.fetchall()
    b64 = l[0][2]
    base64EncodedStr = base64.b64encode(b64)
    bytes = b64decode(base64EncodedStr, validate=True)
    if bytes[0:4] != b'%PDF':
        raise ValueError('Missing the PDF file signature')
    f = open('file.pdf', 'wb')
    f.write(bytes)
    f.close()
    subprocess.Popen(['file.pdf'], shell=True)

def pesquisarInterno(e):
    cpf = inputInterno.get()
    cursor.execute("SELECT nome FROM internos WHERE cpf = '"+cpf+"'")
    listaInternos = cursor.fetchone()
    for i in listaInternos:
        if i != '':
            nomeEntry.insert(0, listaInternos)
            inputInternoPesquisadoNome.config(text=listaInternos)
            inputInserirMedicamentos.config(state='normal', fg='dark gray')
            inputInserirMedicamentos.insert(0, "Insira o nome, dosagem e posologia do medicamento")
            botaoInserirMedicamentos.place(x=782, y=100)
            inputMedico.config(state='normal', fg='dark gray')
            inputMedico.insert(0, 'Nome e CRM do(a) médico(a)')
            botaoRegistro.place(x=810,y=370)
            botaoMotivoSaida.place(x=655, y=630)
            botaoGerarPdf.place(x=830,y=630)
            botaoInserirPdf.place(x=819, y=40)
            inputRegistro.config(state='normal')
            inputRegistro.insert(0, "Digite o que aconteceu para registro")
            inputDataSaida.config(state='normal', fg='dark gray')
            inputDataSaida.insert(0, 'Data de saída')
            inputMotivoSaida.config(state='normal', fg='dark gray')
            inputMotivoSaida.insert(0, 'Digite o motivo da saída')
            try: 
                cursor.execute("SELECT medicamento, medico, receita FROM medicamento WHERE cpf='"+cpf+"'")
                l = cursor.fetchall()
                b64 = l[0][2]
                base64EncodedStr = base64.b64encode(b64)
                bytes = b64decode(base64EncodedStr, validate=True)
                if bytes[0:4] != b'%PDF':
                    raise ValueError('Missing the PDF file signature')
                f = open('file.pdf', 'wb')
                f.write(bytes)
                f.close()                
                for i in l:
                    tabela.insert('', END, values=(i[0], i[1]), tags='botaoReceita')                    
                                       
            except:
                tabela.insert("", END, values="SEM REGISTROS")
            try:
                cursor.execute("SELECT dataRegistro, registro, registradoPor FROM registro WHERE cpf='"+cpf+"'")
                l = cursor.fetchall()
                for i in l:
                    tabelaRegistros.insert("", END, values=i)
            except:
                tabelaRegistros.insert("", END, values="SEM REGISTROS")
    
def registrarSaida():
    cpf = inputInterno.get()
    dataSaida = inputDataSaida.get()
    motivoSaida = inputMotivoSaida.get()
    cursor.execute("UPDATE internos SET dataSaida = '"+dataSaida+"', motivoSaida = '"+motivoSaida+"' WHERE cpf = '"+cpf+"'")
    banco.commit()

def inserirRegistros():
    for n in tabelaRegistros.get_children():
        tabelaRegistros.delete(n)
    cpf = inputInterno.get()
    nome = listaInternos
    registro = inputRegistro.get()
    h = datetime.datetime.now()
    hoje = h.strftime("%d/%m/%Y") + " " + h.time().strftime("%H:%M:%S")    
    registrador = "John"
    
    cursor.execute("CREATE TABLE IF NOT EXISTS registro(cpf text, nome text, registro text, dataRegistro text, registradoPor text)")
    cursor.execute("INSERT INTO registro VALUES('"+cpf+"', '"+nome+"','"+registro+"', '"+hoje+"', '"+registrador+"')")
    banco.commit()
    cursor.execute("SELECT dataRegistro, registro, registradoPor FROM registro WHERE cpf='"+cpf+"'")
    l = cursor.fetchall()
    for i in l:
        tabelaRegistros.insert("", END, values=i)
        
    inputRegistro.delete(0,'end')

inputInterno = Entry(abaPIA, width=30, fg='dark gray')
inputInterno.place(x=50, y=10)
inputInterno.insert(0, "CPF")
inputInterno.bind('<FocusIn>', lambda p:placeholder(inputInterno))
inputInterno.bind('<FocusOut>', lambda p:estavazio(inputInterno, "CPF"))
inputInterno.bind('<KeyPress-Return>', pesquisarInterno)

nm = tk.StringVar()
cpfStringVar = tk.StringVar()
inputInternoPesquisadoNome = Label(abaPIA, text="")
nomeEntry = Entry(abaPIA, width=0)
inputInternoPesquisadoNome.place(x=240,y=10)

botaoInserirPdf = Button(abaPIA,text='Inserir PDF')

labelMedicamentos = Label(abaPIA, text="MEDICAMENTOS")
labelMedicamentos.place(x=100, y=70)
inputInserirMedicamentos = Entry(abaPIA, width=50, state='disabled', fg='dark gray')
inputInserirMedicamentos.place(x=146, y=100)
inputInserirMedicamentos.insert(0, "Insira o nome, dosagem e posologia do medicamento")
inputInserirMedicamentos.bind('<FocusIn>', lambda p:placeholder(inputInserirMedicamentos))
inputInserirMedicamentos.bind('<FocusOut>', lambda p:estavazio(inputInserirMedicamentos, "Insira o nome, dosagem e posologia do medicamento"))

inputMedico = Entry(abaPIA, width=50, fg="dark gray", state='disabled')
inputMedico.place(x=460, y=100)
inputMedico.insert(0, "Nome e CRM do(a) médico(a)")
inputMedico.bind('<FocusIn>', lambda p:placeholder(inputMedico))
inputMedico.bind('<FocusOut>', lambda p:estavazio(inputMedico, "Nome e CRM do(a) médico(a)"))
botaoInserirMedicamentos = Button(abaPIA, text="Inserir medicamento", command = inserirMedicamento)

tabela.column('Coluna 1', width=400, stretch=NO)
tabela.heading('#1', text="Medicamento")
tabela.column('2', width=400)
tabela.heading('#2', text='Médico e CRM')
tabela.column('3', width=95)
tabela.heading('#3', text="Receita")
tabela.place(x=10, y=130)

inputRegistro = Entry(abaPIA, width=100, state='disabled', fg='dark gray')
inputRegistro.place(x=117,y=370)
inputRegistro.insert(0, "Inserir registro:")
inputRegistro.bind('<FocusIn>', lambda p:placeholder(inputRegistro))
inputRegistro.bind('<FocusOut>', lambda p:estavazio(inputRegistro, "Inserir registro:"))
botaoRegistro = Button(abaPIA, text='Inserir registro', command=inserirRegistros)

tabelaRegistros.column('1', width=100, stretch=NO)
tabelaRegistros.column('2', width=540, stretch=NO)
tabelaRegistros.column('3', width=255, stretch=NO)
tabelaRegistros.heading('#1', text='Data')
tabelaRegistros.heading('#2', text='Ocorrência')
tabelaRegistros.heading('#3', text='Registrado por')
tabelaRegistros.place(x=10, y=400)

inputDataSaida = Entry(abaPIA, width=10, state='disabled', fg='dark gray')
inputDataSaida.place(x=90, y=630)
inputDataSaida.insert(0, "Data de saída")
inputDataSaida.bind('<FocusIn>', lambda p:placeholder(inputDataSaida))
inputDataSaida.bind('<FocusOut>', lambda p:estavazio(inputDataSaida, "Data de saída"))

inputMotivoSaida = Entry(abaPIA, width=65, state='disabled', fg='dark gray')
inputMotivoSaida.place(x=255, y=630)
inputMotivoSaida.insert(0, "Motivo da saída")
inputMotivoSaida.bind('<FocusIn>', lambda p:placeholder(inputMotivoSaida))
inputMotivoSaida.bind('<FocusOut>', lambda p:estavazio(inputMotivoSaida, "Motivo da saída"))
botaoMotivoSaida = Button(abaPIA, text='Registrar saída', command=registrarSaida)

botaoGerarPdf = Button(abaPIA, text="Gerar PDF", command=gerarRelatorioAcolhimento)


##########__________________________________________________________________________________________aba Internos
def listarInternos(e):    
    cursor.execute("SELECT nome, cpf FROM internos")
    listaInternos = cursor.fetchall()
    for i in listaInternos:
       tabelaInternos.insert('','end',values=i)  

def limparListaInternos(e):
    for n in tabelaInternos.get_children():
        tabelaInternos.delete(n)
    
abaInternos.bind('<FocusIn>', listarInternos)
abaInternos.bind('<FocusOut>', limparListaInternos)

tabelaInternos.column('1',width=400, stretch=NO)
tabelaInternos.column('2',width=195, stretch=NO)
tabelaInternos.column('3',width=300, stretch=NO)
tabelaInternos.heading('#1', text='Nome do(a) acolhido(a)')
tabelaInternos.heading('#2', text='CPF')
tabelaInternos.heading('#3', text='Foto')
tabelaInternos.place(x=10, y=10)

Application()