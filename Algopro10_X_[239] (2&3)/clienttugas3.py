import socket

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50008))
print "Menghitung luas prisma"
while pesan.lower() != 'keluar':
    pesan = raw_input('pesan: ')
    s.send(pesan)
    if pesan.lower() == 'keluar':
        response = s.recv(1024)
        print 'Response:-'
        s.close()
        break
    elif pesan.lower() != 'keluar':
        response = s.recv(1024)
        print "Response:", response
s.close()
