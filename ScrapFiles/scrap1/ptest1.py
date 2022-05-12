import numpy as np

matrix_A = np.array([
    ['.', '.', 'o'],
    ['.', '.', 'x'],
    ['.', '.', '.'],
])

'''
SCENARIOS:
~ if there are 3x in a row, column or diagonal: utility = 1.0
~ if there are 2x in a row, column or diagonal: utility = 0.2 * number of scenarios
'''

utility = 0
for row in matrix_A:
    # print('x count: ', list(row).count('x'))
    if list(row).count('x') == 3:
        print("utility: 1.0")
        break
    elif list(row).count('x') == 2:
        print(utility)


print(matrix_A)
print(matrix_A.T)
