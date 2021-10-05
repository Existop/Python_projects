# На числовой прямой даны два отрезка D = [17;58] и С [29;80]

# Укажите найменьшую возможную длину такого отрезка А
# (x Э D) -> ((-(x Э С)/\ - (x Э А) -> -(x Э D))  истинно (т.е принимает значение 1)
def f (x,a1,a2):
    return (17 <= x <= 58) <= ((not(29 <= x <= 80) and not (a1 <= x < a2) <= (not(17 <= x <= 58)))

s = []
for a1 in range(-100, 100):
    for a2 in range(-100, 100):
        flag = True
        for x in range(-100, 100):
            id not(f(x,a1,a2)):
                flag = False
                break
        if flag:
            s.append(a2 - a1) # функция.append()  добавляет новый элемент в конец списка
print(min(s))                
