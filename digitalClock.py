from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Digital Clock')
root.resizable(0, 0)
root.iconbitmap('./images/logo.ico')


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=('calibri', 40, 'bold'),
            background='#100720',
            foreground='white')

lbl.pack(anchor='center')
time()

root.mainloop()
