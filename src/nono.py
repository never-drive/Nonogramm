from cell_field import CellField

if __name__ == '__main__':
    block_defs = {
        'rows': [[2, 2], [1, 1], [5], [1, 1, 2], [2, 1, 1, 2],
                 [2, 2, 1], [2, 8], [4, 2, 3], [3, 1], [1, 1, 1],
                 [3, 4, 2], [5, 2, 3, 1], [1, 1, 2, 2, 1], [3, 3, 1], [3, 1]],
        'cols': [[2], [4, 2], [1, 1, 2], [2, 1, 2, 1], [1, 1, 1, 8],
                 [3, 1, 1, 2], [1, 2, 2], [8, 2], [1, 2, 2], [1, 1, 1],
                 [1, 4], [1, 5], [1, 2, 1], [2, 5, 1], [4, 2, 2]],
    }
    field = CellField(15, block_defs)
    field.update()
    field.print()

    # start solving...
    field.try_line(0, True)

'''
    # start solving...

    field.update()
    field.update_row(11, 0)
    field.update_col(4, 0)
    field.update_row(2, 0)
    
    field.go_back()
    field.go_back()
    field.go_back()
    field.print()
'''
