from tkinter import *
from tkinter import ttk, filedialog, messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from PyPDF2 import PdfMerger
import datetime, subprocess, sqlite3, pathlib, base64, cryptocode
from base64 import b64decode
janelaLogin = Tk()

class funcoes():
    global chaveCriptografia, nomeUsuarioLogado, perfilUsuarioLogado
    global responsavelNome, responsavelParentesco, responsavelCpf, responsavelIdentidade, responsavelTelefone, responsavelCep, responsavelUf, responsavelMunicipio, responsavelBairro, responsavelEndereco
    global internoUf, internoTelefone, internoNome, internoNascimento, internoBairro, internoIdentidade, internoCep, internoCpf, internoCredo, internoEndereco, internoEntrada, internoescolaridade
    global internoestadoCivil, internofilhos, internoTipoDependencia, internoMunicipio, nomeAcolhido, cpfAcolhido, listaPdf
                    
    chaveCriptografia = '&t&*_*_+)%&!*$+(@g*#)E$^A#+_$(#!$^%T_$!!+*!*&^!*)@@##&((_**)^$#@&#$V@(!e%#$%!)@_%!@_)*@!)^+#!@$+W#&+#%$%_d%)&@!^$^&)(*+!$)$%q*(#&))%^&#+$+@(!_)%%***%#E%**&^$@+))_%&&$)%+*)!@^)^$_c^%e^+@*%&+(@#*$*)&@+_($+$!#(G^)!$*&@_@)*)&@m@@&^*#!)_H+*&^)*()@(!)_(#_^$!(!(&&*%_)@E+)&^%!_#*@#&_^@&)!)+$%*@h@()+^!++(_^$%*#%!#)+@@)%$$_+&_@@@!()#^((#!+!$&))&%(!+&@)*))_^+^#+$)_(*(_+#%)^!_)_*%*)@)+_)&+%K$@#!!@__+$*(+_($(&$$)^+%^*)!!&$!&_+_^J)!@)#^()$)_#^!$%^^()^#$_$L$%^(_**)$@(@J!_+!&)$@@)#%*!%@^!+$*($)_$*++)_@#!&___!_#($^@))*$&@(&k(^!$+#*#__!l+_)M$!!)+^_#'
    
    def dataAtual(arg):
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
    
    def conectaBancoDados(self):
        self.banco = sqlite3.connect('ctelchadai.db')
        self.cursor = self.banco.cursor()
    
    def fecharConexao(self):
        self.banco.close()

    def validarPreenchimentoCampos(self):
        mensagemDeErro = ''
        if self.inputAcolhidoNome.get() == 'Nome do(a) acolhido(a)': self.internoNome = ""
        else: self.internoNome = self.inputAcolhidoNome.get()
        if self.inputAcolhidoBairro.get() == "Bairro" : self.internoBairro = ""
        else: self.internoBairro = self.inputAcolhidoBairro.get()
        if self.inputAcolhidoCep.get() == "CEP" : self.internoCep = ""
        else: self.internoCep = self.inputAcolhidoCep.get()
        if self.inputAcolhidoCpf.get() == "Número do CPF": self.internoCpf = ""
        else: self.internoCpf = self.inputAcolhidoCpf.get()
        if self.inputAcolhidoCredo.get() == "Crença Religiosa": self.internoCredo = ""
        else: self.internoCredo = self.inputAcolhidoCredo.get()
        if self.inputAcolhidoDataNascimento.get() == "Nascimento: 00/00/0000": self.internoNascimento = ""
        else: self.internoNascimento = self.inputAcolhidoDataNascimento.get()
        if self.inputAcolhidoEndereço.get() == "Endereço": self.internoEndereco = ""
        else: self.internoEndereco = self.inputAcolhidoEndereço.get()
        if self.inputAcolhidoIdentidade.get() == "Número do RG": self.internoIdentidade = ""
        else: self.internoIdentidade = self.inputAcolhidoIdentidade.get()
        if self.inputAcolhidoMunicípio.get() == "Município": self.internoMunicipio = ""
        else: self.internoMunicipio = self.inputAcolhidoMunicípio.get()
        if self.inputAcolhidoTelefone.get() == "Número do Telefone": self.internoTelefone = ""
        else: self.internoTelefone = self.inputAcolhidoTelefone.get()
        if self.inputAcolhidoUf.get() == "UF": self.internoUf = ""
        else: self.internoUf = self.inputAcolhidoUf.get()
        self.internoEntrada = self.inputDataEntrada.get()
        if self.simNao.get() != "Filhos": self.internofilhos = self.simNao.get()
        else: mensagemDeErro += "Selecione se tem filhos\n"
        if self.escolaridade.get() != "Escolaridade": self.internoescolaridade = self.escolaridade.get()
        else: mensagemDeErro += "Selecione a escolaridade\n"
        if self.tipoAcolhimento.get() == "Tipo de Acolhimento" : mensagemDeErro += "Selecione o tipo de acolhimento\n"
        if self.dependencias.get() != "Tipo de dependência": self.internoTipoDependencia = self.dependencias.get()
        else: mensagemDeErro += "Selecione o tipo de dependência\n"
        if self.estadoCivil.get() != "Estado Civil": self.internoestadoCivil = self.estadoCivil.get()
        else: mensagemDeErro += "Selecione o estado civil\n"
        if self.inputResponsavelNome.get() == "Nome do(a) Responsável" : self.responsavelNome = ""
        else: self.responsavelNome = self.inputResponsavelNome.get()
        if self.inputResponsávelParentesco.get() == "Parentesco": self.responsavelParentesco = ""
        else: self.responsavelParentesco = self.inputResponsávelParentesco.get()
        if self.inputResponsávelTelefone.get() == "Número do Telefone": self.responsavelTelefone = ""
        else: self.responsavelTelefone = self.inputResponsávelTelefone.get()
        if self.inputResponsávelIdentidade.get() == "Número do RG": self.responsavelIdentidade = ""
        else: self.responsavelIdentidade = self.inputResponsávelIdentidade.get()
        if self.inputResponsávelCpf.get() == "Número do CPF": self.responsavelCpf = ""
        else: self.responsavelCpf = self.inputResponsávelCpf.get()
        if self.inputResponsávelCep.get() == "CEP": self.responsavelCep = ""
        else: self.responsavelCep = self.inputResponsávelCep.get()
        if self.inputResponsávelUf.get() == "UF": self.responsavelUf = ""
        else: self.responsavelUf = self.inputResponsávelUf.get()
        if self.inputResponsávelMunicípio.get() == "Município": self.responsavelMunicipio = ""
        else: self.responsavelMunicipio = self.inputResponsávelMunicípio.get()
        if self.inputResponsávelEndereço.get() == "Endereço": self.responsavelEndereco = ""
        else: self.responsavelEndereco = self.inputResponsávelEndereço.get()
        if self.inputResponsávelBairro.get() == "Bairro": self.responsavelBairro = ""
        else: self.responsavelBairro = self.inputResponsávelBairro.get()
        if mensagemDeErro != '': messagebox.showerror(title='Falta informações', message= mensagemDeErro)
        else: self.gerarFichaCadastro()

    def gerarFichaCadastro(self):
        cnv = canvas.Canvas("Inscrição.pdf")
        cnv.rotate(55)
        cnv.setFontSize(150)
        cnv.setFillColorRGB(0.9, 0.9, 0.9)
        cnv.drawString(200,-55,'SIGILOSO')
        cnv.rotate(-55)
        cnv.setFontSize(12)
        cnv.setFillColorRGB(0,0,0)
        cnv.setFillColorRGB(0,0,0)
        cnv.setFontSize(12)
        cnv.setTitle("Relatório")        
        cnv.drawString(text='Termo de Adesão', x=70,y=750)
        cnv.drawString(text='I. Identificação da Entidade', x=50,y=730)
        cnv.drawString(text='Nome: Centro de Reabilitação Desafio do Jovem', x=50,y=710)
        cnv.drawString(text='CNPJ: 10.770.476/0001-65', x=50,y=695)
        cnv.drawString(text='II. Dados da pessoa acolhida', x=50,y=675)
        cnv.drawString(text='Nome de Registro:', x=50,y=655)
        cnv.drawString(text= self.internoNome, x=162, y=655)
        cnv.drawString(text='Data de Nascimento:', x=50, y=640)
        cnv.drawString(text= self.internoNascimento, x=174, y=640)
        cnv.drawString(text='Identidade:', x=50, y=625)
        cnv.drawString(text= self.internoIdentidade, x=126, y=625)
        cnv.drawString(text='CPF:', x=400, y=625)
        cnv.drawString(text= self.internoCpf, x=429, y=625)
        cnv.drawString(text='Endereço:', x=50, y=610)
        cnv.drawString(text= self.internoEndereco, x=109, y=610)
        cnv.drawString(text='Bairro:', x=400, y=610)
        cnv.drawString(text= self.internoBairro, x=447, y=610)
        cnv.drawString(text='Município:', x=50, y=595)
        cnv.drawString(text= self.internoMunicipio, x=115, y=595)
        cnv.drawString(text='UF:', x=400, y=595)
        cnv.drawString(text= self.internoUf, x=423, y=595)
        cnv.drawString(text='Telefone:', x=50, y=580)
        cnv.drawString(text= self.internoTelefone, x=109, y=580)
        cnv.drawString(text='Cep:', x=400, y=580)
        cnv.drawString(text= self.internoCep, x=429, y=580)
        cnv.drawString(text='III. Dados do responsável legal (se for o caso)', x=50,y=560)
        cnv.drawString(text='Nome:', x=50,y=540)
        cnv.drawString(text= self.responsavelNome, x=135, y=540)
        cnv.drawString(text='Identidade:', x=50, y=525)
        cnv.drawString(text= self.responsavelIdentidade, x=121, y=525)
        cnv.drawString(text='CPF:', x=400, y=525)
        cnv.drawString(text= self.responsavelCpf, x=429, y=525)
        cnv.drawString(text='Endereço:', x=50, y=510)
        cnv.drawString(text= self.responsavelEndereco, x=109, y=510)
        cnv.drawString(text='Bairro:', x=400, y=510)
        cnv.drawString(text= self.responsavelBairro, x=447, y=510)
        cnv.drawString(text='Município:', x=50, y=495)
        cnv.drawString(text= self.responsavelMunicipio, x=115, y=495)
        cnv.drawString(text='UF:', x=400, y=495)
        cnv.drawString(text= self.responsavelUf, x=420, y=495)
        cnv.drawString(text='Telefone:', x=50, y=480)
        cnv.drawString(text= self.responsavelTelefone, x=109, y=480)
        cnv.drawString(text='Grau de parentesco:', x=50, y=465)
        cnv.drawString(text= self.responsavelParentesco, x=169, y=465)
        cnv.drawString(text='IV. Declaração da pessoa acolhida e/ou responsável', x=50, y=435)

        estiloParagrafo = ParagraphStyle('f',firstLineIndent=50, alignment=4, fontSize=12)
        textoDeclaracao = ''
        if self.tipoAcolhimento.get() == "Social":
            textoDeclaracao = 'Declaro que tomei conhecimento das normas da entidade especificada, com as quais concordo, e que tomei conhecimento do caráter gratuito e voluntário do acolhimento.'
        else:
            textoDeclaracao = 'Declaro que tomei conhecimento das normas da entidade especificada, com as quais concordo, e que tomei conhecimento do caráter voluntário do acolhimento.'
        declaracao = Paragraph(text=textoDeclaracao, style=estiloParagrafo)

        declaracao.wrapOn(cnv, 515, 30)
        declaracao.drawOn(cnv, 50, 400)

        cnv.drawAlignedString(565, 370, 'Marau, ' + self.dataAtual(), direction='LTR')
        cnv.line(150, 320, 450, 320)
        cnv.drawCentredString(300, 305, 'Assinatura da pessoa acolhida e/ou responsável')

        cnv.save()
        subprocess.Popen(['Inscrição.pdf'], shell=True) 
