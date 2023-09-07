class Stadium:

    def __init__(self, name, year, country, city, capacity):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.capacity = capacity
    
    def view_all(self):
        print(f'Название - {self.name}\n'
            f'Год открытия стадиона - {self.year} г.\n'
            f'Страна - {self.country}\n'
            f'Город - {self.city}\n'
            f'Вместимость - {self.capacity} чел.')
            
    def view_name(self):
        print(f'Название - {self.name}')

    def view_year(self):
        print(f'Год открытия стадиона - {self.year} г.')
        
    def view_country(self):
        print(f'Страна - {self.country}')

    def view_city(self):
        print(f'Город - {self.city}')

    def view_capacity(self):
        print(f'Вместимость - {self.capacity} чел.')


check = True

try:
    print()
    print(' Заполните все поля! '.center(50,'*'))
    print()
    name = input('Введите название стадиона: ')
    year = int(input('Введите год открытия стадиона: '))
    country = input('Введите название страны: ')
    city = input('Введите название города: ')
    capacity = int(input('Введите вместимость стадиона: '))
    if len(name) > 0 and len(country) > 0 and len(city) > 0:
        my_stadium = Stadium(name, year, country, city, capacity)
    else:
        check = False
        print('Все поля обязательны, для заполнения!')
except ValueError:
    check = False
    print('Неправильнный ввод, попробуйте еще раз!')

if check:
    while True:
        try:
            print()
            print('1.Вывести все данные\n2.Вывести название стадиона\n3.Вывести'
                  ' год открытия стадиона\n4.Вывести название страны\n5.Вывести'
                  ' название города\n6.Вывести вместимость стадиона\n0.Выход')
            choice = int(input('Выберите необходимое действие: '))
            if choice == 0:
                break
            elif choice == 1:
                print()
                my_stadium.view_all()
            elif choice == 2:
                print()
                my_stadium.view_name()
            elif choice == 3:
                print()
                my_stadium.view_year()
            elif choice == 4:
                print()
                my_stadium.view_country()
            elif choice == 5:
                print()
                my_stadium.view_city()
            elif choice == 6:
                print()
                my_stadium.view_capacity()
            else:
                print('Число должно быть от 0 до 6')
        except ValueError:
            print('Введите число!')
