from services.combinations import Combinations


def test_generate_pos():
    n = 1  # Anzahl der Perlen
    m = 2  # Anzahl der Positionen
    result = Combinations.generate_pos(n, m)
    assert len(result) == 2


def test_generate_pos_2():
    n = 2  # Anzahl der Perlen
    m = 2  # Anzahl der Positionen
    result = Combinations.generate_pos(n, m)
    assert len(result) == 3


def test_generate_pos_3():
    n = 3  # Anzahl der Perlen
    m = 2  # Anzahl der Positionen
    result = Combinations.generate_pos(n, m)
    assert len(result) == 4


def test_generate_pos_4():
    n = 2  # Anzahl der Perlen
    m = 3  # Anzahl der Positionen
    result = Combinations.generate_pos(n, m)
    assert len(result) == 6


def test_generate_gaps():
    n = 1  # Anzahl der Perlen
    m = 4  # Anzahl der Positionen
    result = Combinations.generate_gaps(n, m)
    assert len(result) == 4


def test_generate_gaps_2():
    n = 2  # Anzahl der Perlen
    m = 3  # Anzahl der Positionen
    result = Combinations.generate_gaps(n, m)
    assert len(result) == 6
