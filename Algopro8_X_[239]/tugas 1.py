x = {"name":"kadra",
     "NIM":"L200194239",
     "address":"Klodran",
     "nationality":"Indonesian",
     "religion":"moslem",
     "born":"January28th",
     "year":"2001"}


def Nama():
    print(x["name"])
def Nomor():
    print(x["NIM"])
def Alamat():
    print(x["address"])
def Kewarganegaraan():
    print(x["nationality"])
def Agama():
    print(x["religion"])
def Lahir():
    print(x["born"])
def Tahun():
    print(x["year"])

def pilihan():
    ('''pilihan yang tersedia:
    a Nama
    b Nomor
    c Alamat
    d Kewarganegaraan
    e Agama
    f Lahir
    g Tahun ''')

pilihan()
a = input('pilihan anda:')
while a != 'z':
    if a == "a":
        Nama()
        a = input('pilihan anda:')
    elif a == "b":
        Nomor()
        a = input('pilihan anda:')
    elif a == "c":
        Alamat()
        a = input('pilihan anda:')
    elif a == "d":
        Kewarganegaraan()
        a = input('pilihan anda:')
    elif a == "e":
        Agama()
        a = input('pilihan anda:')
    elif a == "f":
        Lahir()
        a = input('pilihan anda:')
    elif a == "g":
        Tahun()
        a = input('pilihan anda:')
    elif a == "z":
        z()
        break
    else:
        print ('perintah tidak dikenal')
        a = input ('pilihan anda:')






    
