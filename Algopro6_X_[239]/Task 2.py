## Account Program
## Made by Kamila Narendragharini L200194239

import random
angka = random.randint(0,1000)

Name = 'Kamila Narendragharini'
BornDate = '28 Januari 2001'
Nickname = Name[0] + '. ' + Name[7] + '. ' + Name[15:22]
Username = Name[0] + BornDate[0:2] + BornDate[11:15]
Password = Name[0:3] + str(angka)
