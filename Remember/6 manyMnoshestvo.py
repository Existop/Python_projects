numbers = {10, 4, 1, 20, 13, 123, 321, 495, 459, 241, 12, 12, 12}  # Нет дубликатов , все елементы уникальные .
print(numbers)         # пустое множество -- set ()--   numbers = set ([1,2,1,2,4])
for i in numbers:                       # используем ЦЫКЛ for  
    print( 10 in numbers)
numbers.add(58)  # добавить елемент в множества
numbers.discard(123)  # удалить елемент в множестве если не знаете если он вообще .ничего не выведет если его нету
numbers.remove(123)     # удалить елемент в множестве
numbers.pop (10) # удаляет всегда первый елемент нашего множества
numbers.clear # удаляет ВСЕ елементы


a= {1,3, 4, 10}
b= { 3, 4, 10, 12, 120}
c= a.union(b)  or  'c = a | b' or  '&' # Обьеденение множетса БЕЗ ДУБЛИКАТОВ . ЕЛЕменты СТРОГО Уникальны
print(c)


c = a - b # записать только те елементы которые есть только в А или Б 

c = a.copy()# копируем множество

print(len(numbers))# количество елементов

numbers4 = frozenset({10, 4, 1, 20, 13, 123, 321}) # ЗАМОРОЖЕННОЕ , нельзя добавить или хоть как-то изменять

