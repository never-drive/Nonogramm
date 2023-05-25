class CellFieldPrinter:

    @staticmethod
    def print_nonogramm(field):
        text = ''
        col_defs = []
        for i in range(field.get_dim()):
            line = field.get_row_line(i)
            text += line.cells_as_text() + ' ' + line.blocks_as_text() + '\n'
            col_defs.append(field.get_col_line(i).get_blocks())
        text += CellFieldPrinter._create_lines(col_defs) + '\n'
        text += field.combination_counts_as_text() + '\n'
        print(f'{text}')

    @staticmethod
    def _create_lines(cols):
        y_max = 0
        for e in cols:
            y = len(e)
            if y > y_max:
                y_max = y
        lines = ''
        for y in range(y_max):
            for col in cols:
                if len(col) <= y:
                    lines += '  '
                else:
                    lines += str(col[y]) + ' '
            lines += '\n'
        return lines
