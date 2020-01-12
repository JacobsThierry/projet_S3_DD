
import sys
import tkinter as tk
import tkinter.ttk as ttk

def set_Tk_var():
    global combobox
    combobox = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import Interface
    Interface.vp_start_gui()




