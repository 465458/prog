from csv import reader

request = input("Введите ФИО автора:")

with open('books.csv', 'r') as r_file:
    file = reader(r_file, delimiter=';')
    print('Книги автора:')
    for row in file:
        if ('2018' in row[6] or '2015' in row[6]) and (request in row[4]):
            print(row[1][1:])
        