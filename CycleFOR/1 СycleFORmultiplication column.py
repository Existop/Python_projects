a=2
b=5
c=11
d=13                            #ввод данных,построчно, 4 числа
for y in range(c,d+1):          #цикл для верхней части таблицы
    print ('\t',y,end='')       #пробел,число, конец строки
for x in range (a,b+1):         #цикл для левого столбца
    print ('')                  #печатаем "ничего" для пресечения действия "end" в 11 строке 
    print (x,end='')            #печатаем х, строка будет продолжатся
    for y in range (c,d+1):     #цикл для переменной на которую будем перемножать х
        print ('\t',x*y, end='')#печать таб,произведение,продолжение в той же строке.


a =int (input())
b =int (input())
c =int (input())
d =int (input())
for g in range (c,d+1):
    print('\t'+str(g),end='')
print(end='\n')
for i in range (a,b+1):
    print(str(i)+'\t',end='')
    for j in range (c,d+1):
        print(str(i*j),end='\t')
    print(end='\n')       