figure = str(input())
if figure == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) /2 #полупериметр
    print ( (p*(p - a) * (p - b) * (p - c)) ** 0.5)  #формула герона 
    #Нужны дополнительные скобки, т.к. возведение в степень приоретернее умножения!
elif figure == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)
elif figure == 'круг':
    r = float(input())
    pi = 3.14
    print(pi * r ** 2) #скобки дополнительные не нужны, т.к. возведение в степень приоретернее умножения