#Também cria o cadastro do usuário
    def inserirFichaAssinada(self):
        fichaInscricao = filedialog.askopenfilename(title='Selecione o receituário', filetypes = (("Arquivos pdf", "*.pdf"),('','')))
        pdf_path = pathlib.Path(fichaInscricao)
        pdf_data = pdf_path.read_bytes()                
        try:            
            self.conectaBancoDados()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS internos(cpf text, nome text, dataNascimento text, identidade text, cep text, uf text, municipio text, bairro text, endereco text, telefone text, filhos text, religiao text, dependencia text, escolaridade text, dataEntrada text, dataSaida text, motivoSaida text, estadoCivil text, responsavelNome text, responsavelParentesco text, responsavelTelefone text, responsavelIdentidade text, responsavelCpf text, responsavelCep text, responsavelUf text, responsavelMunicipio text, responsavelBairro text, responsavelEndereco text, fichaInscricao BLOB)")
            self.banco.execute("INSERT INTO internos VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (cryptocode.encrypt(self.internoCpf, chaveCriptografia), cryptocode.encrypt(self.internoNome, chaveCriptografia), cryptocode.encrypt(self.internoNascimento, chaveCriptografia),cryptocode.encrypt(self.internoIdentidade, chaveCriptografia),cryptocode.encrypt(self.internoCep, chaveCriptografia),cryptocode.encrypt(self.internoUf, chaveCriptografia),cryptocode.encrypt(self.internoMunicipio, chaveCriptografia),cryptocode.encrypt(self.internoBairro, chaveCriptografia),cryptocode.encrypt(self.internoEndereco, chaveCriptografia),cryptocode.encrypt(self.internoTelefone, chaveCriptografia),cryptocode.encrypt(self.internofilhos, chaveCriptografia),cryptocode.encrypt(self.internoCredo, chaveCriptografia),cryptocode.encrypt(self.internoTipoDependencia, chaveCriptografia),cryptocode.encrypt(self.internoescolaridade, chaveCriptografia),cryptocode.encrypt(self.internoEntrada, chaveCriptografia),'','',cryptocode.encrypt(self.internoestadoCivil, chaveCriptografia),cryptocode.encrypt(self.responsavelNome, chaveCriptografia),cryptocode.encrypt(self.responsavelParentesco, chaveCriptografia),cryptocode.encrypt(self.responsavelTelefone, chaveCriptografia),cryptocode.encrypt(self.responsavelIdentidade, chaveCriptografia),cryptocode.encrypt(self.responsavelCpf, chaveCriptografia),cryptocode.encrypt(self.responsavelCep, chaveCriptografia),cryptocode.encrypt(self.responsavelUf, chaveCriptografia),cryptocode.encrypt(self.responsavelMunicipio, chaveCriptografia),cryptocode.encrypt(self.responsavelBairro, chaveCriptografia),cryptocode.encrypt(self.responsavelEndereco, chaveCriptografia), pdf_data))
            self.banco.commit()
            self.fecharConexao()        
            self.limparCampos()
            messagebox.showinfo(title="Salvo", message="Cadastro realizado com sucesso")
        except Exception as erro:
            messagebox.showerror("Erro ao cadastrar", "Erro: '" + str(erro) + "' detectado. Tente novamente.")
        finally:
            self.fecharConexao()            
            
    def limparCampos(self):
        self.inputAcolhidoNome.delete(0, 'end')
        self.inputAcolhidoNome.config(fg='dark gray')
        self.inputAcolhidoNome.insert(0, "Nome do(a) acolhido(a)")
        self.inputAcolhidoDataNascimento.delete(0, 'end')
        self.inputAcolhidoDataNascimento.config(fg='dark gray')
        self.inputAcolhidoDataNascimento.insert(0, "Nascimento: 00/00/0000")
        self.inputAcolhidoCpf.config(fg='dark gray')
        self.inputAcolhidoCpf.delete(0, 'end')
        self.inputAcolhidoCpf.insert(0, "Número do CPF")
        self.inputAcolhidoIdentidade.delete(0, 'end')
        self.inputAcolhidoIdentidade.config(fg='dark gray')
        self.inputAcolhidoIdentidade.insert(0, "Número do RG")
        self.inputAcolhidoTelefone.delete(0, 'end')
        self.inputAcolhidoTelefone.config(fg='dark gray')
        self.inputAcolhidoTelefone.insert(0, "Número do Telefone")
        self.inputAcolhidoCep.delete(0, 'end')
        self.inputAcolhidoCep.config(fg='dark gray')
        self.inputAcolhidoCep.insert(0, "CEP")
        self.inputAcolhidoUf.delete(0, 'end')
        self.inputAcolhidoUf.config(fg='dark gray')
        self.inputAcolhidoUf.insert(0, "UF")
        self.inputAcolhidoMunicípio.delete(0, 'end')
        self.inputAcolhidoMunicípio.config(fg='dark gray')
        self.inputAcolhidoMunicípio.insert(0, "Município")
        self.inputAcolhidoBairro.delete(0, 'end')
        self.inputAcolhidoBairro.config(fg='dark gray')
        self.inputAcolhidoBairro.insert(0, "Bairro")
        self.inputAcolhidoEndereço.delete(0, 'end')
        self.inputAcolhidoEndereço.config(fg='dark gray')
        self.inputAcolhidoEndereço.insert(0, "Endereço")
        self.inputAcolhidoCredo.delete(0, 'end')
        self.inputAcolhidoCredo.config(fg='dark gray')
        self.inputAcolhidoCredo.insert(0, "Crença Religiosa")
        self.inputResponsavelNome.delete(0, 'end')
        self.inputResponsavelNome.config(fg='dark gray')
        self.inputResponsavelNome.insert(0, "Nome do(a) Responsável")
        self.inputResponsávelParentesco.delete(0, 'end')
        self.inputResponsávelParentesco.config(fg='dark gray')
        self.inputResponsávelParentesco.insert(0, "Parentesco")
        self.inputResponsávelCpf.delete(0, 'end')
        self.inputResponsávelCpf.config(fg='dark gray')
        self.inputResponsávelCpf.insert(0, "Número do CPF")
        self.inputResponsávelIdentidade.delete(0, 'end')
        self.inputResponsávelIdentidade.config(fg='dark gray')
        self.inputResponsávelIdentidade.insert(0, "Número do RG")
        self.inputResponsávelTelefone.delete(0, 'end')
        self.inputResponsávelTelefone.config(fg='dark gray')
        self.inputResponsávelTelefone.insert(0, "Número do Telefone")
        self.inputResponsávelCep.delete(0, 'end')
        self.inputResponsávelCep.config(fg='dark gray')
        self.inputResponsávelCep.insert(0, "CEP")
        self.inputResponsávelUf.delete(0, 'end')
        self.inputResponsávelUf.config(fg='dark gray')
        self.inputResponsávelUf.insert(0, "UF")
        self.inputResponsávelMunicípio.delete(0, 'end')
        self.inputResponsávelMunicípio.config(fg='dark gray')
        self.inputResponsávelMunicípio.insert(0, "Município")
        self.inputResponsávelBairro.delete(0, 'end')
        self.inputResponsávelBairro.config(fg='dark gray')
        self.inputResponsávelBairro.insert(0, "Bairro")
        self.inputResponsávelEndereço.delete(0, 'end')
        self.inputResponsávelEndereço.config(fg='dark gray')
        self.inputResponsávelEndereço.insert(0, "Endereço")

    def logar(self, entUsuario, entSenha):
        self.conectaBancoDados()
        usuario = entUsuario.get()
        senha = entSenha.get()        
        if usuario == '' or senha == '':
            messagebox.showerror(title="Erro!", message="Usuário e/ou senha não podem ficar em branco")
        else:
            self.cursor.execute("SELECT * FROM usuarios WHERE nome = '"+usuario+"'")
            user = self.cursor.fetchall()
            if senha == cryptocode.decrypt(user[0][1], chaveCriptografia):
                global nomeUsuarioLogado
                nomeUsuarioLogado = user[0][0]
                perfilUsuarioLogado = user[0][2]
                if perfilUsuarioLogado == 0:
                    self.botaoTelaPrincipal.place(x=30, y=150)
                    self.botaoCadastrarUsuario.place(x=170, y=150)
                else:
                    self.telaPrincipal()
            if len(user) == 0:
                messagebox.showerror(title="Erro!", message="Usuário e/ou senha incorreta")                
        self.fecharConexao()
        
    def registrarVisita(self):
        h = datetime.datetime.now()        
        cpf = self.entryVisitanteAcolhido.get()
        visitante = self.entryVisitanteNome.get()
        parentesco = self.entryVisitanteParentesco.get()
        dataVisita = h.strftime("%d/%m/%Y")
        try:
            self.conectaBancoDados()
            self.cursor.execute("SELECT nome, cpf FROM internos")
            for i in self.cursor.fetchall():
                if cryptocode.decrypt(i[1], chaveCriptografia) == cpf:
                    visitado = cryptocode.decrypt(i[0], chaveCriptografia)                    
            self.cursor.execute("CREATE TABLE IF NOT EXISTS visitas(cpf TEXT, visitado TEXT, visitante TEXT, parentesco TEXT, dataVisita TEXT)")
            self.cursor.execute("INSERT INTO visitas VALUES(?,?,?,?,?)",  (cryptocode.encrypt(cpf, chaveCriptografia), cryptocode.encrypt(visitado, chaveCriptografia), cryptocode.encrypt(visitante, chaveCriptografia), cryptocode.encrypt(parentesco, chaveCriptografia), cryptocode.encrypt(dataVisita, chaveCriptografia)))
            self.banco.commit()
            messagebox.showinfo(title="Sucesso", message="Visita de " + visitante + " para " + visitado + " registrada com sucesso.")
            self.entryVisitanteAcolhido.delete(0, 'end')
            self.entryVisitanteAcolhido.config(fg='dark gray')
            self.entryVisitanteAcolhido.insert(0, "CPF do(a) acolhido(a)")
            self.entryVisitanteNome.delete(0, 'end')
            self.entryVisitanteNome.config(fg='dark gray')
            self.entryVisitanteNome.insert(0, "Nome do(a) visitante")
            self.entryVisitanteParentesco.delete(0, 'end')
            self.entryVisitanteParentesco.config(fg='dark gray')
            self.entryVisitanteParentesco.insert(0, "Parentesco do(a) visitante")
        except Exception as erro:
            messagebox.showerror(title="Erro ao registrar visita", message="Erro: " + str(erro) + ".\nTente novamente")
        finally:
            self.fecharConexao()

    def pesquisarVisitas(self):
        for n in self.tabelaVisitas.get_children():
            self.tabelaVisitas.delete(n)
        nomeAcolhido = self.entryAcolhidoVisitantes.get()
        try:
            self.conectaBancoDados()
            self.cursor.execute("SELECT cpf, visitado, visitante, parentesco, dataVisita FROM visitas")
            numeroVisitas = 0
            for i in self.cursor.fetchall():
                if nomeAcolhido == cryptocode.decrypt(i[1], chaveCriptografia):
                    numeroVisitas += 1
                    visitante = cryptocode.decrypt(i[2], chaveCriptografia)
                    parentesco = cryptocode.decrypt(i[3], chaveCriptografia)
                    data = cryptocode.decrypt(i[4], chaveCriptografia)
                    self.tabelaVisitas.insert('', 'end', values=(visitante, parentesco, data))
            if numeroVisitas == 0:
                    messagebox.showinfo(title="Atenção", message="Não existem visitas cadastradas para " + nomeAcolhido)                                                    
        except Exception as erro:
            messagebox.showerror(title="Erro ao pesquisar visitas", message="Erro: " + str(erro) + ".\nTente novamente")
        finally:
            self.fecharConexao()

    def inserirMedicamento(self):
        cpf = self.inputInterno.get()    
        medicamento = cryptocode.encrypt(self.inputInserirMedicamentos.get(), chaveCriptografia)
        medico = cryptocode.encrypt(self.inputMedico.get(), chaveCriptografia)  
        for n in self.tabela.get_children():
            self.tabela.delete(n)
        try:
            self.conectaBancoDados()
            receitaCaminho = filedialog.askopenfilename(title='Selecione o receituário', filetypes = (("Arquivos pdf", "*.pdf"),('','')))
            pdf_path = pathlib.Path(receitaCaminho)
            pdf_data = pdf_path.read_bytes()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS medicamento (id INTEGER PRIMARY KEY, cpf text, nome text, medicamento text, medico text, receita BLOB)")
            self.cursor.execute("INSERT INTO medicamento (cpf, nome, medicamento, medico, receita) VALUES (?, ?, ?, ?, ?)", (cryptocode.encrypt(cpf, chaveCriptografia), cryptocode.encrypt(internoNome, chaveCriptografia), medicamento, medico, pdf_data))
            self.banco.commit()
            self.cursor.execute("SELECT id, cpf, medicamento, medico, receita FROM medicamento")
            for i in self.cursor.fetchall():
                if cpf == cryptocode.decrypt(i[0], chaveCriptografia):
                    id = i[0]
                    medicamentoRetornado = cryptocode.decrypt(i[1], chaveCriptografia)
                    medicoRetornado = cryptocode.decrypt(i[2], chaveCriptografia)
                    self.tabela.insert("", END, values=(id, medicamentoRetornado, medicoRetornado))
            self.inputInserirMedicamentos.delete(0,'end')
        except Exception as erro:
            messagebox.showerror(title="Erro ao inserir medicamento", message="Erro: " + str(erro) + ".\nTente novamente")
        finally:
            self.fecharConexao()

    def inserirRegistros(self):
        cpf = cryptocode.encrypt(self.inputInterno.get(), chaveCriptografia)
        nome = cryptocode.encrypt(self.internoNome, chaveCriptografia)
        ocorrencia = cryptocode.encrypt(self.inputRegistro.get(), chaveCriptografia)
        dataOcorrencia = cryptocode.encrypt(self.inputDataRegistro.get(), chaveCriptografia)
        registradoPor = cryptocode.encrypt(nomeUsuarioLogado, chaveCriptografia)
        try:
            self.conectaBancoDados()        
            self.cursor.execute("CREATE TABLE IF NOT EXISTS ocorrencias (cpf TEXT, nome TEXT, ocorrencia TEXT, dataOcorrencia TEXT, registradoPor TEXT)")    
            self.cursor.execute("INSERT INTO ocorrencias VALUES(?,?,?,?,?)", (cpf, nome, ocorrencia, dataOcorrencia, registradoPor))
            self.banco.commit()
            self.cursor.execute("SELECT ocorrencia, dataOcorrencia, registradoPor FROM ocorrencias WHERE cpf='"+cpf+"'")
            for i in self.cursor.fetchall():
                registroRetornado = cryptocode.decrypt(i[0], chaveCriptografia)
                dataOcorrenciaRetornada = cryptocode.decrypt(i[1], chaveCriptografia)
                registradoPorRetornado = cryptocode.decrypt(i[2], chaveCriptografia)
                self.tabelaRegistros.insert("", END, values=(dataOcorrenciaRetornada, registroRetornado, registradoPorRetornado))
        except Exception as erro:
            messagebox.showerror(title="Erro ao inserir registro", message="Erro: " + str(erro) + ".\nTente novamente")
        finally:
            self.fecharConexao()
    
    def pesquisarInterno(self):
        for n in self.tabela.get_children():
            self.tabela.delete(n)
        for n in self.tabelaRegistros.get_children():
            self.tabelaRegistros.delete(n)
        cpf = self.inputInterno.get()
        try:
            self.conectaBancoDados()               
            self.cursor.execute("SELECT nome, cpf, dataSaida FROM internos")
            for i in self.cursor.fetchall():
                if cpf == cryptocode.decrypt(i[1], chaveCriptografia):                    
                    global internoNome, cpfAcolhido
                    internoNome = cryptocode.decrypt(i[0], chaveCriptografia)
                    cpfAcolhido = i[1]
                    self.botaoGerarPdf.place(x=830,y=630)
                    if i[2] == '':
                        self.inputInserirMedicamentos.config(state='normal', fg='dark gray')
                        self.inputInserirMedicamentos.insert(0, "Insira o nome, dosagem e posologia do medicamento")
                        self.botaoInserirMedicamentos.place(x=782, y=100)
                        self.inputMedico.config(state='normal', fg='dark gray')
                        self.inputMedico.insert(0, 'Nome e CRM do(a) médico(a)')
                        self.inputDataRegistro.config(state='normal', fg='dark gray')
                        self.inputDataRegistro.insert(0, 'Data da ocorrência')
                        self.botaoRegistro.place(x=810,y=370)
                        self.botaoMotivoSaida.place(x=655, y=630)                        
                        self.botaoInserirPdf.place(x=819, y=40)
                        self.inputRegistro.config(state='normal')
                        self.inputRegistro.insert(0, "Digite o que aconteceu para registro")
                        self.inputDataSaida.config(state='normal', fg='dark gray')
                        self.inputDataSaida.insert(0, 'Data de saída')
                        self.inputMotivoSaida.config(state='normal', fg='dark gray')
                        self.inputMotivoSaida.insert(0, 'Digite o motivo da saída')
                    try:
                        self.cursor.execute("SELECT id, cpf, medicamento, medico, receita FROM medicamento")
                        for i in self.cursor.fetchall():
                            if cpf == cryptocode.decrypt(i[1], chaveCriptografia):
                                id = i[0]                                
                                medicamentoRetornado = cryptocode.decrypt(i[2], chaveCriptografia)
                                medicoRetornado = cryptocode.decrypt(i[3], chaveCriptografia)
                                self.tabela.insert("", END, values=(id, medicamentoRetornado, medicoRetornado))                                           
                    except:
                        self.tabela.insert('', END, values=("SEM MEDICAMENTOS"))
                    try:
                        self.cursor.execute("SELECT cpf, dataOcorrencia, ocorrencia, registradoPor FROM ocorrencias")                        
                        for i in self.cursor.fetchall():
                            if cpf == cryptocode.decrypt(i[0], chaveCriptografia):
                                dataOcorrenciaRetornada = cryptocode.decrypt(i[1], chaveCriptografia)
                                registroRetornado = cryptocode.decrypt(i[2], chaveCriptografia)
                                registradoPorRetornado = cryptocode.decrypt(i[3], chaveCriptografia)
                                self.tabelaRegistros.insert("", END, values=(dataOcorrenciaRetornada, registroRetornado, registradoPorRetornado))                                
                    except:
                        self.tabelaRegistros.insert('', END, values=("SEM REGISTROS"))
        finally:
            self.fecharConexao()

    def pesquisarEntradas(self):
        for n in self.tabelaEntradaMunicipio.get_children():
            self.tabelaEntradaMunicipio.delete(n)            
        cidade = self.entryMunicipio.get()
        try:
            self.conectaBancoDados()    
            self.cursor.execute("SELECT nome, dataEntrada, dataSaida, motivoSaida, municipio FROM internos")
            for i in self.cursor.fetchall():                
                if cidade == cryptocode.decrypt(i[4], chaveCriptografia):                
                    nomeRetornado = cryptocode.decrypt(i[0], chaveCriptografia)
                    dataEntradaRetornada = cryptocode.decrypt(i[1], chaveCriptografia)
                    dataSaidaRetornada = cryptocode.decrypt(i[2], chaveCriptografia) if i[2] != "" else ""
                    motivoSaidaRetornado = cryptocode.decrypt(i[3], chaveCriptografia) if i[3] != "" else ''
                    self.tabelaEntradaMunicipio.insert('','end',values=(nomeRetornado, dataEntradaRetornada, dataSaidaRetornada, motivoSaidaRetornado))
        except Exception as erro:            
            messagebox.showerror(title="Erro ao pesquisar", message="Erro: " + str(erro) + ".\nTente novamente")
        finally:
            self.fecharConexao()
    
    def listarSaidas(self):
        cidade = self.entryMunicipioSaida.get()
        nomeAcolhido = self.entryAcolhidoSaida.get()
        if cidade != 'Município' and nomeAcolhido != 'Nome do(a) acolhido(a)':
            messagebox.showerror("Erro", "Apenas um campo deve ser preenchido.")
        else:
            for n in self.tabelaSaidas.get_children():
                self.tabelaSaidas.delete(n)        
            try:
                self.conectaBancoDados()
                self.cursor.execute("SELECT nome, dataEntrada, dataSaida, motivoSaida, municipio FROM internos")
                for i in self.cursor.fetchall():
                    if cidade != '':
                        if cidade == cryptocode.decrypt(i[4], chaveCriptografia) or nomeAcolhido == cryptocode.decrypt(i[0], chaveCriptografia):                
                            nomeRetornado = cryptocode.decrypt(i[0], chaveCriptografia)
                            dataEntradaRetornada = cryptocode.decrypt(i[1], chaveCriptografia)
                            dataSaidaRetornada = cryptocode.decrypt(i[2], chaveCriptografia) if i[2] != "" else ""
                            motivoSaidaRetornado = cryptocode.decrypt(i[3], chaveCriptografia) if i[3] != "" else ''
                            self.tabelaSaidas.insert('','end',values=(nomeRetornado, dataEntradaRetornada, dataSaidaRetornada, motivoSaidaRetornado))                
            except Exception as erro:            
                messagebox.showerror(title="Erro ao pesquisar", message="Erro: " + erro + ".\nTente novamente")
            finally:
                self.fecharConexao()
    
    def registrarSaida(self):
        dataSaida = cryptocode.encrypt(self.inputDataSaida.get(), chaveCriptografia)
        motivoSaida = cryptocode.encrypt(self.inputMotivoSaida.get(), chaveCriptografia)
        try:
            self.conectaBancoDados()
            self.cursor.execute("UPDATE internos SET dataSaida = '"+dataSaida+"', motivoSaida = '"+motivoSaida+"' WHERE cpf = '"+cpfAcolhido+"'")
            self.banco.commit()    
        except Exception as erro:
            messagebox.showerror(title="Erro ao registrar saída", message="Erro: " + erro + ".\nTente novamente")
        finally:
            self.fecharConexao()

    def gerarRelatorioAcolhimento(self):
        cpf = self.inputInterno.get()
        try:
            self.conectaBancoDados()
            dadosInterno = self.cursor.execute("SELECT nome, cpf, fichaInscricao FROM internos")
            for i in dadosInterno.fetchall():
                if cpf == cryptocode.decrypt(i[1], chaveCriptografia):
                    global nomeAcolhido
                    nomeAcolhido = cryptocode.decrypt(i[0], chaveCriptografia)
                    b64 = i[2]
                    base64EncodedStr = base64.b64encode(b64)
                    bytes = b64decode(base64EncodedStr, validate=True)
                    if bytes[0:4] != b'%PDF':
                        raise ValueError('Missing the PDF file signature')
                    f = open('Ficha.pdf', 'wb')
                    f.write(bytes)
                    f.close()                                        
            self.gerarPdfMedicamentos()
            self.gerarPdfRegistros()
            self.gerarPdfVisitas()
            self.mesclarPdf()
        
        finally:
            self.fecharConexao()
                
    def mesclarPdf(blob):
        global nomeAcolhido
        listaPdf = ['Ficha.pdf', 'medicamentos.pdf', 'ocorrencias.pdf', 'visitas.pdf']
        merger = PdfMerger()
        for pdf in listaPdf:
            merger.append(pdf)        
        merger.write('Ficha cadastral de ' + nomeAcolhido + '.pdf')
        merger.close()
        subprocess.Popen(['Ficha cadastral de ' + nomeAcolhido + '.pdf'], shell=True)
        
    def gerarPdfMedicamentos(self):
        try:
            self.conectaBancoDados()
            nome = ''
            cpf = self.inputInterno.get()
            coluna1 = 20*mm
            coluna2 = 50*mm
            coluna3 = 135*mm
            posicaoLinha = 250*mm
            rel = canvas.Canvas("medicamentos.pdf", pagesize=A4)
            rel.rotate(55)
            rel.setFontSize(150)
            rel.setFillColorRGB(0.9, 0.9, 0.9)
            rel.drawString(200,-55,'SIGILOSO')
            rel.rotate(-55)
            rel.setFontSize(4*mm)
            rel.setFillColorRGB(0,0,0)            
            self.cursor.execute("SELECT id, cpf, nome, medicamento, medico, receita FROM medicamento")
            n = 0
            for i in self.cursor.fetchall():                
                if cpf == cryptocode.decrypt(i[1], chaveCriptografia):                    
                    n += 1
                    nome = cryptocode.decrypt(i[2], chaveCriptografia)
                    rel.drawString(20*mm, posicaoLinha, "Nome")#começa em 15 termina 45
                    rel.drawString(20*mm, posicaoLinha - 5*mm, "Medicamento")#começa em 45 termina em 135
                    rel.drawString(20*mm, posicaoLinha - 10*mm, "Médico(a)")#começa em 135 termina em 185
                    rel.drawString(50*mm, posicaoLinha, cryptocode.decrypt(i[2], chaveCriptografia))
                    rel.drawString(50*mm, posicaoLinha - 5*mm, cryptocode.decrypt(i[3], chaveCriptografia))
                    rel.drawString(50*mm, posicaoLinha - 10*mm, cryptocode.decrypt(i[4], chaveCriptografia))
                    posicaoLinha -= 20*mm
                    receita = i[5]
                    base64EncodedStr = base64.b64encode(receita)
                    bytes = b64decode(base64EncodedStr, validate=True)
                    if bytes[0:4] != b'%PDF':
                        raise ValueError('Missing the PDF file signature')
                    f = open('receita de '+cryptocode.decrypt(i[3], chaveCriptografia)+' para ' + ' '+nome +'.pdf', 'wb')
                    f.write(bytes)
                    f.close()
                    subprocess.Popen(['receita de '+cryptocode.decrypt(i[3], chaveCriptografia)+' para ' + ' '+nome +'.pdf'], shell=True)

            if n == 0: rel.drawCentredString(300, 655, 'NÃO HÁ MEDICAMENTOS REGISTRADOS')
            rel.drawString(coluna1, 270*mm, "CPF: " + cpf)
            rel.drawString(coluna1, 265*mm, "Nome: " + nome)
            rel.save()                   
        finally:
            self.fecharConexao()

    def gerarPdfRegistros(self):
        cpf = self.inputInterno.get()
        coluna1 = 20*mm
        coluna2 = 50*mm
        coluna3 = 135*mm
        margem = 15*mm
        posicaoLinha = 240*mm
        
        rel = canvas.Canvas("ocorrencias.pdf", pagesize=A4)
        rel.rotate(55)
        rel.setFontSize(150)
        rel.setFillColorRGB(0.9, 0.9, 0.9)
        rel.drawString(200,-55,'SIGILOSO')
        rel.rotate(-55)
        rel.setFontSize(4*mm)
        rel.setFillColorRGB(0,0,0)
        rel.drawCentredString(30*mm, 250*mm, "Data do Fato")#começa em 15 termina 45
        rel.drawCentredString(105*mm, 250*mm, "Ocorrência")#começa em 45 termina em 135
        rel.drawCentredString(165*mm, 250*mm, "Registrado por")#começa em 135 termina em 185
        estiloParagrafo = ParagraphStyle('estiloParagrafo', alignment=4, fontSize=4*mm)
        n = 0
        try:
            self.conectaBancoDados()
            dadosMedicacao = self.cursor.execute("SELECT cpf, nome, ocorrencia, dataOcorrencia, registradoPor FROM ocorrencias")        
            for linha in dadosMedicacao.fetchall():
                declaracao = Paragraph(cryptocode.decrypt(linha[2], chaveCriptografia), style=estiloParagrafo)
                declaracao.wrapOn(rel, 230, 0)                        
                if cpf == cryptocode.decrypt(linha[0], chaveCriptografia):
                    n+= 1
                    if n == 1:
                        rel.drawString(coluna1, 270*mm, "CPF: " + cpf)
                        rel.drawString(coluna1, 265*mm, "Nome: " + nomeAcolhido)          
                    if posicaoLinha - declaracao.height < margem:
                        rel.showPage()
                        rel.drawString(coluna1, 270*mm, "CPF: " + cpf)
                        rel.drawString(coluna1, 265*mm, "Nome: " + nomeAcolhido)
                        posicaoLinha = 240*mm
                        rel.rotate(55)
                        rel.setFontSize(150)
                        rel.setFillColorRGB(0.9, 0.9, 0.9)
                        rel.drawString(200,-55,'SIGILOSO')
                        rel.rotate(-55)
                        rel.setFontSize(4*mm)
                        rel.setFillColorRGB(0,0,0)
                    rel.drawString(coluna1, posicaoLinha, cryptocode.decrypt(linha[3], chaveCriptografia))
                    declaracao.drawOn(rel, coluna2, 4*mm+posicaoLinha-declaracao.height)
                    rel.drawString(coluna3, posicaoLinha, cryptocode.decrypt(linha[4], chaveCriptografia))                    
                    posicaoLinha -= declaracao.height + 2*mm
            if n == 0: rel.drawCentredString(300, 655, 'NÃO HÁ OCORRÊNCIAS REGISTRADOS')
            rel.save()
        except Exception as erro:
            messagebox.showerror("Erro ao gerar PDF de registros", "Erro: " + str(erro) + " detectado. Tente novamente")   
        finally:
            self.fecharConexao()

    def gerarPdfVisitas(self):
        cpf = self.inputInterno.get()
        nome = ''
        x = 210*mm
        y = 297*mm
        coluna1 = 20*mm
        coluna2 = 50*mm
        coluna3 = 160*mm
        posicaoLinha = 240*mm
        rel = canvas.Canvas("visitas.pdf", pagesize=A4)
        rel.rotate(55)
        rel.setFontSize(150)
        rel.setFillColorRGB(0.9, 0.9, 0.9)
        rel.drawString(200,-55,'SIGILOSO')
        rel.rotate(-55)
        rel.setFontSize(12)
        rel.setFillColorRGB(0,0,0)
        rel.drawCentredString(30*mm, 250*mm, "Data da Visita")#começa em 15 termina 45
        rel.drawCentredString(100*mm, 250*mm, "Visitante")#começa em 45 termina em 155
        rel.drawCentredString(170*mm, 250*mm, "Parentesco")#começa em 155 termina em 185
        try:
            self.conectaBancoDados()
            dadosMedicacao = self.cursor.execute("SELECT cpf, visitado, visitante, parentesco, dataVisita FROM visitas")
            n = 0
            for linha in dadosMedicacao.fetchall():
                if cpf == cryptocode.decrypt(linha[0], chaveCriptografia):
                    n += 1
                    nome = cryptocode.decrypt(linha[1], chaveCriptografia)
                    rel.drawString(coluna1, posicaoLinha, cryptocode.decrypt(linha[4], chaveCriptografia))
                    rel.drawString(coluna2, posicaoLinha, cryptocode.decrypt(linha[2], chaveCriptografia))
                    rel.drawString(coluna3, posicaoLinha, cryptocode.decrypt(linha[3], chaveCriptografia))
                    posicaoLinha -= 15
            if n == 0: rel.drawCentredString(300, 655, 'NÃO HÁ VISITAS REGISTRADAS')    
            rel.drawString(coluna1, 270*mm, "CPF: " + cpf)
            rel.drawString(coluna1, 265*mm, "Nome: " + nome)
            rel.save()
        except Exception as erro:
            messagebox.showerror("Erro ao gerar PDF visitas", "Erro " + str(erro) + " ocorreu. Tente Novamente")
        finally:
            self.fecharConexao()

    def listarInternos(self):
        for n in self.tabelaInternos.get_children():
            self.tabelaInternos.delete(n)        
        try:
            self.conectaBancoDados()
            self.cursor.execute("SELECT nome, cpf, dataSaida FROM internos")
            listaInternos = self.cursor.fetchall()
            for i in listaInternos:
                nomeRetornado = cryptocode.decrypt(i[0], chaveCriptografia)
                cpfRetornado = cryptocode.decrypt(i[1], chaveCriptografia)
                dataSaidaRetornada = cryptocode.decrypt(i[2], chaveCriptografia) if i[2] != "" else ""                
                self.tabelaInternos.insert('','end',values=(nomeRetornado, cpfRetornado, dataSaidaRetornada))                
        except Exception as erro:            
            messagebox.showerror(title="Erro ao pesquisar", message="Erro: " + erro + ".\nTente novamente")
        finally:
            self.fecharConexao()      

    def limparListaInternos(self):
        for n in self.tabela.get_children():
            self.tabela.delete(n)

    def cadastrarUsuario(self):
        mensagem = ''
        nome = self.inputNomeUsuarioCadastrar.get()
        senha = self.inputSenhaUsuarioCadastrar.get()
        confirmacaoSenha = self.inputConfirmarSenhaUsuarioCadastrar.get()
        if senha != confirmacaoSenha : mensagem += "As senhas não são iguais\n"
        if len(senha) < 12 : mensagem += "A senha deve ter mais de 12 caracteres"
        else:
            perfil = 0 if self.perfil.get() == "Administrador" else 1
            try:
                self.conectaBancoDados()
                self.cursor.execute("INSERT INTO usuarios VALUES (?,?,?)", (nome, cryptocode.encrypt(senha, chaveCriptografia), perfil))
                self.banco.commit()
                messagebox.showinfo("Sucesso ao cadastrar usuário", nome + " cadastrado(a) com sucesso")
            except Exception as erro:
                messagebox.showerror("Erro ao cadastrar usuário", str(erro) + " .\n Tente novamente.")
            finally:
                self.fecharConexao()
        messagebox.showerror("Erro na senha", mensagem)
    
    def trocarSenha(self):
        mensagem = ''
        novaSenha = self.inputNovaSenhaCadastrar.get()
        novaSenhaConfirmada = self.inputConfirmarNovaSenhaCadastrar.get()
        if novaSenha != novaSenhaConfirmada : mensagem += "As senhas não são iguais\n"
        if len(novaSenha) < 12 : mensagem += "A senha deve ter mais de 12 caracteres"
        else:
            try:
                self.conectaBancoDados()
                self.cursor.execute("UPDATE usuarios SET senha = '"+cryptocode.encrypt(novaSenha, chaveCriptografia)+"' WHERE nome = '"+nomeUsuarioLogado+"'")
                self.banco.commit()
                messagebox.showinfo("Sucesso ao alterar senha", "Senha alterada com sucesso")
            except Exception as erro:
                messagebox.showerror("Erro ao alterar a senha", str(erro) + " .\n Tente Novamente")
            finally:
                self.fecharConexao()
        if mensagem != '': messagebox.showerror("Erro na nova senha", mensagem)

    def linhaSelecionada(self):
        itemSelecionado = self.tabela.selection()[0]
        valores = self.tabela.item(itemSelecionado, 'values')
        try:
            self.conectaBancoDados()            
            self.cursor.execute("SELECT receita FROM medicamento WHERE id ='"+valores[0]+"'")
            l = self.cursor.fetchall()
            b64 = l[0][0]
            base64EncodedStr = base64.b64encode(b64)
            bytes = b64decode(base64EncodedStr, validate=True)
            if bytes[0:4] != b'%PDF':
                raise ValueError('Missing the PDF file signature')
            f = open('receita.pdf', 'wb')
            f.write(bytes)
            f.close()
            subprocess.Popen(['receita.pdf'], shell=True)
        finally:
            self.fecharConexao()

class login(funcoes):
    def __init__(self):
        self.janelaLogin = janelaLogin
        self.tela()
        janelaLogin.mainloop() 
    
    def placeholder(entrada, self):
        self.delete(0, 'end')
        self.config(fg='black')        

    def estavazio(self, entrada, mensagem):
        if entrada.get() == '':
            entrada.insert(0, mensagem)
            entrada.config(fg='dark gray')

    def telaCadastrarUsuario(self):
        self.listaPerfilUsuario = ['Usuario', 'Administrador']
        self.perfil = StringVar()
        self.perfil.set(self.listaPerfilUsuario[0])
        self.telaCadUsuario = Toplevel()
        self.telaCadUsuario.title("Cadastrar usuário")
        self.window_height = 300
        self.window_width = 300
        self.telaCadUsuario.resizable(False, False)
        self.screen_width = self.telaCadUsuario.winfo_screenwidth()
        self.screen_height = self.telaCadUsuario.winfo_screenheight()
        self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))
        self.telaCadUsuario.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_cordinate, self.y_cordinate))
        self.telaCadUsuario.configure(background="#22aaee")
        self.inputNomeUsuarioCadastrar = Entry(self.telaCadUsuario, width=40, fg='dark gray')
        self.inputNomeUsuarioCadastrar.place(x=30, y=10)
        self.inputNomeUsuarioCadastrar.insert(0, "Nome completo")
        self.inputNomeUsuarioCadastrar.bind('<FocusIn>', lambda p:self.placeholder(self.inputNomeUsuarioCadastrar))
        self.inputNomeUsuarioCadastrar.bind('<FocusOut>', lambda p:self.estavazio(self.inputNomeUsuarioCadastrar, "Digite o nome do(a) usuário(a)"))        
        Label(self.telaCadUsuario, text="Digite a senha. Deve ter mais de 12 caracteres").place(x=30, y=40)
        self.inputSenhaUsuarioCadastrar = Entry(self.telaCadUsuario, width=40, fg='dark gray', show="*")
        self.inputSenhaUsuarioCadastrar.place(x=30, y=70)        
        Label(self.telaCadUsuario, text="Confirme a senha").place(x=30, y=100)
        self.inputConfirmarSenhaUsuarioCadastrar = Entry(self.telaCadUsuario, width=40, fg='dark gray', show="*")
        self.inputConfirmarSenhaUsuarioCadastrar.place(x=30, y=130)        
        self.menuPerfilUsuario = OptionMenu(self.telaCadUsuario, self.perfil, *self.listaPerfilUsuario)
        self.menuPerfilUsuario.place(x=30, y = 150)
        Button(self.telaCadUsuario, text="Cadastrar usuário", command=self.cadastrarUsuario).place(x=30, y=200)

    def tela(self):
        self.janelaLogin.title("Centro de Tratamento Elchadai")
        self.window_height = 200
        self.window_width = 300
        self.janelaLogin.resizable(False, False)
        self.screen_width = janelaLogin.winfo_screenwidth()
        self.screen_height = janelaLogin.winfo_screenheight()
        self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))
        self.janelaLogin.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_cordinate, self.y_cordinate))
        self.janelaLogin.configure(background="#22aaee")
        
        self.inputUsuario = Entry(janelaLogin, width=40, fg='dark gray')
        self.inputUsuario.place(x=30, y=10)
        self.inputUsuario.insert(0, "Usuário")
        self.inputUsuario.focus()
        self.inputUsuario.bind('<FocusIn>', lambda p:self.placeholder(self.inputUsuario))
        self.inputUsuario.bind('<FocusOut>', lambda p:self.estavazio(self.inputUsuario, "Usuário"))

        self.inputSenha = Entry(janelaLogin, width=40,fg='dark gray', show='*')
        self.inputSenha.place(x=30, y=40)
        self.inputSenha.insert(0, "Senha")
        self.inputSenha.bind('<FocusIn>', lambda p:self.placeholder(self.inputSenha))
        self.inputSenha.bind('<FocusOut>', lambda p:self.estavazio(self.inputSenha, "Senha"))
        self.inputSenha.bind('<KeyPress-Return>', lambda p:self.logar(self.inputUsuario, self.inputSenha))

        self.botaoCadastrarUsuario = Button(janelaLogin, text="Cadastrar usuário", command=self.telaCadastrarUsuario)
        self.botaoTelaPrincipal = Button(janelaLogin, text="Ir para tela principal", command=self.telaPrincipal)

    def telaAlterarSenha(self):
        self.telaAlterarSenha = Toplevel()
        self.telaAlterarSenha.title("Alterar senha")
        self.window_height = 200
        self.window_width = 300
        self.telaAlterarSenha.resizable(False, False)
        self.screen_width = self.telaAlterarSenha.winfo_screenwidth()
        self.screen_height = self.telaAlterarSenha.winfo_screenheight()
        self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))
        self.telaAlterarSenha.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_cordinate, self.y_cordinate))
        self.telaAlterarSenha.configure(background="#22aaee")
        
        Label(self.telaAlterarSenha, text="Digite a nova senha.\nDeve ter mais de 12 caracteres").place(x=30, y=10)
        self.inputNovaSenhaCadastrar = Entry(self.telaAlterarSenha, width=40, fg='dark gray', show="*")
        self.inputNovaSenhaCadastrar.place(x=30, y=50)        
        Label(self.telaAlterarSenha, text="Confirme a senha").place(x=30, y=80)
        self.inputConfirmarNovaSenhaCadastrar = Entry(self.telaAlterarSenha, width=40, fg='dark gray', show="*")
        self.inputConfirmarNovaSenhaCadastrar.place(x=30, y=100)
        Button(self.telaAlterarSenha, text="Trocar Senha", command=self.trocarSenha).place(x=30, y=170)        

    def telaPrincipal(self):
        janelaLogin.destroy()
        self.janelaPrincipal = Tk()
        self.janelaPrincipal.title("Centro de Tratamento Elchadai")
        window_height = 700
        window_width = 915
        self.janelaPrincipal.resizable(False, False)
        screen_width = self.janelaPrincipal.winfo_screenwidth()
        screen_height = self.janelaPrincipal.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.janelaPrincipal.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.janelaPrincipal.configure(background="#22aaee")
