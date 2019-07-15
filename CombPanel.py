"""
    UFRPE - BSI2019.1 - Matemática Discreta - Trabalho 2 - 2ª VA
    Dupla: Edson Kropniczki + Cristina Oliveira
    Descrição: Gui para cálculo de combinação (Comb.py)
"""


from tkinter import *
from tkinter import messagebox
import ScrollableText
import Comb


class CombPanel:

    def __init__(self, frame):

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        wrap = Frame(frame)
        wrap.grid({"row": 0, "column": 0, "sticky": NSEW})
        wrap.grid_rowconfigure(2, weight=1)
        wrap.grid_columnconfigure(0, weight=1)

        header = Frame(wrap)
        header.grid({"row": 0, "column": 0, "sticky": NSEW})
        l1 = Label(header, {"text": "Entre os valores para n e k:",
                            "font": ("Arial", 12),
                            "padx": 20,
                            "pady": 20})
        l1.grid({"row": 0, "column": 0})

        form = Frame(wrap, {"pady": 8, "padx": 8})
        form.grid({"row": 1, "column": 0, "sticky": NSEW, "pady": 8, "padx": 8})

        # label and entry to input n
        Label(form, {"text": "n: ",
                     "font": ("Arial", 12)}).grid({"row": 0, "column": 0})
        self.n = StringVar()
        Entry(form, {"textvariable": self.n}).grid({"row": 0, "column": 1})

        # label and entry to input k
        Label(form, {"text": "k: ",
                     "font": ("Arial", 12)}).grid({"row": 0, "column": 2})
        self.k = StringVar()
        Entry(form, {"textvariable": self.k}).grid({"row": 0, "column": 3})

        # submit button
        params = {"text": "Ok",
                  "width": 5,
                  "font": ("Arial", 10),
                  "command": self._submit_form
                  }
        Button(form, params).grid({"row": 0, "column": 4, "padx": 4, "pady": 8, "sticky": W})

        text = Frame(wrap, {"pady": 8, "padx": 8})
        text.grid({"row": 2, "column": 0, "sticky": NSEW})
        text.grid_columnconfigure(0, weight=1)
        text.grid_rowconfigure(0, weight=1)
        self.text = ScrollableText.ScrollableText(text)

    def _submit_form(self):
        n = self.n.get()
        k = self.k.get()
        try:
            n, k = [int(v) for v in (n, k)]
            if n < k:
                raise ValueError
        except ValueError:
            messagebox.showerror("Êpa!!",
                                 "Entrada inválida!\nEntre somente inteiros positivos com n > k.")
            return

        result = Comb.comb(n, k)
        self.text.append_text("C(%d, %d) = %d\n" % (n, k, result))




