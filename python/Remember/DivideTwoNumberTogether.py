# Два числа делятся на одно самое бдижайшее
a = int(input())      # 3 5 15
b = int(input())	  # 5 7 15
res = a
while res % b != 0:   
    res += a
print(res)