####################CRIA AS ABAS####################
        abas = ttk.Notebook(self.janelaPrincipal)
        abas.place(x=0, y=0, width=915, height=700)
        abaDados = Frame(abas)
        abaEntradas = Frame(abas)
        abaSaidas = Frame(abas)
        abaVisitas = Frame(abas)
        abaPIA = Frame(abas)
        abaInternos = Frame(abas)
        abas.add(abaDados, text='Dados Pessoais')
        abas.add(abaEntradas, text='Entradas')
        #abas.add(abaSaidas, text="Saídas")
        abas.add(abaVisitas, text='Visitas')
        abas.add(abaPIA, text='PIA - Plano Individual de Atendimento')
        abas.add(abaInternos, text='Internos')
####################CRIA AS TABELAS####################
        self.tabela = ttk.Treeview(abaPIA, selectmode='browse', column=('Coluna 1', '2', '3','4'), show='headings', height=10)
        self.tabelaEntradaMunicipio = ttk.Treeview(abaEntradas, selectmode="browse", columns=('1', '2', '3','4'), show='headings', height=29)
        self.tabelaSaidas = ttk.Treeview(abaSaidas, selectmode="browse", columns=('1', '2', '3','4'), show='headings', height= 29)
        self.tabelaVisitas = ttk.Treeview(abaVisitas, selectmode="browse", columns=('1', '2', '3'), show='headings', height=28)
        self.tabelaInternos = ttk.Treeview(abaInternos, selectmode="browse", columns=('1', '2', '3'), show='headings', height=31)
        self.tabelaRegistros = ttk.Treeview(abaPIA, selectmode="browse", columns=('1', '2', '3'), show='headings', height=10)

        self.tabelaEntradaMunicipio.column('1',width=345, stretch=NO)
        self.tabelaEntradaMunicipio.column('2',width=100, stretch=NO)
        self.tabelaEntradaMunicipio.column('3',width=100, stretch=NO)
        self.tabelaEntradaMunicipio.column('4',width=350, stretch=NO)
        self.tabelaEntradaMunicipio.heading('#1', text='Nome do(a) acolhido(a)')
        self.tabelaEntradaMunicipio.heading('#2', text='Data da entrada')
        self.tabelaEntradaMunicipio.heading('#3', text='Data da saída')
        self.tabelaEntradaMunicipio.heading('#4', text='Motivo da saída')
        self.tabelaEntradaMunicipio.place(x=10, y=40)

        self.tabelaSaidas.column('1',width=345, stretch=NO)
        self.tabelaSaidas.column('2',width=100, stretch=NO)
        self.tabelaSaidas.column('3',width=100, stretch=NO)
        self.tabelaSaidas.column('4',width=350, stretch=NO)
        self.tabelaSaidas.heading('#1', text="Nome")
        self.tabelaSaidas.heading('#2', text="Data da entrada")
        self.tabelaSaidas.heading('#3', text="Data da saída")
        self.tabelaSaidas.heading('#4', text="Motivo da saída")
        self.tabelaSaidas.place(x=10,y=40)

        self.tabelaVisitas.column('1',width=400, stretch=NO)
        self.tabelaVisitas.column('2',width=295, stretch=NO)
        self.tabelaVisitas.column('3',width=200, stretch=NO)
        self.tabelaVisitas.heading('#1', text="Nome")
        self.tabelaVisitas.heading('#2', text="Parentesco")
        self.tabelaVisitas.heading('#3', text="Data da visita")
        self.tabelaVisitas.place(x=10, y=70)
        
        self.tabela.heading('#1', text="ID")
        self.tabela.column('Coluna 1', width=30, stretch=NO)
        self.tabela.column('2', width=432)
        self.tabela.heading('#2', text='Medicamento')
        self.tabela.column('3', width=432)
        self.tabela.heading('#3', text='Médico e CRM')
        self.tabela.place(x=10, y=130)

        self.tabelaRegistros.column('1', width=100, stretch=NO)
        self.tabelaRegistros.column('2', width=540, stretch=NO)
        self.tabelaRegistros.column('3', width=255, stretch=NO)
        self.tabelaRegistros.heading('#1', text='Data')
        self.tabelaRegistros.heading('#2', text='Ocorrência')
        self.tabelaRegistros.heading('#3', text='Registrado por')
        self.tabelaRegistros.place(x=10, y=400)

        self.tabelaInternos.column('1',width=400, stretch=NO)
        self.tabelaInternos.column('2',width=195, stretch=NO)
        self.tabelaInternos.column('3',width=300, stretch=NO)
        self.tabelaInternos.heading('#1', text='Nome do(a) acolhido(a)')
        self.tabelaInternos.heading('#2', text='CPF')
        self.tabelaInternos.heading('#3', text='Data da saída')
        self.tabelaInternos.place(x=10, y=10)

