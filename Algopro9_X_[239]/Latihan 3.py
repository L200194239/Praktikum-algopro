x = open("latihan1.txt", "r")
NIM = x.readline()
Lahir = x.readline()
Kota = x.readline()
Nama = x.readline()
x.close()

import shelve

x = shelve.open("Dra.txt")
x["data"] = [Nama, Lahir, Kota, NIM]
x.close()
