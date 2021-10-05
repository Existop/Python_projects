#на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки 
# сначала максимальное, потом минимальное, после чего оставшееся число.
#На ввод могут подаваться и повторяющиеся числа.
x = int(input())
y = int(input())
z = int(input())
a = min(x, y, z)   #наименьшее число
b = max(x, y, z)   #наибольшее число
last = x + y + z - a - b  #вычитаем из суммы всех чисел наибольшее и наименьшее и находим оставшееся
print(b)
print(a)
print(last)

"""
if x >= y >= z:
	print(x)
	print(z)
	print(y) 
elif x >= z >= y:
	print(x)
	print(y)
	print(z)
elif y >= z >= x:
	print(y)
	print(x)
	print(z) 
elif y >= x >= z:
	print(y)
	print(z)
	print(x)
elif z >= x >= y:
	print(z)
	print(y)
	print(x) 
elif z >= y >= x:
	print(z)
	print(x)
	print(y) """