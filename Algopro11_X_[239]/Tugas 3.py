from tkinter import Tk, Label, Entry, Button, StringVar

my_app = Tk(className = "Menampilkan Data Diri")

J1 = Label(my_app, text = "Digit terakhir NIM", font=('Arial', 14))
J1.grid(row = 0, column = 0)

J2 = Label(my_app, text = "Tema", font=('Arial', 13))
J2.grid(row = 0, column = 1)

L1 = Label(my_app, text= 'angka 1')
L1.grid(row = 1, column = 0)
angka1 = StringVar()
E1 = Entry(my_app)
E1.grid(row = 1, column = 0)

L2 = Label(my_app, text= 'angka 2')
L2.grid(row = 2, column = 0)
angka2 = StringVar()
E2 = Entry(my_app)
E2.grid(row = 2, column = 0)

M1 = Label(my_app, text = "Prisma")
M1.grid(row = 1, sticky = 'w', column = 1)

def luas_prisma():
    x = float(angka1.get())
    y = float(angka2.get())
    alas = x*y
    tegak = x*y*4
    hasil = alas + tegak
    L.config(text=hasil)

    
my_app.mainloop()

