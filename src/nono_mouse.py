from cell_field import CellField

if __name__ == '__main__':
    block_definitions = {
        'rows': [[2, 2], [1, 1, 1, 1], [1, 5, 1], [2, 1, 2], [5], [3, 3], [1, 8], [1, 8], [1, 8], [8]],
        'cols': [[3], [2, 1], [1, 1, 5], [1, 8], [2, 6], [3, 4], [2, 6], [1, 8], [1, 1, 5], [2, 3]],
    }
    field = CellField(10, block_definitions)
    field.update()
    field.print()

    # start solving...
    field.try_line(5, True)
