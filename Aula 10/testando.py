#importei a biblioteca visual
from tkinter import *
from tkinter import ttk
#chamei uma variavel e atribuir o valor da biblioteca a ela

class janela_main():
    janela =Tk()

    #dei titulo a janela
    janela.title("Ola")

    #dei o tamanho da janela
    janela.geometry("1000x500")

    #grid é a linha e a coluna e entry entrada de dados
    Entry().grid(row=0,column=1)

    Entry(show="*").grid(row=1,column=1)
    #show é para esconder str por outras str

    Button(text="entrar").grid(row=2, column=1)


    janela.mainloop()