import numpy as np


A = np.array([[3, 2, 4],
              [1, 7, 2]])

B = np.array([[3, 4],
              [2, 3],
              [8, 5]])

result = np.dot(A, B)


print("Матрица A:")
print(A)
print("\nМатрица B:")
print(B)
print("\nРезультат умножения A × B:")
print(result)
