# Cчитаем вместе след число и предидущее
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