################CRIA AS LISTAS PARA OS OPTIONS################
        self.listaTipoAcolhimento = ['Tipo de Acolhimento', 'Social', 'Particular']
        self.listaSimNao = ['Filhos', 'Sim', 'Não']
        self.listaEscolaridade = ['Escolaridade','Analfabeto', 'Lê e escreve', 'Ensino Fundamental Incompleto', 'Ensino Fundamental Completo', 'Ensino Médio Incompleto', 'Ensino Médio Completo', 'Ensino Superior Incompleto', 'Ensino Superior Completo']
        self.listaEstadoCivil = ['Estado Civil','Solteiro(a)', 'Casado(a)', 'Separado(a) Judicialmente', 'Divorciado(a)', 'Viúvo(a)']
        self.listaDependencias = ['Tipo de dependência','Álcool', 'Maconha / Haxixe','Cocaína', 'Crack', 'Inalantes / Cola / Solvente / Tiner', 'Benzodiazepínico / Diazepan', 'Anfetaminas / Remédios para Emagrecer', 'Ecstasy / MDMA', 'LSD', 'Heroína / Morfina / Metadona']
        
        self.tipoAcolhimento = StringVar()
        self.tipoAcolhimento.set(self.listaTipoAcolhimento[0])
        self.simNao = StringVar()
        self.simNao.set(self.listaSimNao[0])
        self.escolaridade = StringVar()
        self.escolaridade.set(self.listaEscolaridade[0])
        self.estadoCivil = StringVar()
        self.estadoCivil.set(self.listaEstadoCivil[0])
        self.dependencias = StringVar()
        self.dependencias.set(self.listaDependencias[0])
        

