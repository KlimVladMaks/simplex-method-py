from simplex_method import SimplexMethod

def test_1():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_1.txt')
    answer = sm.get_solution()
    assert answer == [[0, 7, 10, 0, 63, 0], 201]
