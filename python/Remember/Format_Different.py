name = 'Джес'
age = 23
print( 'Privet, ' + str(name) + '! Тебе уже ' + str(age) + ' года!' )
print('Privet, %s! \nТебе уже %d год!' % (name, age))  #%прейсхолдер  s-cтрока  d-число f-дробь 
human = {
  'name': 'Jesia',
  'age': 21}
print('Имя: {person[name]}\nВозраст: {person[age]}'.format(person = human ) ) 
input = 'Jessi'
print('{0:_^15}'.format(input))   # после двуеточия пишем Символ Заполнитель  , Направление заполнения  ^-центр  < jes***  > ***jec
print( 'Привет, {0}!\nТебе уже {1} год!'.format( name, age)) # и количество знако мест 
print ( '{0}{1}{0}'.format('пон', '123'))
leng = 30
if (len(input) % 2):
    leng += 1
print( ('{0:*^'+str(leng)+'}').format( input) )

