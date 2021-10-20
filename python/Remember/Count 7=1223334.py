# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
s,a = [],int(input())
for i in range(1,a+1):
    s.extend([i]*i)
print(*s[:a])
