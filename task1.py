from accessify import private

class Car:

    def __init__(self, model, year, manufacturer, capacity, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.capacity = capacity
        self.color = color
        self.price = price
        self.congratulation = False
    
    @private
    def __checked(self, is_digital, inp):
        if is_digital:
            if inp.isdigit():
                return True
            else:
                return False
        else:
            if len(inp) > 0:
                return True
            else:
                return False

    def inp(self):
        while True:
            if self.congratulation:
                print('Успешно!'.center(50,'*'))
            self.congratulation = False
            try:
                print('1. Модель\n2. Год выпуска\n3. Производитель\n4. Объем '
                    'двигателя\n5. Цвет\n6. Цена\n0. Выход')
                choice = int(input('Выберите какие данные вы хотите '
                                   'редактировать: '))
                if choice == 0:
                    break

                if choice == 1:
                    model_inp = input('Введите название модели: ')
                    check = self.__checked(False, model_inp)
                    if check:
                        self.model = model_inp
                        self.congratulation = True
                    else:
                        print('\nВы ничего не ввели! Название модели не было '
                            'изменено!\n')
                if choice == 2:
                    year_inp = input('Введите год автомобиля: ')
                    check = self.__checked(True, year_inp)
                    if check:
                        self.year = int(year_inp)
                        self.congratulation = True
                    else:
                        print('Необходимо ввести число!'.center(50,'*'))

                if choice == 3:
                    manufacturer_inp = input('Введите название производителя: ')
                    check = self.__checked(False, manufacturer_inp)
                    if check:
                        self.manufacturer = manufacturer_inp
                        self.congratulation = True
                    else:
                        print('\nВы ничего не ввели! Название производителя не '
                              'было изменено!\n')
                if choice == 4:
                    try:
                        capacity_inp = float(input('Введите объем двигателя: '))
                        self.capacity = capacity_inp
                        self.congratulation = True
                    except ValueError:
                        print('Необходимо ввести число!'.center(50,'*'))
                if choice == 5:
                    color_inp = input('Введите цвет: ')
                    check = self.__checked(False, color_inp)
                    if check:
                        self.color = color_inp
                        self.congratulation = True
                    else:
                        print('\nВы ничего не ввели! Цвет не был изменен!\n')
                if choice == 6:
                    price_inp = input('Введите цену: ')
                    check = self.__checked(True, price_inp)
                    if check:
                        self.price = price_inp
                        self.congratulation = True
                    else:
                        print('Необходимо ввести целое число!'.center(50,'*'))
                    
            except ValueError:
                print('Введите число!'.center(50,'*'))

    def view_all(self):
        print(f'Модель - {self.model}\nГод выпуска - {self.year} г.\n'
              f'Производитель - {self.manufacturer}\nОбъем двигателя - '
              f'{self.capacity} л.\nЦвет - {self.color}\nЦена - {self.price} ₽')
    
    def view_model(self):
        print(f'Модель - {self.model}')
    
    def view_year(self):
        print(f'Год выпуска - {self.year} г.')
    
    def view_manufacturer(self):
        print(f'Производитель - {self.manufacturer}')

    def view_capacity(self):
        print(f'Объем двигателя - {self.capacity} л.')

    def view_color(self):
        print(f'Цвет - {self.color}')

    def view_price(self):
        print(f'Цена - {self.price} ₽')
    

my_car = Car('Niva', 2020, 'Lada', 1.7, 'Белый', 1000000)

while True:
    try:
        print('1.Внести изменения\n2.Вывести все данные\n3.Вывести название '
              'модели\n4.Вывести год выпуска\n5.Вывести название производителя'
              '\n6.Вывести объем двигателя\n7.Вывести цвет\n8.Вывести цену\n'
              '0.Выход')
        choice = int(input('Выберите необходимое действие: '))
        if choice == 0:
            break
        elif choice == 1:
            my_car.inp()
        elif choice == 2:
            my_car.view_all()
        elif choice == 3:
            my_car.view_model()
        elif choice == 4:
            my_car.view_year()
        elif choice == 5:
            my_car.view_manufacturer()
        elif choice == 6:
            my_car.view_capacity()
        elif choice == 7:
            my_car.view_color()
        elif choice == 8:
            my_car.view_price()
        else:
            print('Число должно быть от 0 до 8')
    except ValueError:
        print('Введите число!')
