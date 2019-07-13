
from tkinter import *
from tkinter import messagebox
import tools


class EdgeDistanceDlg:

    def __init__(self, parent, callback):

        self.top = Toplevel(parent, pady=10, padx=10)
        self.top.resizable(0, 0)
        self.top.state("normal")
        self.top.geometry('220x70')
        self.top.title("Aresta")
        self.top.iconbitmap('brasao32.ico')
        self.top.protocol("WM_DELETE_WINDOW", lambda: None)
        self.parent = parent
        self.parent.master.master.wm_attributes("-disabled", True)
        self.top.after(500, lambda: self.top.focus_force())
        self.top.transient(parent.master.master)
        self.callback = callback

        Label(self.top, text="Distância: ").grid(row=0, column=0)

        self.e = Entry(self.top, width=5, text=1)
        self.e.grid(row=0, column=1)

        b = Button(self.top, text="OK", command=self._ok, width=10)
        b.grid(row=0, column=2, padx=5)

        tools.center_window(self.top)

    def _ok(self):
        # validate user input
        try:
            if int(self.e.get()) < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Êpa!!", "Distância inválida")
            return
        self.parent.master.master.wm_attributes("-disabled", False)
        self.top.destroy()
        self.callback()











