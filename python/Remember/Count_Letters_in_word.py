def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index] == char.upper() or string[index] == char.lower():
            count = count + 1
        index = index + 1
    return count
print(count_chars('HeEEexlEtewes', 'e'))


def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index] == char:
            # Считаем только подходящие символы
            count = count + 1
        # Счётчик увеличивается в любом случае
        index = index + 1
    return count
print(count_chars('eepe swordsE.', 'e'))  # 4
print(count_chars('1231231231523123', '5'))