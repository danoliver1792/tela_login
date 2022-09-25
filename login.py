from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

# Cores da tela:
colorOne = '#f0f3f5' # Preto
colorTwo = '#feffff' # Branco
colorThree = '#ff6600' # Laranja
colorFour = '#38576b' # Valor
colorFive = '#403d3d' # Letras

# Criação da janela
window = Tk()
window.title('') # Título
window.geometry('310x300') # Largura x comprimento
window.configure(background=colorThree) #Cor da tela será branca
window.resizable(width=FALSE, height=FALSE) # A janela não será alterada

# Dividindo a janela
frame_up = Frame(window, width=310, height=50, bg=colorTwo, relief='flat')
# Em janela: largura, altura, background, estilo

frame_up.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
# Divisão: linha, coluna, espaço, ..., posicão


frame_down = Frame(window, width=310, height=250, bg=colorTwo, relief='flat')
frame_down.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


# Configurando o frame_up
l_name = Label(frame_up, text='Login', anchor=NE, font=('Ivy 25'), bg=colorTwo, fg=colorFive) # Texto de login
l_name.place(x=5, y=5) # Posicionando a palavra Login

l_row = Label(frame_up, text='', width=275, anchor=NW, font=('Ivy 1'), fg=colorFive)
l_row.place(x=10, y=45)

# Dados
credentials = ['danrlei', '1234']

# Função que irá verificar se o usuário existe
def verificationPassword():
    nomeUser = e_name.get()
    passUser = e_pass.get()
    
    if nomeUser == 'admin' and passUser == 'admin':
        messagebox.showinfo('Login', 'Seja Bem-vindo Admin!')
    elif credentials[0] == nomeUser and credentials[1] == passUser:
        messagebox.showinfo('Login', 'Seja Bem-vindo ' + credentials[0])
    else:
        messagebox.showwarning('Erro!', 'Verifique seu usuário e senha')
        
# Configurando o frame_down
l_name = Label(frame_down, text='Nome *', anchor=NW, font=('Ivy 10'), bg=colorTwo, fg=colorFive)
l_name.place(x=10, y=20)

# Criando campo de preenchimento para 'nome'
e_name = Entry(frame_down, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
e_name.place(x=14, y=50)

# Criando campo de preenchimento para 'senha'
l_pass = Label(frame_down, text='Senha *', anchor=NW, font=('Ivy 10'), bg=colorTwo, fg=colorFive)
l_pass.place(x=10, y=95)

e_pass = Entry(frame_down, width=25, justify='left', show='*', font=('', 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=130)

#criando botão de 'entrar'
b_submit = Button(frame_down, command=verificationPassword, text='Entrar', width=39, height=2, font=('Ivy 8 bold'), bg=colorThree, fg=colorTwo, relief=RAISED, overrelief=RIDGE)
b_submit.place(x=15, y=180)


window.mainloop() # Chamando o menu