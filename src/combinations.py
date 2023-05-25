from itertools import combinations_with_replacement


class Combinations:

    @staticmethod
    def generate_pos(n, m) -> ():
        if n < 0:
            return []
        positions = [i for i in range(m)]  # Erzeuge eine Liste von Positionen
        all_combinations = list(combinations_with_replacement(positions, n))
        return all_combinations

    @staticmethod
    def generate_gaps(n, m) -> ():
        all_gaps = []
        for pos in Combinations.generate_pos(n, m):
            gaps = []
            for i in range(m):
                count = len([p for p in pos if p == i])
                if 0 < i < m - 1:
                    count += 1
                gaps.append(count)
            all_gaps.append(gaps)
        return all_gaps


if __name__ == '__main__':
    # Beispielaufruf
    n = 1  # Anzahl der Perlen
    m = 4  # Anzahl der Positionen
    result = Combinations.generate_gaps(n, m)
    for combi in result:
        print(combi)
