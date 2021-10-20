def print_name_by_symbol(name):
    i = len(name) - 1
    while i >= 0:
        print(name[i])
        i = i - 1
print_name_by_symbol('name')


def print_name_by_symbol(name):
    i = 0
    # Такая проверка будет выполняться до конца строки
    # включая последний символ. Его индекс `length - 1`.
    while i < len(name):
        # Обращаемся к символу по индексу
        print(name[i])
        i = i + 1
name = '!!Arya'
print_name_by_symbol(name)
