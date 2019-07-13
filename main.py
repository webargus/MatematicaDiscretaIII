
"""
    UFRPE - BSI2019.1 - Matemática Discreta - Trabalho 2 - 2ª VA
    Dupla: Edson Kropniczki + Cristina Oliveira
    Descrição: Interface gráfica para o Trabalho 2
"""

from tkinter import *
from tkinter.ttk import *
import GraphCanvas


class Gui(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.iconbitmap("brasao32.ico")
        self.master.resizable(0, 0)
        self.master.geometry("1120x600")
        self.master.state('normal')
        self.master.title("Matemática Discreta - Trabalho 2 - SI2019.1")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.grid({"row": 0, "column": 0, "sticky": NSEW})
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.graph = GraphCanvas.GraphCanvas(self)

        self.mainloop()


if __name__ == '__main__':
    gui = Gui()






