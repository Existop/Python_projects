a = int(input())          # 3 5 15
b = int(input())	  # 5 7 15
res = a
while res % b != 0:   
    res += a
print(res)
input()


#--------------------------------------------
#a=int(input())
#b=int(input())
#m=a
#if a==b:  			 # если оба значения (a и b) равны, выводим сразу это значение, и программа завершается.   
#  print(m)
          			 # иначе, при помощи цикла, прибавляем к одному из значений(a или b) его же значение,
#else:     			 # а+а+... или b+b+...до тех пор, пока сумма не будет кратной введенным значениям a и b 
#  while m%a!=0 or m%b!=0: 	# ТАКОЙ способ позволяет не прерывать цикл. Ниже пояснение.
#    m=m+a
#  print(m)


     # конструкция m%a!=0 or m%b!=0 - позволяет производить цикл до момента, когда оба условия одновременно
     # станут False. Потому что помним(!!!), что цикл While работает только когда условие в нем True, если 
     # становится False, то блок While перестает работать.