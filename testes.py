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
global listaPdf
banco = sqlite3.connect('ctelchadai.db')
cursor = banco.cursor()
chaveCriptografia = '&t&*_*_+)%&!*$+(@g*#)E$^A#+_$(#!$^%T_$!!+*!*&^!*)@@##&((_**)^$#@&#$V@(!e%#$%!)@_%!@_)*@!)^+#!@$+W#&+#%$%_d%)&@!^$^&)(*+!$)$%q*(#&))%^&#+$+@(!_)%%***%#E%**&^$@+))_%&&$)%+*)!@^)^$_c^%e^+@*%&+(@#*$*)&@+_($+$!#(G^)!$*&@_@)*)&@m@@&^*#!)_H+*&^)*()@(!)_(#_^$!(!(&&*%_)@E+)&^%!_#*@#&_^@&)!)+$%*@h@()+^!++(_^$%*#%!#)+@@)%$$_+&_@@@!()#^((#!+!$&))&%(!+&@)*))_^+^#+$)_(*(_+#%)^!_)_*%*)@)+_)&+%K$@#!!@__+$*(+_($(&$$)^+%^*)!!&$!&_+_^J)!@)#^()$)_#^!$%^^()^#$_$L$%^(_**)$@(@J!_+!&)$@@)#%*!%@^!+$*($)_$*++)_@#!&___!_#($^@))*$&@(&k(^!$+#*#__!l+_)M$!!)+^_#'
def gerarRelatorio():
    cpf = "080.393.050-04"
    dadosInterno = cursor.execute("SELECT nome, cpf, fichaInscricao FROM internos")
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
        listaPdf = []
        listaPdf.append('Ficha.pdf')
    gerarPdfMedicamentos()

def gerarPdfMedicamentos():
    nome = ''
    cpf = "080.393.050-04"
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
    cursor.execute("SELECT id, cpf, nome, medicamento, medico, receita FROM medicamento")
    n = 0
    for i in cursor.fetchall():                
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
    gerarPdfRegistros()

def gerarPdfRegistros():
    cpf = "080.393.050-04"
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
    dadosMedicacao = cursor.execute("SELECT cpf, nome, ocorrencia, dataOcorrencia, registradoPor FROM ocorrencias")        
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
    gerarPdfVisitas()

def gerarPdfVisitas():
    cpf = "080.393.050-04"
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
    dadosMedicacao = cursor.execute("SELECT cpf, visitado, visitante, parentesco, dataVisita FROM visitas")
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
    mesclarPdf()

def mesclarPdf():
    global nomeAcolhido
    listaPdf = ['Ficha.pdf', 'medicamentos.pdf', 'ocorrencias.pdf', 'visitas.pdf']
    merger = PdfMerger()
    for pdf in listaPdf:
        merger.append(pdf)        
    merger.write('Ficha cadastral de ' + nomeAcolhido + '.pdf')
    merger.close()
    subprocess.Popen(['Ficha cadastral de ' + nomeAcolhido + '.pdf'], shell=True)