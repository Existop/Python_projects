#Идекс всех елементов на каком месте разположены
lst = [ 1, 8, 8, 2, 19, 123]
#lst = [int(i) for i in input().split()]
x = int(input())

for i in range(len(lst)):
    if x == lst[i]:
        print(i, end=' ')

if x not in lst:
    print('Отсутствует')
