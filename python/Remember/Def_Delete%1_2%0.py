#Напишите функцию modify_list(l), удаляет из него все нечётные значения, а чётные нацело делит на два.


def modify_list(l):
    le = len(l) -1
    i = le
    while i != -1:
        if l[i]% 2:
            del l[i]
        else:
            l[i]=l[i] // 2
        i -=1
    return
f = [1, 10, 3, 4, 5, 20]
print(f)
modify_list(f)
print(f)

def modify_list(l):                    #Создаем новый список
    for x in l:                #Пробегаем все значения нового списка
        if x%2>0:              #Условие нечетности
            l.remove(x)        # неустраивающее нас значение

    for i in range(len(l)):    #Делим оставшиешя значение нацело на 2
        l[i]=l[i]//2


print(f)
print(modify_list(f))
print(f)
modify_list(f)



