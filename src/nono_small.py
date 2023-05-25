from cell_field import CellField

if __name__ == '__main__':
    block_definitions = {
        'rows': [[5], [1, 1, 1], [5], [1], [1]],
        'cols': [[5], [1, 1], [3], [1, 1], [3]],
    }
    field = CellField(5, block_definitions)
    field.update()
    field.print()

    # start solving...
    field.try_line(0, True)