################EXIBE A ABA DADOS PESSOAIS####################
        self.labelDadosAcolhido = Label(abaDados, text="DADOS DO(A) ACOLHIDO(A)").place(x=100, y=10)
        self.inputAcolhidoNome = Entry(abaDados, width=74, fg='dark gray')
        self.inputAcolhidoNome.insert(0, "Nome do(a) acolhido(a)")
        self.inputAcolhidoNome.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputAcolhidoNome))
        self.inputAcolhidoNome.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputAcolhidoNome, "Nome do(a) acolhido(a)"))
        self.inputAcolhidoNome.place(x=10, y=40)
        self.inputAcolhidoDataNascimento = Entry(abaDados, width=22, fg='dark gray')
        self.inputAcolhidoDataNascimento.place(x=464, y=40)
        self.inputAcolhidoDataNascimento.insert(0, "Nascimento: 00/00/0000")
        self.inputAcolhidoDataNascimento.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputAcolhidoDataNascimento))
        self.inputAcolhidoDataNascimento.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputAcolhidoDataNascimento, "Nascimento: 00/00/0000"))
        self.inputAcolhidoCpf = Entry(abaDados, width=15, fg='dark gray')
        self.inputAcolhidoCpf.place(x=606, y=40)
        self.inputAcolhidoCpf.insert(0, "Número do CPF")
        self.inputAcolhidoCpf.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputAcolhidoCpf))
        self.inputAcolhidoCpf.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputAcolhidoCpf, "Número do CPF"))
        self.inputAcolhidoIdentidade = Entry(abaDados, width=20, fg='dark gray')
        self.inputAcolhidoIdentidade.place(x=706, y=40)
        self.inputAcolhidoIdentidade.insert(0, "Número do RG")
        self.inputAcolhidoIdentidade.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputAcolhidoIdentidade))
        self.inputAcolhidoIdentidade.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputAcolhidoIdentidade, "Número do RG"))
        self.inputAcolhidoTelefone = Entry(abaDados, width=20, fg='dark gray')
        self.inputAcolhidoTelefone.place(x=10, y=70)
        self.inputAcolhidoTelefone.insert(0, "Número do Telefone")
        self.inputAcolhidoTelefone.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputAcolhidoTelefone))
        self.inputAcolhidoTelefone.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputAcolhidoTelefone, "Número do Telefone"))
        self.inputAcolhidoCep = Entry(abaDados, width=10, fg='dark gray')
        self.inputAcolhidoCep.place(x=140, y=70)
        self.inputAcolhidoCep.insert(0, "CEP")
        self.inputAcolhidoCep.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputAcolhidoCep))
        self.inputAcolhidoCep.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputAcolhidoCep, "CEP"))
        self.inputAcolhidoUf = Entry(abaDados, width=3, fg='dark gray')
        self.inputAcolhidoUf.place(x=210, y=70)
        self.inputAcolhidoUf.insert(0, "UF")
        self.inputAcolhidoUf.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputAcolhidoUf))
        self.inputAcolhidoUf.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputAcolhidoUf, "UF"))
        self.inputAcolhidoMunicípio = Entry(abaDados, width=20, fg='dark gray')
        self.inputAcolhidoMunicípio.place(x=238, y=70)
        self.inputAcolhidoMunicípio.insert(0, "Município")
        self.inputAcolhidoMunicípio.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputAcolhidoMunicípio))
        self.inputAcolhidoMunicípio.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputAcolhidoMunicípio, "Município"))
        self.inputAcolhidoBairro = Entry(abaDados, width=30, fg='dark gray')
        self.inputAcolhidoBairro.place(x=368, y=70)
        self.inputAcolhidoBairro.insert(0, "Bairro")
        self.inputAcolhidoBairro.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputAcolhidoBairro))
        self.inputAcolhidoBairro.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputAcolhidoBairro, "Bairro"))
        self.inputAcolhidoEndereço = Entry(abaDados, width=45, fg='dark gray')
        self.inputAcolhidoEndereço.place(x=558, y=70)
        self.inputAcolhidoEndereço.insert(0, "Endereço")
        self.inputAcolhidoEndereço.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputAcolhidoEndereço))
        self.inputAcolhidoEndereço.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputAcolhidoEndereço, "Endereço"))
        self.inputAcolhidoCredo = Entry(abaDados, width=20, fg='dark gray')
        self.inputAcolhidoCredo.place(x=10, y=100)
        self.inputAcolhidoCredo.insert(0, "Crença Religiosa")
        self.inputAcolhidoCredo.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputAcolhidoCredo))
        self.inputAcolhidoCredo.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputAcolhidoCredo, "Crença Religiosa"))
        menuAcolhidoEstadoCivil = OptionMenu(abaDados, self.estadoCivil, *self.listaEstadoCivil)
        menuAcolhidoEstadoCivil.place(x=140, y=100)
        menuListaFilhos = OptionMenu(abaDados, self.simNao,*self.listaSimNao)
        menuListaFilhos.place(x=330, y=100)
        menuListaEscolaridade = OptionMenu(abaDados, self.escolaridade, *self.listaEscolaridade)
        menuListaEscolaridade.place(x=410,y=100)
        menuAcolhidoTipoDependencia = OptionMenu(abaDados, self.dependencias, *self.listaDependencias)
        menuAcolhidoTipoDependencia.place(x=640, y=100)
        menuTipoAcolhimento = OptionMenu(abaDados, self.tipoAcolhimento, *self.listaTipoAcolhimento)
        menuTipoAcolhimento.place(x=10, y=130)
    
    ######__________________________________________________________________________________________Dados do responsável
        self.labelDadosResponsavel = Label(abaDados, text="DADOS DO(A) RESPONSAVEL: ").place(x=100, y=180)
        self.inputResponsavelNome = Entry(abaDados, width=74, fg='dark gray')
        self.inputResponsavelNome.place(x=10, y=210)
        self.inputResponsavelNome.insert(0, "Nome do(a) Responsável")
        self.inputResponsavelNome.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputResponsavelNome))
        self.inputResponsavelNome.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputResponsavelNome, "Nome do(a) Responsável"))
        self.inputResponsávelParentesco = Entry(abaDados, width=22, fg='dark gray')
        self.inputResponsávelParentesco.place(x=464, y=210)
        self.inputResponsávelParentesco.insert(0, "Parentesco")
        self.inputResponsávelParentesco.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputResponsávelParentesco))
        self.inputResponsávelParentesco.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputResponsávelParentesco, "Parentesco"))
        self.inputResponsávelCpf = Entry(abaDados, width=15, fg='dark gray')
        self.inputResponsávelCpf.place(x=606, y=210)
        self.inputResponsávelCpf.insert(0, "Número do CPF")
        self.inputResponsávelCpf.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputResponsávelCpf))
        self.inputResponsávelCpf.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputResponsávelCpf, "Número do CPF"))
        self.inputResponsávelIdentidade = Entry(abaDados, width=20, fg='dark gray')
        self.inputResponsávelIdentidade.place(x=706, y=210)
        self.inputResponsávelIdentidade.insert(0, "Número do RG")
        self.inputResponsávelIdentidade.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputResponsávelIdentidade))
        self.inputResponsávelIdentidade.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputResponsávelIdentidade, "Número do RG"))
        self.inputResponsávelTelefone = Entry(abaDados, width=20, fg='dark gray')
        self.inputResponsávelTelefone.place(x=10, y=240)
        self.inputResponsávelTelefone.insert(0, "Número do Telefone")
        self.inputResponsávelTelefone.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputResponsávelTelefone))
        self.inputResponsávelTelefone.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputResponsávelTelefone, "Número do Telefone"))
        self.inputResponsávelCep = Entry(abaDados, width=10, fg='dark gray')
        self.inputResponsávelCep.place(x=140, y=240)
        self.inputResponsávelCep.insert(0, "CEP")
        self.inputResponsávelCep.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputResponsávelCep))
        self.inputResponsávelCep.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputResponsávelCep, "CEP"))
        self.inputResponsávelUf = Entry(abaDados, width=3, fg='dark gray')
        self.inputResponsávelUf.place(x=210, y=240)
        self.inputResponsávelUf.insert(0, "UF")
        self.inputResponsávelUf.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputResponsávelUf))
        self.inputResponsávelUf.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputResponsávelUf, "UF"))
        self.inputResponsávelMunicípio = Entry(abaDados, width=20, fg='dark gray')
        self.inputResponsávelMunicípio.place(x=238, y=240)
        self.inputResponsávelMunicípio.insert(0, "Município")
        self.inputResponsávelMunicípio.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputResponsávelMunicípio))
        self.inputResponsávelMunicípio.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputResponsávelMunicípio, "Município"))
        self.inputResponsávelBairro = Entry(abaDados, width=30, fg='dark gray')
        self.inputResponsávelBairro.place(x=368, y=240)
        self.inputResponsávelBairro.insert(0, "Bairro")
        self.inputResponsávelBairro.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputResponsávelBairro))
        self.inputResponsávelBairro.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputResponsávelBairro, "Bairro"))
        self.inputResponsávelEndereço = Entry(abaDados, width=45, fg='dark gray')
        self.inputResponsávelEndereço.place(x=558, y=240)
        self.inputResponsávelEndereço.insert(0, "Endereço")
        self.inputResponsávelEndereço.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputResponsávelEndereço))
        self.inputResponsávelEndereço.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputResponsávelEndereço, "Endereço"))
        Label(abaDados, text='Data de entrada:').place(x=10, y=280)
        h = datetime.datetime.now()
        self.inputDataEntrada = Entry(abaDados, width=10)
        self.inputDataEntrada.place(x=111, y=280)
        self.inputDataEntrada.insert(0, h.strftime("%d/%m/%Y"))
        Button(abaDados, text='Registrar entrada', command=self.validarPreenchimentoCampos).place(x=181, y=280)
        Button(abaDados, text='Inserir ficha assinada', command=self.inserirFichaAssinada).place(x=730 ,y=280)
        Button(abaDados, text='Trocar senha', command=self.telaAlterarSenha, width=20).place(x=450 ,y=400)

