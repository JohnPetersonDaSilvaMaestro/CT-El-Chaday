from tkinter import *
from PIL import Image, ImageTk
janela = Tk()
janela.geometry('350x200')

def sucesso(titulo, mensagem, mensagemBotao, icone):    
    window_height = 200
    window_width = 350
    janela.resizable(False, False)
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    janela.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    janela.config(bg='#77c600')
    janela.title(titulo)
    imagem = Image.open(icone).resize((50,50))
    icone = ImageTk.PhotoImage(imagem)
    Label(janela, image=icone).place(x=10, y=75)
    mensagem = Label(janela, text=mensagem)
    mensagem.config(background='#77c600', font=("Arial", 16, 'bold'))
    mensagem.place(x=70, y=85)
    botao = Button(janela, text = mensagemBotao, background="#709b2e", foreground="Black", width=10, height=1, command=janela.destroy)
    botao.place(x=250,y=150)
    janela.mainloop()

sucesso("Sucesso", "Deu tudo certo", "Que bom","sucesso.ico")