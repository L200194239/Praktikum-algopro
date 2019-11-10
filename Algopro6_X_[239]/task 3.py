Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Name = 'Kamila Narendragharini'
>>> NIM = 'L200194239'
>>> x = '1' + NIM[7:]
>>> a = int(x)
>>> b = len(Name)
>>> type(a)
<class 'int'>
>>> # because the 'x' data had changed the integer data type
>>> type(b)
<class 'int'>
>>> # because the 'Name' data has a 'len' instruction
>>> a / b
56.31818181818182
>>> # because the result of 1239 divided by 22 is 56.31818181818182
>>> a // b
56
>>> # because the meaning of "//" is divided with rounding down, so the result is 56
>>> 10 * (a - 999)
2400
>>> # because the value of 'a' minus 999 is 240, after that it will multiple with 10 and got the result as 2400
>>> b ** 2
484
>>> # because the result of 'b' is 22, then the result of b will be lifted by 2 and got the result as 484
>>> a % b
7
>>> # the result of 'a' is 1239 then modulo with the result of 'b' where is the result of b is 22, and got the remainder calculation as 7
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #because the 'c' data has  a decimal number
>>> a / c
99.12
>>> #because the result of a is 1239 then divided by 12.5 and got the result 99.12
>>> a // c
99.0
>>> #because the value of a/c is 99.12 , then the value of a//c is 99.0. the meaning of '//' is divided with rounding down
>>> a % c
1.5
>>> #because '%' has a meaning as remainder calculation, so the remainder of calculation above is 1.5
>>> c > b
False
>>> # 'c' is 12.5 then 'b' is 22, means if 'c' greater than 'b' is wrong
>>> type(c > b)
<class 'bool'>
>>> # because the 'c > b' data type has a result 'false' then the type is boolean.
>>> a > b and b > c
True
>>> # 'a' is 1239 and 'b' is 22 means if 'a' greater than 'b' is true and 'b' is 22 and 'c' is 12.5 also means true if 'b' greater than 'c'
>>> a > 1100 or b < 10
True
>>> # 'a' is 1239 greater than 1100 = true and 'b' is 22 smaller than 10 = false, but here we use 'or' as the operator that means if 'True or False' means True
