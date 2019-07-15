"""
    Description:
        Simple tkinter dlg to input edge length from user
    Author:
        Edson Kropniczki - (c) jul/2019 - all rights reserved
    License:
        just keep this header in your copy and feel free to mess up with this code as you wish;
        source code also publicly available at https://github.com/webargus/MatematicaDiscretaIII;
        actually, accretions and improvements are more than welcome! :)
    Disclaimer:
        No liabilities or warrants whatsoever granted, as usual. Use it on your own risk!
"""

from tkinter import *
from tkinter import messagebox
import Tools


class EdgeDistanceDlg:

    def __init__(self, parent, title, callback):

        self.top = Toplevel(parent, pady=10, padx=10)
        Tools.Tools.center_window(self.top, 200, 100)
        self.top.resizable(0, 0)
        self.top.state("normal")
        self.top.title(title)
        self.top.iconbitmap('brasao32.ico')
        self.top.protocol("WM_DELETE_WINDOW", self._close)      # cancel input
        Tools.Tools.master.wm_attributes("-disabled", True)     # disable top parent window
        self.top.after(500, lambda: self.top.focus_force())     # set focus after things settle
        self.top.transient(Tools.Tools.master)
        self.callback = callback                                # callback to return input to caller

        Label(self.top, text="Distância: ").grid(row=0, column=0, pady=8)

        self.e = Entry(self.top, width=5, text=1)
        self.e.grid(row=0, column=1, pady=8)

        b = Button(self.top, text="Cancelar", command=self._close, width=8)
        b.grid(row=1, column=0, padx=12, pady=12)

        b = Button(self.top, text="OK", command=self._ok, width=8)
        b.grid(row=1, column=1, padx=12, pady=12)

    def _close(self, dist=None):
        Tools.Tools.master.wm_attributes("-disabled", False)        # important! enable main window!
        self.top.destroy()
        self.callback(dist)             # return input to caller (None, if cancelled)

    def _ok(self):
        # validate user input
        try:
            dist = float(self.e.get())
            if dist <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Êpa!!", "Distância inválida\nEntre um número > 0")
            return
        self._close(dist)










