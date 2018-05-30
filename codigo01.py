from tkinter import *

class Application:
    def __init__(self, master=None):
        #---------------------------------------------------
        #               Definição dos Widgets
        #---------------------------------------------------
        self.lbtitulo = Label()
        self.lbtitulo["text"] = "Quem é a pessoa da figura?"
        self.lbtitulo["font"] = ("Verdana", "16", "bold")
        self.lbtitulo.pack()

        self.lbimagem = Label()
        self.lbimagem.img = PhotoImage(file="imgs/gracehopper.png")
        self.lbimagem["image"] = self.lbimagem.img        
        self.lbimagem.pack()

        self.bt1 = Button()
        self.bt1["text"] = "Grace Hopper"
        self.bt1["font"] = ("Verdana", "10")
        self.bt1.pack()

        self.bt2 = Button()
        self.bt2["text"] = "Margaret Hamilton"
        self.bt2["font"] = ("Verdana", "10")
        self.bt2.pack()        

        self.btavancar = Button()
        self.btavancar["font"] = ("Verdana", "10", "bold")
        self.btavancar.pack()

    
root = Tk()
root.title("Jogo de Perguntas e Respostas")
root.geometry("400x400")
Application(root) 
root.mainloop()
