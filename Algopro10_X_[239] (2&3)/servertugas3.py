import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50008))
s.listen(5)
print "Server Siap"
perintah = ''
a=0
t=0
p=0
x=0.5
while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        item = komm.recv(1024).lower().split("=")
        perintah = item[0]
        if perintah == 'keluar':
            komm.send('done')
            s.close()
            break
        print "pesan:", perintah
        if len(item)==4:
            if perintah == 'alas':
                a=int(item[1])
                komm.send('alas disimpan')
            elif perintah == 'tinggi':
                t=int(item[1])
                komm.send('tinggi disiman')
            elif perintah == 'panjang':
                p=int(item[1])
                komm.send('panjang disimpan')
            elif perintah == 'xetengah':
                x=int(item[1])
                komm.send('xetengah disimpan')
            else:
                komm.send('pesan tidak diketahui')
        elif perintah == 'hitung':
            L=float(a*t*p*x)
            response = 'Luas prisma dengan alas {} tinggi {} panjang {} adalah {}'. format(a,t,p,x,L)
            komm.send(response)
        else:
            komm.send('Pesan tidak diketahui')
