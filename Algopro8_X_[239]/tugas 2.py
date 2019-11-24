def TemperatureConvertion(c = 0, f = 32):
    "temperature convertion celcius and fahrenheit"
    if c != 0 and f == 32:
        f = float((c*9/5)+32)
        print('Temperature', c, 'celcius equals with', f, 'fahrenheit')
    elif f != 32 and c == 0:
        c = float((f-32)*5/9)
        print('Temperature', f, 'fahrenheit equals with', c, 'celcius')
    else:
        f = float((c*9/5)+32)
        print ('Temperature', c, 'celcius equals wth', f, 'fahrenheit')
