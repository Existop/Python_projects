# не добавляйте кода вне функции



def update_dictionary(d, key, value):
    if key in d: # если key есть в списке
        d[key].append(value) # к списку по ключу key добавляем переданное значение
        
    if key not in d and 2 * key in d: # если key нет в словаре и есть ключ 2*key
        d[2 * key].append(value) # к списку по ключу 2*key добавляем переданное значение
        
    if key not in d and 2*key not in d: # если key и 2*key нет в словаре
        d[2*key] = [value] # добавляем в словарь список, в котором хран. value с ключом 2*key

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                             