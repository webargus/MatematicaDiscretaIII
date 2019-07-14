
"""
    UFRPE - BSI2019.1 - Matemática Discreta - Trabalho 2 - 2ª VA
    Dupla: Edson Kropniczki + Cristina Oliveira
    Descrição: GUI para executar o algoritmo de Dijkstra
"""

from tkinter import *
from tkinter import messagebox
import GraphCanvas


class GraphPanel:

    def __init__(self, frame):

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        wrap = Frame(frame)
        wrap.grid({"row": 0, "column": 0, "sticky": NSEW})
        wrap.grid_rowconfigure(2, weight=1)
        wrap.grid_columnconfigure(0, weight=1)

        header = Frame(wrap)
        header.grid({"row": 0, "column": 0, "sticky": NSEW})
        l1 = Label(header, {"text": "Cálculo do menor percurso pelo algoritmo de Dijkstra",
                            "font": ("Arial", 12),
                            "padx": 20,
                            "pady": 20})
        l1.grid({"row": 0, "column": 0})

        form = Frame(wrap, {"pady": 8, "padx": 8})
        form.grid({"row": 1, "column": 0, "sticky": NSEW, "pady": 8, "padx": 8})

        # result report labels
        self.path = Label(form)
        self.path.grid(row=0, column=0)
        self.result = Label(form)
        self.result.grid(row=1, column=0)

        # infos btn
        self.info_img = PhotoImage(file="info24.png")
        Button(form,
               image=self.info_img,
               width=24,
               height=24,
               command=self._infos).grid(row=2, column=0)

        canvasF = Frame(wrap, {"relief": SUNKEN, "border": 1})
        canvasF.grid({"pady": 8, "padx": 8, "row": 2, "column": 0, "sticky": NSEW})
        canvasF.grid_columnconfigure(0, weight=1)
        canvasF.grid_rowconfigure(0, weight=1)
        self.canvas = GraphCanvas.GraphCanvas(canvasF, self._do_dijkstra)

    def _do_dijkstra(self, sel, graph):
        for node in sel:
            print(node)
        for node in graph:
            print(node)

    def _infos(self):
        text = "Clique no painel em branco: cria novo vértice\n"
        text += "Clique em dois vértices em sequência: cria aresta\n"
        text += "Ctrl + clique em dois vértices em sequência: cálculo Dijkstra"
        messagebox.showinfo("Infos", text)










