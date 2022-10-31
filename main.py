class colour:
    none = "\u001b[0m"
    white = "\u001b[107m"

def rgb(r, g, b): return f"\u001b[48;2;{r};{g};{b}m"

def print_poland_flag():

    print(rgb(251,251,251), end='')
    print(' ' * 7, end='')
    print(colour.none, end='')
    print('\n', end='')

    print(rgb(251,0,0), end='')
    print(' ' * 7, end='')
    print(colour.none, end='')
    print('\n', end='')


# auxiliry finction
def next_row():
    print(colour.none, end='')
    print('\n', end='')

# auxiliry finction
def black_line(length):
    print(rgb(0, 0, 0), end='')
    print(' ' * length, end='')

def print_pattern():
    black_line(33)
    next_row()

    print(colour.none, end='')
    print(' ' * 15, end='')

    black_line(3)
    next_row()

    black_line(33)
    next_row()

    print(colour.none, end='')
    print(' ' * 7, end='')

    black_line(3)

    print(colour.none, end='')
    print(' ' * 13, end='')

    black_line(3)
    next_row()

    black_line(33)


def print_func():
    # максимальное значение аргумента
    index = 99
    # список из зчание функции
    mass = [int(i ** 0.5) for i in range(index)]
    mass.reverse()

    for i in range(max(mass), 0, -1):
        ind = mass.count(i)
        index -= ind
        line = str(i) + ' ' * index + '*' * ind
        print(line)

# подключение библиотеки
import csv

def print_stat():
    before_2017_in = after_2017 = 0
    # открытие файла
    with open('books.csv', 'r') as books_csv:
        # запись из csv в список
        books = list(csv.reader(books_csv, delimiter=';'))[1:]
        for book in books:
            # преобразование строки
            line = int(book[6].split('.')[2].split(' ')[0])
            # проверка условия
            if line > 2017:
                after_2017 += 1
            elif line <= 2017:
                before_2017_in += 1
        # процентное соотношение книг разных лет
        len_mass = len(books)

        percent_before = round(before_2017_in / len_mass * 100, 2)
        percent_after = round(after_2017 / len_mass * 100, 2)

        # вывод
        print('Книги после 2017 ' + '- ' + str(percent_after) + '%')
        print(colour.white, end='')
        print(' ' * int(percent_after), end='')
        next_row()
        next_row()
        print('Книги до 2017 (включительно) ' + '- ' + str(percent_before) + '%')
        print(colour.white, end='')
        print(' ' * int(percent_before), end='')

# вызов всех функций
print_poland_flag()
print_pattern()
next_row()
print_func()
next_row()
print_stat()





