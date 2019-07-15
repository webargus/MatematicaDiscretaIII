
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
        form.grid_columnconfigure(0, weight=1)

        # result report labels
        self.path = Label(form, anchor=W)
        self.path.grid(row=0, column=0, sticky=W)
        self.result = Label(form, anchor=W)
        self.result.grid(row=1, column=0, sticky=W)

        # clear btns
        self.reset = Button(form,
                            width=14,
                            command=self._reset_canvas,
                            text="Resetar grafo")
        self.reset.grid(row=0, column=1, sticky=E, pady=8)
        self.clear = Button(form,
                            width=14,
                            command=self._clear_canvas,
                            text="Excluir grafo")
        self.clear.grid(row=1, column=1, stick=E)

        # infos btn
        self.info_img = PhotoImage(file="info24.png")
        Button(form,
               image=self.info_img,
               width=24,
               height=24,
               command=GraphPanel._infos,
               anchor=W).grid(row=2, column=0, sticky=W, pady=8)

        canvasF = Frame(wrap, {"relief": SUNKEN, "border": 1})
        canvasF.grid({"pady": 8, "padx": 8, "row": 2, "column": 0, "sticky": NSEW})
        canvasF.grid_columnconfigure(0, weight=1)
        canvasF.grid_rowconfigure(0, weight=1)
        self.canvas = GraphCanvas.GraphCanvas(canvasF, self._do_dijkstra)

    def _do_dijkstra(self, sel, graph):
        dist, prev = graph.dijkstra(sel[0], sel[1])
        s, dist = graph.reverse_path(prev, sel[0], sel[1])
        if len(s) == 0:
            s = "Destino inacessível"
        self.path.config(text=("Menor caminho: %s" % s))
        self.result.config(text=("Total percorrido: %.2f" % dist))

    @staticmethod               # user guide msg
    def _infos():
        text = "Clique no painel em branco: cria novo vértice\n"
        text += "Clique em dois vértices em sequência: cria aresta\n"
        text += "Ctrl + clique em dois vértices em sequência: cálculo Dijkstra"
        messagebox.showinfo("Infos", text)

    def _reset_canvas(self):
        self.path.config(text="")
        self.result.config(text="")
        self.canvas.remove_tags()

    def _clear_canvas(self):
        self.path.config(text="")
        self.result.config(text="")
        self.canvas.clear()







