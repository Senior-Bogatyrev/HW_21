class Book:

    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
    
    def view_all(self):
        print(f'Название - {self.name}\n'
            f'Год выпуска - {self.year} г.\n'
            f'Издательство - {self.publisher}\n'
            f'Жанр - {self.genre}\n'
            f'Автор - {self.author}\n'
            f'Цена - {self.price} ₽')
            
    def view_name(self):
        print(f'Название - {self.name}')

    def view_year(self):
        print(f'Год выпуска - {self.year} г.')
        
    def view_publisher(self):
        print(f'Издательство - {self.publisher}')

    def view_genre(self):
        print(f'Жанр - {self.genre}')

    def view_author(self):
        print(f'Автор - {self.author}')

    def view_price(self):
        print(f'Цена - {self.price} ₽')


check = True

try:
    print()
    print(' Заполните все поля! '.center(50,'*'))
    print()
    name = input('Введите название книги: ')
    year = int(input('Введите год выпуска: '))
    publisher = input('Введите название издательства: ')
    genre = input('Введите название жанра: ')
    author = input('Введите имя автора: ')
    price = int(input('Введите цену: '))
    if len(name) > 0 and len(publisher) > 0 and len(genre) > 0 \
    and len(author) > 0:
        my_book = Book(name, year, publisher, genre, author, price)
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
            print('1.Вывести все данные\n2.Вывести название книги\n3.Вывести год '
                'выпуска\n4.Вывести название издательства\n5.Вывести название жанра'
                '\n6.Имя автора\n7.Вывести цену\n0.Выход')
            choice = int(input('Выберите необходимое действие: '))
            if choice == 0:
                break
            elif choice == 1:
                print()
                my_book.view_all()
            elif choice == 2:
                print()
                my_book.view_name()
            elif choice == 3:
                print()
                my_book.view_year()
            elif choice == 4:
                print()
                my_book.view_publisher()
            elif choice == 5:
                print()
                my_book.view_genre()
            elif choice == 6:
                print()
                my_book.view_author()
            elif choice == 7:
                print()
                my_book.view_price()
            else:
                print('Число должно быть от 0 до 7')
        except ValueError:
            print('Введите число!')
