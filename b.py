from a import SimplexMethod


sm = SimplexMethod()
answer = sm.solve([
    [9, 5, 4, 3, 2, 0, "max"],
    [1, -2, 2, 0, 0, 1, 6],
    [1, 2, 1, 1, 0, 0, 24],
    [2, 1, -4, 0, 1, 0, 30]
])
print(answer)







