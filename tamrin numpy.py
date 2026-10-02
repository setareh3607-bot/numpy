# import numpy as np


# scores = [72, 85, 90, 66, 78]

# score = np.array(scores)
# x = score.ndim
# y = score.shape
# z = score.dtype
# f = score.size
# print(score)
# print(x)
# print(y)
# print(z)
# print(f)
# ========================tamrin2==============================
# import numpy as np

# grades = np.array([
# [18, 15, 12, 20], # Student 1
# [14, 17, 19, 16], # Student 2
# [20, 20, 18, 15] # Student 3
# ])

# student2 = grades[1]
# final_exam = grades[:, -1]
# sub_matrix = grades[0:2, 0:2]
# print(student2)
# print(final_exam)
# print(sub_matrix)
# ====================tamrin3==============================
# import numpy as np

# a = np.array([3, 6, 9])
# b = np.array([1, 2, 3])

# sum1 = a[0] + b[0]
# sum2 = a[1] + b[1]
# sum3 = a[2] + b[2]
# result = a + b
# subtraction1 = a[0] - b[0]
# subtraction2 = a[1] - b[1]
# subtraction3 = a[2] - b[2]
# result1 = a - b
# multiplication1 = a[0] * b[0]
# multiplication2 = a[1] * b[1]
# multiplication3 = a[2] * b[2]
# result2 = a * b
# result3 = a * .5
# print(f"sum: {sum1}, {sum2}, {sum3}")
# print(f"subtraction: {subtraction1}, {subtraction2}, {subtraction3}")
# print(f"Multiplication: {multiplication1}, {multiplication2}, {multiplication3}")
# print(result)
# print(result1)
# print(result2)
# print(result3)
# ============================tamrin4========================================
# import numpy as np

# x = np.array([
#     [34, 20 , 1],
#     [12, 43, 18],
#     [8, 32, 24]])
# v = np.array([100, 0, -5])
# result = v + x
# print(result)
# ==============================tamrin5========================================
# import numpy as np


# point_A = np.array([2, 3, 5])
# point_B = np.array([7, 1, 9])
# result = point_A - point_B

# x = np.linalg.norm(result)
# print(x)
# if x >= 7:
#   print("The result is closer to 10.")
# elif x < 7:
#     print("The result is closer to 5.")
# ============================tamrin6=========================
# import numpy as np

# M = np.array([
#     [80, 70, 90],
#     [60, 85, 75],
#     [95, 60, 80],
#     [70, 70, 70]
# ])

# x = M.T
# x1 = x.shape
# y = M.reshape(2, 6)
# w = M.reshape(6, 2)
# print(x)
# print(x1)
# print(y)
# print(w)
# =================================tamrin7===================
import numpy as np

M = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 60, 80],
    [70, 70, 70]
])

weights = np.array([0.5, 0.3, 0.2])

x = np.dot(M, weights)
print(x)