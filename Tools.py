"""
    Description:
        Static reference to main window, including method to center window on screen
    Author:
        Edson Kropniczki - (c) jul/2019 - all rights reserved
    License:
        just keep this header in your copy and feel free to mess up with this code as you wish;
        source code also publicly available at https://github.com/webargus/MatematicaDiscretaIII;
        actually, accretions and improvements are more than welcome! :)
    Disclaimer:
        Use it at your own risk!
"""


class Tools:

    master = None                # static member to retrieve reference to root window
    _screen_width = None
    _screen_height = None

    @staticmethod
    def root(win):
        Tools.master = win
        Tools._screen_width = win.winfo_screenwidth()
        Tools._screen_height = win.winfo_screenheight()

    # center window on client view
    @staticmethod
    def center_window(win, width, height):
        # call update_idletasks before retrieving any geometry,
        # to ensure that the values returned are accurate
        win.update_idletasks()
        x = (Tools._screen_width // 2) - (width // 2)
        y = (Tools._screen_height // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))








