from models.cell import Cell
from models.line import Line


class Field:

    def __init__(self, dim: int, block_defs: {list[list[int]]}):
        self._block_defs = block_defs
        row_defs = block_defs['rows']
        col_defs = block_defs['cols']

        all_cells = []
        row_lines = []
        for y in range(dim):
            row_cells = []
            for x in range(dim):
                row_cells.append(Cell(x, y))
            all_cells += row_cells
            row_lines.append(Line(row_cells, row_defs[y], y))

        col_lines = []
        for x in range(dim):
            col_cells = []
            for y in range(dim):
                line = row_lines[y]
                cell = line.get_cell(x)
                assert line.get_nr() == y
                assert cell.get_x() == x
                assert cell.get_y() == y
                col_cells.append(cell)
            col_lines.append(Line(col_cells, col_defs[x], x))

        self._dim = dim
        self._all_cells = all_cells
        self._row_lines = row_lines
        self._col_lines = col_lines
        self._steps = []
        self._solutions = []
        self._update()

    def get_dim(self):
        return self._dim

    def is_complete(self):
        for line in self._row_lines:
            if not line.is_complete():
                return False
        for line in self._col_lines:
            if not line.is_complete():
                return False

        # solution found -> keept it!
        self.add_solution()

        return True

    def is_invalid(self):
        for line in self._row_lines:
            if line.is_invalid():
                return True
        for line in self._col_lines:
            if line.is_invalid():
                return True
        return False

    # for printer...

    def cells_as_text(self):
        text = ''
        for y in len(self._row_lines):
            text += self._row_cells_as_text(self, y) + '\n'
        return text

    def _row_cells_as_text(self, y):
        return ' '.join(str(c.get_value()) for c in self._get_row_cells(y))

    def _get_row_cells(self, y):
        return self._row_lines[y].get_cells()

    def combination_counts_as_text(self):
        row_combinations = []
        for line in self._row_lines:
            row_combinations.append(line.get_combination_count_for_cells())
        col_combinations = []
        for line in self._col_lines:
            col_combinations.append(line.get_combination_count_for_cells())
        return 'row combinations: ' + ', '.join([str(c) for c in row_combinations]) + '\n' + \
               'col combinations: ' + ', '.join([str(c) for c in col_combinations])

    # for user to play...

    def change_value(self, x, y):
        cell = self._get_cell(x, y)
        cell.change_value()

    def _get_cell(self, x, y) -> Cell:
        cell = self._all_cells[y * self._dim + x]
        assert cell.get_x() == x
        assert cell.get_y() == y
        return cell

    # for unit testing to manipulate values directly...

    def get_value(self, x, y):
        cell = self._get_cell(x, y)
        return cell.get_value()

    def set_value(self, x, y, value):
        cell = self._get_cell(x, y)
        cell.set_value(value)

    # for solver to access...

    def update_row(self, y: int, nr: int):
        self.push()
        line = self.get_row_line(y)
        line.set_combination(nr)
        self._update()

    def update_col(self, x: int, nr: int):
        self.push()
        line = self.get_col_line(x)
        line.set_combination(nr)
        self._update()

    def can_go_back(self):
        return len(self._steps) > 0

    def go_back(self):
        self.pop()
        self._update()

    def _update(self):
        for line in self._row_lines:
            line.set_cells_if_possible()
        for line in self._col_lines:
            line.set_cells_if_possible()

    def get_row_line(self, y: int) -> Line:
        return self._row_lines[y]

    def get_col_line(self, x: int) -> Line:
        return self._col_lines[x]

    def add_solution(self):
        values = self._collect_values()
        self._solutions.append(values)

    def solution_count(self):
        return len(self._solutions)

    def push(self):
        values = self._collect_values()
        self._steps.append(values)

    def pop(self):
        if len(self._steps) <= 0:
            return
        value = self._steps.pop()
        for i in range(len(self._all_cells)):
            cell = self._all_cells[i]
            cell.set_value(value[i])

    def _collect_values(self):
        values = ''
        for cell in self._all_cells:
            values += cell.get_value()
        return values
