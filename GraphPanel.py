
"""
    UFRPE - BSI2019.1 - Matemática Discreta - Trabalho 2 - 2ª VA
    Dupla: Edson Kropniczki + Cristina Oliveira
    Descrição: GUI para executar o algoritmo de Dijkstra
"""

from tkinter import *
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
                            "font": ("Arial", 12)})
        l1.grid({"row": 0, "column": 0})

        form = Frame(wrap, {"pady": 8, "padx": 8})
        form.grid({"row": 1, "column": 0, "sticky": NSEW, "pady": 8, "padx": 8})
        form.grid_columnconfigure(0, weight=1)

        text = " Como usar:\n"
        text += " Criar vértice: clique na área em branco abaixo.\n"
        text += " Criar aresta: clique nos vértices que quer conectar.\n"
        text += " Dijkstra: clique no vértice inicial e no final \n\tcom a tecla CTRL pressionada."
        self.info_img = PhotoImage(file="info24.png")
        Label(form,
              relief=SUNKEN,
              text=text,
              font=("Arial, sans-serif", 10),
              image=self.info_img,
              compound=LEFT,
              justify=LEFT,
              anchor=W).grid(row=0, column=0, sticky=EW, pady=8, columnspan=2)

        # result report labels
        self.path = Label(form, anchor=W)
        self.path.grid(row=1, column=0, sticky=W)
        self.result = Label(form, anchor=W)
        self.result.grid(row=2, column=0, sticky=W)

        # clear btns
        self.reset = Button(form,
                            width=10,
                            command=self._reset_canvas,
                            text="Resetar grafo")
        self.reset.grid(row=1, column=1, sticky=E, pady=8)
        self.clear = Button(form,
                            width=10,
                            command=self._clear_canvas,
                            text="Excluir grafo")
        self.clear.grid(row=2, column=1, stick=E)
        # infos btn
        """self.info_img = PhotoImage(file="info24.png")
        Button(form,
               image=self.info_img,
               width=24,
               height=24,
               command=GraphPanel._infos,
               anchor=W).grid(row=2, column=0, sticky=W, pady=8)"""

        canvasF = Frame(wrap, {"relief": SUNKEN, "border": 1})
        canvasF.grid({"pady": 8, "padx": 8, "row": 2, "column": 0, "sticky": NSEW})
        canvasF.grid_columnconfigure(0, weight=1)
        canvasF.grid_rowconfigure(0, weight=1)
        # create graph canvas passing callback from Dijkstra calculation
        self.canvas = GraphCanvas.GraphCanvas(canvasF, self._do_dijkstra)

    def _do_dijkstra(self, sel, graph):
        dist, prev = graph.dijkstra(sel[0], sel[1])
        s, dist = graph.reverse_path(prev, sel[0], sel[1])
        if len(s) == 0:
            s = "Destino inacessível"
        else:
            # draw Dijkstra path here
            node_ids = [int(x) for x in s.split('->')]
            for i in range(len(node_ids) - 1):
                self.canvas.draw_path_edge(node_ids[i], node_ids[i+1])
        self.path.config(text=("Menor caminho: %s" % s))
        self.result.config(text=("Total percorrido: %.2f" % dist))

    def _reset_canvas(self):
        self.path.config(text="")
        self.result.config(text="")
        self.canvas.remove_tags()

    def _clear_canvas(self):
        self.path.config(text="")
        self.result.config(text="")
        self.canvas.clear()







