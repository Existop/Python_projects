class House (): # описание дома 
    def __init__(self, street, number):  # Функуия / метод 
        # свойста дома    init - МЕТОД  или КОНСТРУКТОР КЛАССА
        self.street = street
        self.number = number #  self — это стандартное имя первого аргумента для методов объекта.
        self.age = 2         #self- Имя для аргумента, представляющего текущий объект класса.
    def build(self):        # street, number - параметры или значения
        print('Дом на улице ' + self.street + ' под номером ' + str(self.number) + ' построен.')
    def age_of_house(self, year):
        # возраст дома
        self.age += year
House1 = House("березняки", 20)  # house1,2  Об'экты на основе классов
House2 = House('позняки', 30)       # каждый об'экт является екземпляром класса
House123 = House('Осокор', 123)

class prospecthouse(House):  # дома на проспекте
    def __init__(self, prospect, number):
        super().__init__(self,number)   
        # суб клас , a House Cупер класс
        self.prospect = prospect
Prhouse = prospecthouse('Ленина', 5)
print(Prhouse.prospect)
print(House2.street)
House123.build()
House123.age_of_house(1)
print(House1.age)