####################EXIBE A ABA ENTRADAS####################
        self.entryMunicipio = Entry(abaEntradas, width=30, fg='dark gray')
        self.entryMunicipio.place(x=69, y=10)
        self.entryMunicipio.insert(0, "Município")
        self.entryMunicipio.bind('<FocusIn>', lambda p:login.placeholder(self, self.entryMunicipio))
        self.entryMunicipio.bind('<FocusOut>', lambda p:login.estavazio(self, self.entryMunicipio, "Município"))
        Button(abaEntradas, text="Pesquisar", command=self.pesquisarEntradas).place(x=259, y=10)
        
####################EXIBE A ABA SAÍDAS####################
        self.entryMunicipioSaida = Entry(abaSaidas, width=30, fg='dark gray')
        self.entryMunicipioSaida.place(x=69, y=10)
        self.entryMunicipioSaida.insert(0, "Município")
        self.entryMunicipioSaida.bind('<FocusIn>', lambda p:login.placeholder(self, self.entryMunicipioSaida))
        self.entryMunicipioSaida.bind('<FocusOut>', lambda p:login.estavazio(self, self.entryMunicipioSaida, "Município"))
        self.entryAcolhidoSaida = Entry(abaSaidas, width=30, fg='dark gray')
        self.entryAcolhidoSaida.place(x=325, y=10)
        self.entryAcolhidoSaida.insert(0, "Nome do(a) acolhido(a)")
        self.entryAcolhidoSaida.bind('<FocusIn>', lambda p:login.placeholder(self, self.entryAcolhidoSaida))
        self.entryAcolhidoSaida.bind('<FocusOut>', lambda p:login.estavazio(self, self.entryAcolhidoSaida, "Nome do(a) acolhido(a)"))
        Button(abaSaidas, text='Pesquisar saída', command=self.listarSaidas).place(x= 515, y=10)
        
