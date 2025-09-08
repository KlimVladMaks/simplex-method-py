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

def test_solve_4():
    sm = SimplexMethod()
    answer = sm.solve([
        [2, 1, -1, 0, 0, "min"],
        [3, 0, 2, -1, 0, 12],
        [1, -1, 1, 0, 0, 5],
        [1, 0, 1, 0, -1, 6]
    ])
    assert answer == [[0, 1, 6, 0, 0], -5]

def test_solve_5():
    sm = SimplexMethod()
    answer = sm.solve([
        [3, -2, 4, 0, "max"],
        [3, -1, 1, -1, 4],
        [1, 2, 4, 0, 2]
    ])
    assert answer == [[2, 0, 0, 2], 6]

def test_solve_6():
    sm = SimplexMethod()
    answer = sm.solve([
        [2, 1, -2, 0, 0, 0, "min"],
        [1, -5, 0, -3, 0, -1, 25],
        [0, -16, 0, -7, 1, -3, 57],
        [0, -6, 1, -2, 0, -1, 17]
    ])
    assert answer is None

def test_solve_7():
    sm = SimplexMethod()
    answer = sm.solve([
        [20, 20, 10, 0, 0, 0, "min"],
        [-4, -3, -2, 1, 0, 0, -33],
        [-3, -2, -1, 0, 1, 0, -23],
        [-1, -1, -2, 0, 0, 1, -12]
    ])
    assert answer == [[7, 0, 5/2, 0, 1/2, 0], 165]

def test_solve_8():
    sm = SimplexMethod()
    answer = sm.solve([
        [20, 20, 10, 0, 0, 0, "max"],
        [-4, -3, -2, 1, 0, 0, -33],
        [-3, -2, -1, 0, 1, 0, -23],
        [-1, -1, -2, 0, 0, 1, -12]
    ])
    assert answer is None
