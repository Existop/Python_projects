a,b,c,d,e,f = str(input())
if  int(a) + int(b) + int(c) == int(d) + int(e) + int(f):
    print('Счастливый')
elif int(a) + int(b) + int(c) != int(d) + int(e) + int(f):
    print('Обычный')

lst = [int(i) for i in input().split()]
if lst[0] + lst[1]  == lst[5]:
    print('Счастливый')
else:
    print('Обычный') 