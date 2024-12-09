from pprint import pprint
#можно использовать pretty print для красивого вывода
MAX_CELLS = 4

items = {
    'a': {'price': 700, 'cells': 3},
    'b': {'price': 300, 'cells': 1},
    'c': {'price': 500, 'cells': 2},
    'd': {'price': 550, 'cells': 2},
}

def table_memo(items, max_cells):
    table = [ [ 0 for _ in range(max_cells)] for _ in range(len(items))]
    for row, value in enumerate(items.values()):
        cells = value['cells']
        price = value['price']
        for limit_cells in range(1, max_cells+1):
            col = limit_cells - 1

            if row == 0:
                table[row][col] = 0 if cells > limit_cells else price
            else:
                prev_price = table[row-1][col]
                if cells > limit_cells:
                    table[row][col] = prev_price
                else:
                    used = 0 if col-cells < 0 else table[row-1][col-cells]
                    res = max(prev_price, price + used)
                    table[row][col] = res
    pprint(table)
    pprint(items)

table_memo(items, MAX_CELLS)