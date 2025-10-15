from simplex_method import SimplexMethod

sm = SimplexMethod()
sm.load_problem('tests_txt/test_1.txt')
answer = sm.get_solution()
print(answer)
