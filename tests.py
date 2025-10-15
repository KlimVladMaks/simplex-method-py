from simplex_method import SimplexMethod

def test_1():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_1.txt')
    answer = sm.get_solution()
    assert answer == [[0, 0, 0, 8], 32]

def test_2():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_2.txt')
    answer = sm.get_solution()
    assert answer == [[0, 0, 0, 6], 6]

def test_3():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_3.txt')
    answer = sm.get_solution()
    assert answer == [[9, 0, 0, 7], 57]
