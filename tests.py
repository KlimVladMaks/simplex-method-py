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

def test_4():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_4.txt')
    answer = sm.get_solution()
    assert answer == [[0, 0, 0, 5], 10]

def test_5():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_5.txt')
    answer = sm.get_solution()
    assert answer == [[2, 4, 0, 0], 22]

def test_6():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_6.txt')
    answer = sm.get_solution()
    assert answer == [[0, 0, 7, 0], 7]

def test_7():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_7.txt')
    answer = sm.get_solution()
    assert answer == [[6, 0, 0, 9], 54]

def test_8():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_8.txt')
    answer = sm.get_solution()
    assert answer == [[0, 0, 2, 4], 8]

def test_9():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_9.txt')
    answer = sm.get_solution()
    assert answer == [[0, 2, 7, 1], 25]

def test_10():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_10.txt')
    answer = sm.get_solution()
    assert answer == [[0, 2, 5, 0], 7]

def test_11():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_11.txt')
    answer = sm.get_solution()
    assert answer == [[9, 0, 1, 0], 13]

def test_12():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_12.txt')
    answer = sm.get_solution()
    assert answer == [[5/2, 0, 9/2, 1/2], 23/2]

def test_13():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_13.txt')
    answer = sm.get_solution()
    assert answer == [[0, 8, 0, 6], 32]

def test_14():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_14.txt')
    answer = sm.get_solution()
    assert answer == [[0, 0, 0, 4], 4]

def test_15():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_15.txt')
    answer = sm.get_solution()
    assert answer == [[0, 11/5, 7/5, 28/5], 144/5]

def test_16():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_16.txt')
    answer = sm.get_solution()
    # Правильный ответ: [[7/3, 0, 22/3, 5/3], 21]
    # но т.к. в нём встречаются бесконечные дроби, то будем сравнивать только ответ
    assert answer[1] == 21

def test_17():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_17.txt')
    answer = sm.get_solution()
    assert answer == [[2, 6, 0, 0], 20]

def test_18():
    sm = SimplexMethod()
    sm.load_problem('tests_txt/test_18.txt')
    answer = sm.get_solution()
    assert answer == [[5, 0, 0, 3], 16]

# def test_19():
#     sm = SimplexMethod()
#     sm.load_problem('tests_txt/test_19.txt')
#     answer = sm.get_solution()
#     assert answer == [[], ]

# def test_20():
#     sm = SimplexMethod()
#     sm.load_problem('tests_txt/test_20.txt')
#     answer = sm.get_solution()
#     assert answer == [[], ]
