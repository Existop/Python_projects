number = [int(i) for i in input().split()]
result = []
if len(number) == 1:
    result += [number[0]]
else:
    for i in range(len(number)):
        if not i == len(number) -1:
            result += [number[i +1] + number[i -1]]
        else:
            result += [number[0] + number[i - 1]]
print(result)


a = [int(i) for i in input().split()]   #вводим строку
if len(a) == 1:    # рассмотрение списка из одного символа              
    print(*a)      # звездочка для вывода строки, а не списка
elif len(a) == 2:  # рассмотрение списка из двух символов
    print(a[1] * 2, a[0] * 2)
else:     # рассмотрение списка из более, чем двух символов    
    i = 0 
    while i < len(a):  # создание цикла 
        if i == 0:     # отдельная итерация для первого символа
            print(a[i + 1] + a[-1], end=" ")
            i += 1
        elif i == len(a) - 1:   # отдельная итерация для последнего символа
            print(a[i - 1] + a[0], end=" ")
            i += 1
        else:         # промежуточные значения списка
            print(a[i - 1] + a[i + 1], end=" ")
            i += 1
