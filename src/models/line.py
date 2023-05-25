from models.cell import Cell
from services.combinations import Combinations


class Line:

    def __init__(self, cells: list[Cell], blocks: list[int], nr: int = -1):
        self._cells = cells
        self._blocks = blocks
        self._nr = nr
        self._combinations = Line.create_all_combinations(self.get_dim(), blocks)
        self._combinations_for_cells = []

    @classmethod
    def create(cls, dim: int, blocks: list[int]):
        cell_list = []
        for i in range(dim):
            cell_list.append(Cell(-1, -1))
        return cls(cell_list, blocks)

    @classmethod
    def from_text(cls, cell_text: str, blocks: list[int]):
        cell_list = []
        for ch in cell_text:
            cell_list.append(Cell(-1, -1, ch))
        return cls(cell_list, blocks)

    def get_dim(self) -> int:
        return len(self._cells)

    def get_blocks(self) -> list[int]:
        return self._blocks

    def get_cells(self) -> list[Cell]:
        return self._cells

    def get_nr(self):
        return self._nr

    def get_cell(self, i) -> Cell:
        if 0 <= i < self.get_dim():
            return self._cells[i]
        raise IndexError()

    def get_value(self, i) -> Cell:
        cell = self.get_cell(i)
        return cell.get_value()

    def get_combinations(self) -> list:
        return self._combinations

    def get_combination_count(self) -> int:
        return len(self._combinations)

    def update_cells(self):
        combinations = []
        for comb in self._combinations:
            match = True
            for i in range(len(self._cells)):
                if self.get_value(i) == Cell.UNDEF:
                    continue
                elif self.get_value(i) != comb[i]:
                    match = False
                    break
            if match:
                combinations.append(comb)
        self._combinations_for_cells = combinations

    def get_combination_count_for_cells(self) -> int:
        return len(self._combinations_for_cells)

    def is_single(self):
        return self.get_combination_count_for_cells() == 1

    def is_complete(self) -> bool:
        if Cell.UNDEF not in self._cells:
            text = self.cells_as_text('')
            return text in self._combinations
        else:
            return False

    def is_invalid(self):
        return self.get_combination_count_for_cells() <= 0

    def cells_as_text(self, ch=' ') -> str:
        return ch.join([str(c) for c in self._cells])

    def blocks_as_text(self) -> str:
        return ' '.join([str(b) for b in self._blocks])

    def __str__(self):
        return self.cells_as_text() + ' ' + self.blocks_as_text()

    @staticmethod
    def create_all_combinations(length: int, blocks: list[int]) -> list[str]:
        positions = len(blocks) + 1
        smallest_combi = '✕'.join(['■' * block for block in blocks])
        smallest_length = len(smallest_combi)
        perls = length - smallest_length
        gap_list = Combinations.generate_gaps(perls, positions)
        combinations = []
        for gaps in gap_list:
            combi = ''
            i = 0
            for gap in gaps:
                combi += '✕' * gap
                if i < len(blocks):
                    combi += '■' * blocks[i]
                    i += 1
            combinations.append(combi)
        return combinations

    def set_cells_if_possible(self):
        self.update_cells()
        if self.is_single():
            self.set_combination(0)

    def set_combination(self, nr: int):
        combinations = self._combinations_for_cells
        if 0 <= nr < len(combinations):
            pass
        else:
            print("komisch")
            print(nr, len(combinations))
        for i in range(self.get_dim()):
            comb = combinations[nr]
            cell = self.get_cell(i)
            cell.set_value(comb[i])


if __name__ == '__main__':
    line = Line.create(11, [3, 4, 1])
    all_combinations = line.get_combinations()
    for combi in all_combinations:
        print('|'.join(combi))
    print('amount of combinations:', len(all_combinations))
