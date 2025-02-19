from tkinter import *
from Diagrammid import *
global värv
def värvi_valik():
    värv="white"
    if tekst.get()!="":
        värv=tekst.get()
    else:
        tekst.configure(bg="red")
    return värv


def figuur(värv:str):
    valik=var.get()
    if valik==1:
        Vala(värv)
    elif valik==2:
        Vihmavari(värv)
    else:
        Prillid()
        print("Joonista hiljem")



aken = Tk()
aken.geometry("800x400")
aken.title("Garaafikud")

pealkiri = Label(aken, text="Erinevad piltid Matplotlib abil", font=("Calibri", 24),
                 fg="green", bg="yellow", pady=20, width=200)
var=IntVar()
r1=Radiobutton(aken,text="Vala",font="Calibri 18", variable=var,value=1,command=figuur)
r2=Radiobutton(aken,text="Vihmavari",font="Calibri 18", variable=var,value=2,command=figuur)
r3=Radiobutton(aken,text="Vihmavari",font="Calibri 18", variable=var,value=3,command=figuur)
tekst=Entry(aken,font="Calibri 24",fg="green",bg="yellow",width=50)
nupp=Button(aken, text="Värvi valik",font="Calibri 24", command=värvi_valik)

pealkiri.pack()
tekst.pack()
nupp.pack()
r1.pack()
r2.pack()
r3.pack()
aken.mainloop()
