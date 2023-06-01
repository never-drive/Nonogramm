import pytest

from services.combinations import Combinations


@pytest.mark.parametrize("perls,positions,expected_amount", [
    (1, 2, 2),
    (2, 2, 3),
    (3, 2, 4),
    (2, 3, 6)])
def test_generate_pos(perls: int, positions: int, expected_amount: int):
    n = perls      # Anzahl der Perlen
    m = positions  # Anzahl der Positionen
    result = Combinations.generate_pos(n, m)
    assert len(result) == expected_amount


@pytest.mark.parametrize("perls,positions,expected_amount", [
    (1, 4, 4),
    (2, 3, 6)])
def test_generate_gaps(perls: int, positions: int, expected_amount: int):
    n = perls      # Anzahl der Perlen
    m = positions  # Anzahl der Positionen
    result = Combinations.generate_gaps(n, m)
    assert len(result) == expected_amount
