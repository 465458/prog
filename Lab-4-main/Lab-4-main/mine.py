MAX_CELLS = 9

items = [
    ['r',25,3],
    ['p',15,2],
    ['a',15,2],
    ['m',20,2],
    ['i',5,1],
    ['k',15,1],
    ['x',20,3],
    ['t',25,1], 
    ['f',15,1],
    ['d',10,1],
    ['s',20,2],
    ['c',20,2]
]

survival_points = 15
survival_points += [x for x in items if x[0] == 'i'][0][1]
i_size = [x for x in items if x[0] == 'i'][0][2]
free_space = MAX_CELLS-i_size
items = [x for x in items if x[0] != 'i']
backpack = []
backpack.append('i')

items.sort(key=lambda row: (row[2]))
items.sort(key=lambda row: (row[1]),reverse = True)

n = 0
for x in items:
    n += 1
    if x[2] <= free_space:
        backpack.append(x[0])
        survival_points += x[1]
        free_space -= x[2]

print('Инвентарь:',backpack)
print('Очки выживания:',survival_points)






