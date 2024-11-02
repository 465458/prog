from csv import reader

output = open('3.txt', 'w')
result = []
k = 0


with open('books-en.csv', 'r') as r_file:
    file = reader(r_file, delimiter=';')
    for row in file:
        if k == 0:
            ...
        if k>=1 and k<=20:
            output.write(f"{k}. {row[2]}. {row[1]} - {row[3]} \n")
        k += 1

output.close()