import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import Crypto_support

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran: return        
    try: Crypto_support.root.tk.call('source',
                os.path.join(_location, 'themes', 'default.tcl'))
    except: pass
    style = ttk.Style()
    style.theme_use('default')
    style.configure('.', font = "TkDefaultFont")
    if sys.platform == "win32":
       style.theme_use('winnative')    
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("800x640+290+108")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.combobox = tk.StringVar()

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Entry6 = tk.Entry(self.top)
        self.Entry6.place(relx=0.259, rely=1.023, height=50, relwidth=0.293)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="-family {Courier New} -size 10")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="#000000")
        self.Entry6.configure(insertbackground="#000000")
        self.Entry6.configure(selectbackground="#d9d9d9")
        self.Entry6.configure(selectforeground="black")

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.358, rely=0.772, height=26, width=97)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 9")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="#000000")
        self.Button2.configure(text='''Button''')

        self.Entry7 = tk.Entry(self.top)
        self.Entry7.place(relx=0.198, rely=0.834, height=50, relwidth=0.293)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="-family {Courier New} -size 10")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(highlightbackground="#d9d9d9")
        self.Entry7.configure(highlightcolor="#000000")
        self.Entry7.configure(insertbackground="#000000")
        self.Entry7.configure(selectbackground="#d9d9d9")
        self.Entry7.configure(selectforeground="black")

        self.Button4 = tk.Button(self.top)
        self.Button4.place(relx=0.025, rely=0.947, height=26, width=177)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="black")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Segoe UI} -size 9")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="#000000")
        self.Button4.configure(text='''Button''')

        self.Label7 = tk.Label(self.top)
        self.Label7.place(relx=0.038, rely=0.872, height=21, width=33)
        self.Label7.configure(activebackground="#d9d9d9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Segoe UI} -size 9")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="#000000")
        self.Label7.configure(text='''Label''')

        self.Label6 = tk.Label(self.top)
        self.Label6.place(relx=0.038, rely=0.722, height=21, width=33)
        self.Label6.configure(activebackground="#d9d9d9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Segoe UI} -size 9")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="#000000")
        self.Label6.configure(text='''Label''')

        _style_code()
        self.Scrolledtext1 = ScrolledText(self.top)
        self.Scrolledtext1.place(relx=0.013, rely=0.016, relheight=0.314
                , relwidth=0.978)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="#000000")
        self.Scrolledtext1.configure(insertbackground="#000000")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#d9d9d9")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.configure(wrap="none")

        self.Entry5 = tk.Entry(self.top)
        self.Entry5.place(relx=0.198, rely=0.669, height=50, relwidth=0.293)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="-family {Courier New} -size 10")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="#000000")
        self.Entry5.configure(insertbackground="#000000")
        self.Entry5.configure(selectbackground="#d9d9d9")
        self.Entry5.configure(selectforeground="black")

        self.Entry8 = tk.Entry(self.top)
        self.Entry8.place(relx=0.69, rely=0.669, height=50, relwidth=0.293)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="-family {Courier New} -size 10")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(highlightbackground="#d9d9d9")
        self.Entry8.configure(highlightcolor="#000000")
        self.Entry8.configure(insertbackground="#000000")
        self.Entry8.configure(selectbackground="#d9d9d9")
        self.Entry8.configure(selectforeground="black")

        self.Button5 = tk.Button(self.top)
        self.Button5.place(relx=0.85, rely=0.87, height=26, width=97)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="black")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font="-family {Segoe UI} -size 9")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="#000000")
        self.Button5.configure(text='''Button''')

        self.Entry9 = tk.Entry(self.top)
        self.Entry9.place(relx=0.69, rely=0.77, height=50, relwidth=0.293)
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font="-family {Courier New} -size 10")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(highlightbackground="#d9d9d9")
        self.Entry9.configure(highlightcolor="#000000")
        self.Entry9.configure(insertbackground="#000000")
        self.Entry9.configure(selectbackground="#d9d9d9")
        self.Entry9.configure(selectforeground="black")

        self.TSeparator4 = ttk.Separator(self.top)
        self.TSeparator4.place(relx=0.0, rely=0.93,  relwidth=0.996)

        self.Entry4 = tk.Entry(self.top)
        self.Entry4.place(relx=0.688, rely=0.563, height=30, relwidth=0.293)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="-family {Courier New} -size 10")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="#000000")
        self.Entry4.configure(insertbackground="#000000")
        self.Entry4.configure(selectbackground="#d9d9d9")
        self.Entry4.configure(selectforeground="black")

        self.Entry3 = tk.Entry(self.top)
        self.Entry3.place(relx=0.2, rely=0.563, height=30, relwidth=0.293)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="-family {Courier New} -size 10")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="#000000")
        self.Entry3.configure(insertbackground="#000000")
        self.Entry3.configure(selectbackground="#d9d9d9")
        self.Entry3.configure(selectforeground="black")

        self.Entry2 = tk.Entry(self.top)
        self.Entry2.place(relx=0.2, rely=0.5, height=30, relwidth=0.293)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Courier New} -size 10")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="#000000")
        self.Entry2.configure(insertbackground="#000000")
        self.Entry2.configure(selectbackground="#d9d9d9")
        self.Entry2.configure(selectforeground="black")

        self.Label4 = tk.Label(self.top)
        self.Label4.place(relx=0.038, rely=0.563, height=20, width=36)
        self.Label4.configure(activebackground="#d9d9d9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 9")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="#000000")
        self.Label4.configure(text='''Label''')

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.038, rely=0.516, height=20, width=36)
        self.Label3.configure(activebackground="#d9d9d9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 9")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="#000000")
        self.Label3.configure(text='''Label''')

        self.Button6 = tk.Button(self.top)
        self.Button6.place(relx=0.7, rely=0.516, height=26, width=97)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="black")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font="-family {Segoe UI} -size 9")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="#000000")
        self.Button6.configure(text='''Button''')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.85, rely=0.516, height=26, width=97)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 9")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''Button''')

        self.TSeparator3 = ttk.Separator(self.top)
        self.TSeparator3.place(relx=0.0, rely=0.614,  relwidth=0.998)

        self.TSeparator2 = ttk.Separator(self.top)
        self.TSeparator2.place(relx=0.0, rely=0.441,  relwidth=0.999)

        self.n = tk.Entry(self.top)
        self.n.place(relx=0.688, rely=0.391, height=30, relwidth=0.293)
        self.n.configure(background="white")
        self.n.configure(disabledforeground="#a3a3a3")
        self.n.configure(font="-family {Courier New} -size 10")
        self.n.configure(foreground="#000000")
        self.n.configure(highlightbackground="#d9d9d9")
        self.n.configure(highlightcolor="#000000")
        self.n.configure(insertbackground="#000000")
        self.n.configure(selectbackground="#d9d9d9")
        self.n.configure(selectforeground="black")

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.2, rely=0.391, height=30, relwidth=0.293)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 10")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="#000000")
        self.Entry1.configure(insertbackground="#000000")
        self.Entry1.configure(selectbackground="#d9d9d9")
        self.Entry1.configure(selectforeground="black")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.038, rely=0.406, height=20, width=73)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 9")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''Label''')

        self.TCombobox1 = ttk.Combobox(self.top)
        self.TCombobox1.place(relx=0.85, rely=0.336, relheight=0.045
                , relwidth=0.12)
        self.TCombobox1.configure(font="-family {Segoe UI} -size 9")
        self.TCombobox1.configure(textvariable=self.combobox)

        self.Button3 = tk.Button(self.top)
        self.Button3.place(relx=0.259, rely=0.947, height=26, width=177)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="black")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Segoe UI} -size 9")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="#000000")
        self.Button3.configure(text='''Button''')

        self.Button7 = tk.Button(self.top)
        self.Button7.place(relx=0.513, rely=0.947, height=26, width=177)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="black")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font="-family {Segoe UI} -size 9")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="#000000")
        self.Button7.configure(text='''Button''')

        self.Button8 = tk.Button(self.top)
        self.Button8.place(relx=0.75, rely=0.947, height=26, width=177)
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(activeforeground="black")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(font="-family {Segoe UI} -size 9")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="#000000")
        self.Button8.configure(text='''Button''')

        self.Label9 = tk.Label(self.top)
        self.Label9.place(relx=0.763, rely=0.344, height=21, width=36)
        self.Label9.configure(activebackground="#d9d9d9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(compound='left')
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Segoe UI} -size 9")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="#000000")
        self.Label9.configure(text='''Label''')

        self.Label8 = tk.Label(self.top)
        self.Label8.place(relx=0.038, rely=0.344, height=21, width=36)
        self.Label8.configure(activebackground="#d9d9d9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Segoe UI} -size 9")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="#000000")
        self.Label8.configure(text='''Label''')

        self.Label10 = tk.Label(self.top)
        self.Label10.place(relx=0.038, rely=0.453, height=21, width=36)
        self.Label10.configure(activebackground="#d9d9d9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(anchor='w')
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(compound='left')
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font="-family {Segoe UI} -size 9")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="#000000")
        self.Label10.configure(text='''Label''')

        self.Label11 = tk.Label(self.top)
        self.Label11.place(relx=0.038, rely=0.641, height=21, width=35)
        self.Label11.configure(activebackground="#d9d9d9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(anchor='w')
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(compound='left')
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(font="-family {Segoe UI} -size 9")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="#000000")
        self.Label11.configure(text='''Label''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.525, rely=0.406, height=20, width=73)
        self.Label2.configure(activebackground="#d9d9d9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 9")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="#000000")
        self.Label2.configure(text='''Label''')

        self.Label5 = tk.Label(self.top)
        self.Label5.place(relx=0.525, rely=0.563, height=21, width=36)
        self.Label5.configure(activebackground="#d9d9d9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 9")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="#000000")
        self.Label5.configure(text='''Label''')

        self.Label12 = tk.Label(self.top)
        self.Label12.place(relx=0.525, rely=0.641, height=21, width=34)
        self.Label12.configure(activebackground="#d9d9d9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(anchor='w')
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(compound='left')
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(font="-family {Segoe UI} -size 9")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="#000000")
        self.Label12.configure(text='''Label''')

        self.Label13 = tk.Label(self.top)
        self.Label13.place(relx=0.525, rely=0.797, height=21, width=36)
        self.Label13.configure(activebackground="#d9d9d9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(anchor='w')
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(compound='left')
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(font="-family {Segoe UI} -size 9")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(highlightbackground="#d9d9d9")
        self.Label13.configure(highlightcolor="#000000")
        self.Label13.configure(text='''Label''')

        self.Label14 = tk.Label(self.top)
        self.Label14.place(relx=0.525, rely=0.703, height=21, width=36)
        self.Label14.configure(activebackground="#d9d9d9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(anchor='w')
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(compound='left')
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(font="-family {Segoe UI} -size 9")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(highlightbackground="#d9d9d9")
        self.Label14.configure(highlightcolor="#000000")
        self.Label14.configure(text='''Label''')

        self.TSeparator1 = ttk.Separator(self.top)
        self.TSeparator1.place(relx=0.5, rely=0.611,  relheight=0.395)
        self.TSeparator1.configure(orient="vertical")

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    Crypto_support.main()

if __name__ == '__main__':
    Crypto_support.main()




