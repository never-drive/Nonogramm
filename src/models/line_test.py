import pytest

from models.line import Line


def test_get_dim():
    sut = Line.create(5, [5])
    cells = sut.get_cells()
    result = sut.get_dim()
    assert result == len(cells)
    assert not sut.is_complete()


def test_get_value():
    sut = Line.from_text('■✕.', [5])
    assert sut.get_value(0) == '■'
    assert sut.get_value(1) == '✕'
    assert sut.get_value(2) == '.'


@pytest.mark.parametrize("dim,blocks,expected_cell_texts", [
    (5, [5], ['■■■■■']),
    (5, [2, 2], ['■■✕■■']),
    (5, [1, 2], ['✕■✕■■', '■✕✕■■', '■✕■■✕']),
    (5, [1, 1], ['✕✕■✕■', '✕■✕✕■', '✕■✕■✕', '■✕✕✕■', '■✕✕■✕', '■✕■✕✕']),
    (6, [1, 1, 1], ['✕■✕■✕■', '■✕✕■✕■', '■✕■✕✕■', '■✕■✕■✕'])])
def test_get_combinations(dim: int, blocks: list[int], expected_cell_texts: list[str]):
    sut = Line.create(dim, blocks)
    result = sut.get_combinations()
    assert len(result) == len(expected_cell_texts)
    for combination in result:
        assert combination in expected_cell_texts


@pytest.mark.parametrize("cell_text,blocks", [
    ('■■■■■', [5]),
    ('■■✕■■', [2, 2]),
    ('■✕✕■■', [1, 2]),
    ('■✕✕✕■', [1, 1])])
def test_is_complete(cell_text: str, blocks: list[int]):
    sut = Line.from_text(cell_text, blocks)
    assert sut.is_complete()


@pytest.mark.parametrize("cell_text,blocks", [
    ('■✕✕■■', [1, 1]),
    ('■✕✕■.', [1, 1]),
    ('■....', [1])])
def test_is_not_complete(cell_text: str, blocks: list[int]):
    sut = Line.from_text(cell_text, blocks)
    assert not sut.is_complete()


def test_set_cells_if_possible():
    sut = Line.from_text('■....', [1])
    sut.set_cells_if_possible()
    assert sut.cells_as_text('') == '■✕✕✕✕'
    assert sut.is_complete()
