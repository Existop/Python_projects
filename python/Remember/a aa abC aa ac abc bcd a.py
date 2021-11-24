#подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
s = input().lower().split()
for i in set(s):
    print(i, s.count(i))


d  = {e:0 for e in s} #создаем словарь на основе списка с 0 значениями
for key in s: d[key]+= 1 #тупо считаем повторяющиеся
for key,value in d.items(): print(key, value) #тупо выводим

    