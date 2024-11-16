import tkinter as tk
from tkinter import *

top= Tk()

top.geometry("700x500")
answer = Text(width=35,height=2)
answer.place(x=100,y=75)

def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)
        elif x=="Clear":
             answer.delete('0.0', END)
        else:
            answer.insert(tk.INSERT, x)
    except:
        answer.insert(tk.INSERT, '')

B1 = Button(top, text="1", width=8, height=5, command=lambda: show("1"))
B1.place(x=100, y=115)
B2 = Button(top, text="2", width=8, height=5, command=lambda: show("2"))
B2.place(x=200, y=115)
B3 = Button(top, text="3", width=8, height=5, command=lambda: show("3"))
B3.place(x=300, y=115)
B4 = Button(top, text="+", width=8, height=5, command=lambda: show("+"))
B4.place(x=400, y=115)

B1 = Button(top, text="3", width=8, height=5, command=lambda: show("4"))
B1.place(x=100, y=200)
B2 = Button(top, text="4", width=8, height=5, command=lambda: show("5"))
B2.place(x=200, y=200)
B3 = Button(top, text="5", width=8, height=5, command=lambda: show("6"))
B3.place(x=300, y=200)
B1 = Button(top, text="-", width=8, height=5, command=lambda: show("-"))
B1.place(x=400, y=200)

B1 = Button(top, text="7", width=8, height=5, command=lambda: show("7"))
B1.place(x=100, y=285)
B2 = Button(top, text="8", width=8, height=5, command=lambda: show("8"))
B2.place(x=200, y=285)
B3 = Button(top, text="9", width=8, height=5, command=lambda: show("9"))
B3.place(x=300, y=285)
B4 = Button(top, text="X", width=8, height=5, command=lambda: show("*"))
B4.place(x=400, y=285)


B2 = Button(top, text="0", width=8, height=5, command=lambda: show("0"))
B2.place(x=200, y=375)
B1 = Button(top, text="=", width=8, height=5, command=lambda: show("="))
B1.place(x=100, y=375)
B3 = Button(top, text="Clear", width=8, height=5, command=lambda: show("Clear"))
B3.place(x=300, y=375)
B4 = Button(top, text="/", width=8, height=5, command=lambda: show("/"))
B4.place(x=400, y=375)
top.mainloop()
