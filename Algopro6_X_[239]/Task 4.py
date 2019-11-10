Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Name = 'Kamila Narendragharini'
>>> NIM = 239
>>> Height = 1.61
>>> Weight = 53
>>> BornYear = 2001
>>> Me = (BornYear, Weight, Height, NIM, Name)
>>> Data = [BornYear, Weight, Height, NIM, Name]
>>> type(Me)
<class 'tuple'>
>>> #because 'Me' data consist of object chain and use parenthesis
>>> Me[0]
2001
>>> #because the first object in 'Me' data is 'BornYear', so the value is 2001
>>> a = NIM % 4; Me[a]
239
>>> #because the remaining result of 239 divided by 4 is 3, then the 3rd object in 'Me' data is 'NIM' then the value is 239
>>> type(Me[a])
<class 'int'>
>>> #the value of 'Me' is 3 and it goes to 'NIM' data, and 'NIM' data consist of just number that means its an Integer
>>> Me[a:4]
(239,)
>>> #because the 'Me' data refer to 'NIM' and 'NIM' is the last data in the first 4 object in the 'Me' data.
>>> type(Me[4])
<class 'str'>
>>> #the 4 in 'Me' gata refer to the last data in 'Me' and its a 'Name' data which consist of just character.
>>> Me[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Me[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #because Me[0] data type is an Integer and it doesn't support the 'ok' data
>>> type(Data)
<class 'list'>
>>> #because 'Data' data consist of object chain and use bracket
>>> type(Data[4])
<class 'str'>
>>> #the 4 in 'Data' gata refer to the last data in 'Data' and its a 'Name' data which consist of just character.
>>> Data[4][5]
'a'
>>> #data[4] means the 4th objecct in 'Data' data and that's 'Name' object, then the '[5]' means the 5th character from 'Name'
>>> Data[4][a:6]
'ila'
>>> #data[4] means the 4th object in 'Data' data and that's 'Name' object, then 'a' is 3 so it pointing out that [a:6] want teh program to represent the range from 3rd until 6th character in 'Name' data.
>>> Data[0] = 'ok'; Data
['ok', 53, 1.61, 239, 'Kamila Narendragharini']
>>> #means the 'BornYear' data getting replaced by 'ok' in 'Data' list.
>>> Data[-a]
1.61
>>> #means the program represent the 'Data' data from the last and 'a' = , so it comes to 'Height' data.
>>> range(a)
range(0, 3)
>>> #means range 3 is (0, 3)
