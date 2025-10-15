from simplex_method import SimplexMethod

def test_1():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_1.txt')
    answer = sm.get_solution()
    assert answer == [[0, 7, 10, 0, 63, 0], 201]

def test_2():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_2.txt')
    answer = sm.get_solution()
    assert answer == [[35, 10, 0, 140, 0], 190]

def test_3():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_3.txt')
    answer = sm.get_solution()
    assert answer == [[0, 1, 6, 0, 0], -5]

def test_4():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_4.txt')
    answer = sm.get_solution()
    assert answer == [[2, 0, 0, 2], 6]

def test_5():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_5.txt')
    answer = sm.get_solution()
    assert answer is None

def test_6():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_6.txt')
    answer = sm.get_solution()
    assert answer == [[0, 1, 6, 0, 0], -5]

def test_7():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_7.txt')
    answer = sm.get_solution()
    assert answer == [[7, 0, 5/2, 0, 1/2, 0], 165]

def test_8():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_8.txt')
    answer = sm.get_solution()
    assert answer is None
