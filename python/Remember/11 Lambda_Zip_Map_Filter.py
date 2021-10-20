print((lambda a: a **2)(10))  
# Написать lambda-функцию, принимающую 1 аргумент — сторону квадрата, и возвращающую периметр квадрата.
print((lambda a,b,c: (a+b+c)/3) (5,5,5))
#Написать lambda-функцию, которая выводит среднее арифметическое 3 чисел.
a= filter(lambda x:(x % 2 == 0), (2,4,5,6,7,8,9,10))
print(list(a)) 
def d(a,b):
    return a*b
a = map(d, [2, 4, 5], [5, 6, 7])
print(list(a))

a  = map(lambda x: x + 15, (15, 25, 35))
print(list(a))

from functools import reduce
print(reduce(lambda a, b: a * b , (10, 2, 3)))

a=[1,4,6,9]
b= 'askif'
res = zip(a,b)
print(list(res))



with open('15Lesson.txt') as f:
    n = int(f.readline())     # Открили файл КАК ОБЬЕКТ Ф , считали первую одну строчку 
    for i in range(n):      # Берем каждую строчку построчно, МЕТОД сплит Разрезает  Строку по пробелам и возвращет строчный тип (str)
        a, b = map(int, f.readline().split())
        print(a*b)






