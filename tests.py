from simplex_method import SimplexMethod

def test_solve_1():
    sm = SimplexMethod()
    answer = sm.solve([
        [9, 5, 4, 3, 2, 0, "max"],
        [1, -2, 2, 0, 0, 1, 6],
        [1, 2, 1, 1, 0, 0, 24],
        [2, 1, -4, 0, 1, 0, 30]
    ])
    assert answer == [[0, 7, 10, 0, 63, 0], 201]

def test_solve_2():
    sm = SimplexMethod()
    answer = sm.solve([
        [3, 4, 2, 1, 0, "max"],
        [2, 1, 1, 0, 0, 8],
        [1/3, 2/3, 0, 1, 5/3, 2]
    ])
    assert answer == [[0, 3, 5, 0, 0], 22]

def test_solve_3():
    sm = SimplexMethod()
    answer = sm.solve([
        [4, 5, 4, 0, 0, "max"],
        [2, 3, 6, 1, 0, 240],
        [4, 2, 4, 0, 0, 160],
        [4, 6, 8, 0, 1, 200]
    ])
    assert answer == [[35, 10, 0, 140, 0], 190]
