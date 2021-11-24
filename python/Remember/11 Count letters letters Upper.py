text = 'acggtgttat'
text = text.lower()
g = text.count('g')
word = text.count('c')
L = len(text)
print((g + word) / L * 100)

a = 'aCggtGttat'
s1 = a.upper().count('G'.upper())
s2 = a.upper().count('c'.upper())
e = s1 + s2
print((e/len(a))*100)

genome = 'aCggtGttat'    # Вводимый геном
s = genome.lower ()      # Приводим к одному регистру, если вдруг ввели без его учета
g = s.count ('g')        # Считаем гуанин
c = s.count ('c')        # Считаем цитозин
a = g + c                # Считаем их общее кол-во
b = len (s)              # Считаем кол-во символов во всем геноме
K = (a / b) * 100        # Получаем результат
print (K)                # Собственно сам результат

s = 'aCggtGttat'
print((s.lower().count('g'.lower())+s.lower().count('c'.lower()))/len(s)*100)

g = 'aCggtGttat'
q = g.lower()
c = 0
for i in q:
    if i == 'g' or i == 'c':
        c += 1
print(c/len(q) * 100)