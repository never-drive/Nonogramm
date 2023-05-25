from cell_line import CellLine


def test_get_dim():
    sut = CellLine.create(5, [5])
    cells = sut.get_cells()
    result = sut.get_dim()
    assert result == len(cells)


def test_get_value():
    sut = CellLine.from_text('■✕.', [5])
    assert sut.get_value(0) == '■'
    assert sut.get_value(1) == '✕'
    assert sut.get_value(2) == '.'


def test_get_combinations():
    sut = CellLine.create(5, [5])
    result = sut.get_combinations()
    assert len(result) == 1
    assert result[0] == '■■■■■'


def test_get_combinations_2():
    sut = CellLine.create(5, [2, 2])
    result = sut.get_combinations()
    assert len(result) == 1
    assert result[0] == '■■✕■■'


def test_get_combinations_3():
    sut = CellLine.create(5, [1, 2])
    assert len(sut.get_combinations()) == 3
    assert '✕■✕■■' in sut.get_combinations()
    assert '■✕✕■■' in sut.get_combinations()
    assert '■✕■■✕' in sut.get_combinations()


def test_get_combinations_4():
    sut = CellLine.create(5, [1, 1])
    assert len(sut.get_combinations()) == 6
    assert '✕✕■✕■' in sut.get_combinations()
    assert '✕■✕✕■' in sut.get_combinations()
    assert '✕■✕■✕' in sut.get_combinations()
    assert '■✕✕✕■' in sut.get_combinations()
    assert '■✕✕■✕' in sut.get_combinations()
    assert '■✕■✕✕' in sut.get_combinations()


def test_get_combinations_5():
    sut = CellLine.create(6, [1, 1, 1])
    assert len(sut.get_combinations()) == 4
    assert '✕■✕■✕■' in sut.get_combinations()
    assert '■✕✕■✕■' in sut.get_combinations()
    assert '■✕■✕✕■' in sut.get_combinations()
    assert '■✕■✕■✕' in sut.get_combinations()


def test_is_complete():
    sut = CellLine.from_text('■■■■■', [5])
    assert sut.is_complete()


def test_is_complete_2():
    sut = CellLine.from_text('■■✕■■', [2, 2])
    assert sut.is_complete()


def test_is_complete_3():
    sut = CellLine.from_text('■✕✕■■', [1, 2])
    assert sut.is_complete()


def test_is_complete_4():
    sut = CellLine.from_text('■✕✕✕■', [1, 1])
    assert sut.is_complete()


def test_is_not_complete():
    sut = CellLine.create(5, [5])
    assert not sut.is_complete()


def test_is_not_complete_2():
    sut = CellLine.from_text('■✕✕■■', [1, 1])
    assert not sut.is_complete()


def test_is_not_complete_3():
    sut = CellLine.from_text('■✕✕■.', [1, 1])
    assert not sut.is_complete()


def test_set_cells_if_possible():
    sut = CellLine.from_text('■....', [1])
    sut.set_cells_if_possible()
    assert sut.cells_as_text('') == '■✕✕✕✕'
    assert sut.is_complete()

