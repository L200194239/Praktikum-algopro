import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50008))
s.listen(5)
print "Program komunikasi tentang data diri"
data = ''
kamus = {'nama': 'Kamila Narendragharini',
         'NIM': 'L200194239',
         'angkatan': '19'}
while data.lower() != 'keluar':
    komm, addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)
        if data.lower() == 'keluar':
            print 'siap!!'
            s.close()
            break
        print 'Pertanyaan:', data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('pertanyaan anda tidak masuk akal')
