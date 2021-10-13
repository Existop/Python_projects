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

NS = 'Ama Ra42_394*&*&i93)23jsaf622216'
Fresult = re.search(r"T..a", NS) # место точек что-то
print(Fresult)

#\s любой первый пробел \S все кроме пробела
Fresult = re.search(r'\bRa', NS) # начало или конец слова
print(Fresult)
Fresult = re.search(r'[^4-6]', NS) # Что не входит в 4-6
print(Fresult)
Fresult = re.search(r'23j|6516', NS) # Что раньше найдет |ИЛИ
print(Fresult)
Fresult = re.search(r'\d{4,}', NS) # (4)подряд идущие цифры и больше
print(Fresult)

