from models.field import Field
from services.printer import Printer


class Solver:

    @staticmethod
    def try_line(field: Field, i: int, is_row: bool):
        if field.is_complete():
            print('solution found!\n')
            field.update()
            Solver.print_field(field)
            return  # terminate solving...

        line = field.get_row_line(i) if is_row else field.get_col_line(i)
        max_combinations = line.get_combination_count_for_cells()
        for n in range(max_combinations):
            field.update_row(i, n) if is_row else field.update_col(i, n)
            print('row:' if is_row else 'col:', i, 'updated')
            if field.is_invalid():
                Solver.print_field(field)
                field.go_back()
            else:
                # next step
                if not is_row:
                    i += 1
                if i >= field.get_dim():
                    i = 0
                Solver.try_line(field, i, not is_row)
        # no solution for current step
        if field.can_go_back():
            Solver.print_field(field)
            field.go_back()
        else:
            print('no solution found!\n')

    @staticmethod
    def print_field(field):
        Printer.print_nonogramm(field)