####################EXIBE A ABA VISITAS####################
        self.entryVisitanteAcolhido = Entry(abaVisitas, width=40, fg='dark gray')
        self.entryVisitanteAcolhido.place(x=10, y=10)
        self.entryVisitanteAcolhido.insert(0, "Nome do(a) acolhido(a)")
        self.entryVisitanteAcolhido.bind('<FocusIn>', lambda p:login.placeholder(self, self.entryVisitanteAcolhido))
        self.entryVisitanteAcolhido.bind('<FocusOut>', lambda p:login.estavazio(self, self.entryVisitanteAcolhido, "CPF do(a) acolhido(a)"))
        self.entryVisitanteNome = Entry(abaVisitas, width=50, fg='dark gray')
        self.entryVisitanteNome.place(x=260,y=10)
        self.entryVisitanteNome.insert(0, "Nome do(a) visitante")
        self.entryVisitanteNome.bind('<FocusIn>', lambda p:login.placeholder(self, self.entryVisitanteNome))
        self.entryVisitanteNome.bind('<FocusOut>', lambda p:login.estavazio(self, self.entryVisitanteNome, "Nome do(a) visitante"))
        self.entryVisitanteParentesco = Entry(abaVisitas, width=37, fg='dark gray')
        self.entryVisitanteParentesco.place(x=570, y=10)
        self.entryVisitanteParentesco.insert(0, "Parentesco do(a) visitante")
        self.entryVisitanteParentesco.bind('<FocusIn>', lambda p:login.placeholder(self, self.entryVisitanteParentesco))
        self.entryVisitanteParentesco.bind('<FocusOut>', lambda p:login.estavazio(self, self.entryVisitanteParentesco, "Parentesco do(a) visitante"))
        self.botaoRegistrarVisita = Button(abaVisitas, text='Registrar Visita', width=13, command=self.registrarVisita)
        self.botaoRegistrarVisita.place(x=805, y=10)
        self.entryAcolhidoVisitantes = Entry(abaVisitas, width=130, fg='dark gray')
        self.entryAcolhidoVisitantes.place(x=10, y=40)
        self.entryAcolhidoVisitantes.insert(0, 'Digite o nome do(a) acolhido(a) para pesquisar as visitas e pressione ENTER')
        self.entryAcolhidoVisitantes.bind('<FocusIn>', lambda p:login.placeholder(self, self.entryAcolhidoVisitantes))
        self.entryAcolhidoVisitantes.bind('<FocusOut>', lambda p:login.estavazio(self, self.entryAcolhidoVisitantes, "Digite o nome do(a) acolhido(a) para pesquisar as visitas e pressione ENTER"))
        self.entryAcolhidoVisitantes.bind('<KeyPress-Return>', lambda p:self.pesquisarVisitas())
        
