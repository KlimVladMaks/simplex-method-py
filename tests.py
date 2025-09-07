from simplex_method import SimplexMethod


# sm = SimplexMethod()
# answer = sm.solve([
#     [9, 5, 4, 3, 2, 0, "max"],
#     [1, -2, 2, 0, 0, 1, 6],
#     [1, 2, 1, 1, 0, 0, 24],
#     [2, 1, -4, 0, 1, 0, 30]
# ])
# print(answer)

def test__find_row_with_smallest_negative_b():
    sm = SimplexMethod()
    sm.st = [
        [1, 5, 7, 4, -3],
        [2, 8, -7, -4, 5],
        [-7, 4, 2, 8, -7]
    ]
    answer = sm._find_row_with_smallest_negative_b()
    assert answer == 2


def test__get_rid_of_negative_free_coefficients():
    sm = SimplexMethod()
    sm.st = [
        [2, 3, 6, 1, 0, 240],
        [4, 2, 4, 0, 0, 200],
        [-4, -6, -8, 0, 1, -160]
    ]
    sm._get_rid_of_negative_free_coefficients()
    is_correct = True
    for row in sm.st:
        if row[-1] < 0:
            is_correct = False
            break
    assert is_correct


def test__find_minimum_negative_item_in_row():
    sm = SimplexMethod()
    sm.st = [
        [1, 5, 7, 4, -3],
        [2, 8, -7, -4, 5],
        [-7, 4, 2, 8, -7]
    ]
    answer = sm._find_minimum_negative_item_in_row(1)
    assert answer == 2


def test__zero_out_other_items_in_the_column():
    sm = SimplexMethod()
    sm.st = [
        [1, 5, 7, 4, -3],
        [2, 8, 1, -4, 5],
        [-7, 4, 2, 8, 1]
    ]
    sm._zero_out_other_items_in_the_column(1, 2)
    is_correct = True
    if (sm.st[0][2] != 0) or (sm.st[1][2] != 1) or (sm.st[2][2] != 0):
        is_correct = False
    assert is_correct


def test__get_coefficients_for_deltas():
    sm = SimplexMethod()
    sm.c = [3, 0, 2, 0, 0, -6]
    sm.st = [
        [2, 1, -3, 0, 0, 6, 18],
        [-3, 0, 2, 1, 0, -2, 24],
        [1/5, 0, 3/5, 0, 1, -4/5, 36/5]
    ]
    sm.basis_size = 3
    answer = sm._get_basis_indexes()
    assert answer == [1, 3, 4]


def test__calculate_deltas():
    sm = SimplexMethod()
    sm.c = [3, 0, 2, 0, 0, -6]
    sm.st = [
        [2, 1, -3, 0, 0, 6, 18],
        [-3, 0, 2, 1, 0, -2, 24],
        [1/5, 0, 3/5, 0, 1, -4/5, 36/5]
    ]
    sm.basis_size = 3
    sm.deltas = [None for _ in range(len(sm.st[0]) - 1)]
    sm._calculate_deltas()
    assert sm.deltas == [-3, 0, -2, 0, 0, 6]


def test__calculate_simplex_relations_of_q():
    sm = SimplexMethod()
    sm.st = [
        [1, -2, 2, 0, 0, 1, 6],
        [1, 2, 1, 1, 0, 0, 24],
        [2, 1, -4, 0, 1, 0, 30]
    ]
    answer = sm._calculate_simplex_relations_of_q(2)
    assert answer == [3, 24, None]
