#Которая проверит равенство сумм и выведет "Счастливый", и "Обычный", если суммы различны.

#На вход программе подаётся строка из шести цифр.

#Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.

a,b,c,d,e,f = str(input())
if  int(a) + int(b) + int(c) == int(d) + int(e) + int(f):
    print('Счастливый')
elif int(a) + int(b) + int(c) != int(d) + int(e) + int(f):
    print('Обычный')