####################EXIBE A ABA PIA - PLANO INDIVIDUAL DE ATENDIMENTO####################
        self.inputInterno = Entry(abaPIA, width=30, fg='dark gray')
        self.inputInterno.place(x=50, y=10)
        self.inputInterno.insert(0, "CPF")
        self.inputInterno.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputInterno))
        self.inputInterno.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputInterno, "CPF"))
        self.inputInterno.bind('<KeyPress-Return>', lambda p:self.pesquisarInterno())
        self.botaoInserirPdf = Button(abaPIA,text='Inserir PDF')
        labelMedicamentos = Label(abaPIA, text="MEDICAMENTOS")
        labelMedicamentos.place(x=100, y=70)
        self.inputInserirMedicamentos = Entry(abaPIA, width=50, state='disabled', fg='dark gray')
        self.inputInserirMedicamentos.place(x=146, y=100)
        self.inputInserirMedicamentos.insert(0, "Insira o nome, dosagem e posologia do medicamento")
        self.inputInserirMedicamentos.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputInserirMedicamentos))
        self.inputInserirMedicamentos.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputInserirMedicamentos, "Insira o nome, dosagem e posologia do medicamento"))
        self.inputMedico = Entry(abaPIA, width=50, fg="dark gray", state='disabled')
        self.inputMedico.place(x=460, y=100)
        self.inputMedico.insert(0, "Nome e CRM do(a) médico(a)")
        self.inputMedico.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputMedico))
        self.inputMedico.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputMedico, "Nome e CRM do(a) médico(a)"))
        self.botaoInserirMedicamentos = Button(abaPIA, text="Inserir medicamento", command = self.inserirMedicamento)
        
        self.tabela.bind('<Button-1>', lambda p:self.linhaSelecionada())
        self.inputRegistro = Entry(abaPIA, width=100, state='disabled', fg='dark gray')
        self.inputRegistro.place(x=117,y=370)
        self.inputRegistro.insert(0, "Inserir registro")
        self.inputRegistro.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputRegistro))
        self.inputRegistro.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputRegistro, "Inserir registro"))
        self.inputDataRegistro = Entry(abaPIA, width=10, state='disabled', fg='dark gray')
        self.inputDataRegistro.place(x=730,y=370)
        self.inputDataRegistro.insert(0, "Data da ocorrência:")
        self.inputDataRegistro.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputDataRegistro))
        self.inputDataRegistro.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputDataRegistro, "Data da ocorrência"))
        self.botaoRegistro = Button(abaPIA, text='Inserir registro', command=self.inserirRegistros)
        
        self.inputDataSaida = Entry(abaPIA, width=10, state='disabled', fg='dark gray')
        self.inputDataSaida.place(x=90, y=630)
        self.inputDataSaida.insert(0, "Data de saída")
        self.inputDataSaida.bind('<FocusIn>', lambda p:self.placeholder(self.inputDataSaida))
        self.inputDataSaida.bind('<FocusOut>', lambda p:self.estavazio(self.inputDataSaida, "Data de saída"))
        self.inputMotivoSaida = Entry(abaPIA, width=65, state='disabled', fg='dark gray')
        self.inputMotivoSaida.place(x=255, y=630)
        self.inputMotivoSaida.insert(0, "Motivo da saída")
        self.inputMotivoSaida.bind('<FocusIn>', lambda p:login.placeholder(self, self.inputMotivoSaida))
        self.inputMotivoSaida.bind('<FocusOut>', lambda p:login.estavazio(self, self.inputMotivoSaida, "Motivo da saída"))
        self.botaoMotivoSaida = Button(abaPIA, text='Registrar saída', command=self.registrarSaida)
        self.botaoGerarPdf = Button(abaPIA, text="Gerar PDF", command=self.gerarRelatorioAcolhimento)
####################EXIBE A ABA INTERNOS####################
        abaInternos.bind('<FocusIn>', lambda p: self.listarInternos())
        abaInternos.bind('<FocusOut>', lambda p: self.limparListaInternos())

login()