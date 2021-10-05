import re  # регулярные выражения
s = 'ac/I wanna be a/ Supermanc/d1111c/dc'
result = re.match("ac",s) # Что ищу и в какой строке В НАЧАЛЕ СТРОКИ
print(result)
result = re.search('c/', s) # Первый который встретится
print(result[0],result) 

result = re.findall('a', s) # в Строчку все елементы
print(result)

result = re.split("/", s) # Розбивает по выбраному символу
print(result)

result = re.split("/", s , maxsplit= 2) 
print(result)

result = re.sub('c', 'a', s) # Замена всех символов на "А" в строке S
print(result)
