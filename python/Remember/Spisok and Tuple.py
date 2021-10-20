# list cписок  ['с', 'п', 'и', 'с', 'о', 'к']   Пустой список s = []  
# tuple -  Кортеж  ('h', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!')
fruit = ['Lemon', 'Apple', 'Pineapple']  # cписок
member = "james,  astom, Tonny, Galya"  
print(member.split(','))
print('_ -_'.join(fruit))
print('Привет, Peter!'.replace( 'Peter', 'Алекс'))
name = 'Валера'
print(min( [7,6,21,5,7,2] ))
print( abs ( -1000)) # абсолютное число , без знаков

if (name.lower().startswith('в') or name.lower().startswith('В')):
    print('Вася')
else:
    print('вася')

