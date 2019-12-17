from tkinter import Tk, Label, Button

my_app = Tk(className = "Menampilkan Data Diri")

L1 = Label(my_app, text = "Data diri", font=('Arial', 24))
L1.grid(row = 0, sticky = 'w', column = 0)

L2 = Label(my_app, text = "Nama")
L2.grid(row = 1, sticky = 'w', column = 0)

E2 = Label(my_app, text = "Kamila Narendragharini" )
E2.grid(row = 1, sticky = 'w', column = 1)

L3 = Label(my_app, text = "NIM")
L3.grid(row = 2, sticky = 'w', column = 0)

E3 = Label(my_app, text = "L200194239")
E3.grid(row = 2, sticky = 'w', column = 1)

L4 = Label(my_app, text = "Buku Favorit")
L4.grid(row = 3, sticky = 'w', column = 0)

E4 = Label(my_app, text = "Interval")
E4.grid(row = 3, sticky = 'w', column = 1)

L5 = Label(my_app, text = "Idola di kalangan sahabat")
L5.grid(row = 4, sticky = 'w', column = 0)

E5 = Label(my_app, text = "Umar bin Khattab")
E5.grid(row = 4, sticky = 'w', column = 1)

L6 = Label(my_app, text = "Motto")
L6.grid(row = 5, sticky = 'w', column = 0)

E6 = Label(my_app, text = "The world is ugly, but I hope I never row to be someone who can no longer see the small beautiful things")
E6.grid(row = 5, sticky = 'w', column = 1)

def keluar():
    my_app.quit()

B = Button(my_app, text = "Tutup", command = keluar)
B.grid(row = 6, column = 1)

my_app.mainloop()

 
