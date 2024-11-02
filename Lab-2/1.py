from csv import reader

count = 0

with open('books-en.csv', 'r') as r_file:
    file = reader(r_file, delimiter = ';')
    for row in file:
        if len(row[1]) > 30:
            count += 1 

print('Количество книг, у которых в названии более 30 символов:',count)