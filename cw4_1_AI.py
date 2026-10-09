import numpy as np

students = np.array([
[2, 60, 45, 50],
[5, 80, 70, 75],
[1, 40, 35, 38],
[8, 90, 88, 92],
[4, 75, 60, 65],
[7, 85, 80, 84],
[3, 55, 50, 52],
[6, 70, 72, 78]
])
x = students[:, :3]
y = students[:, -1]
print(students.shape)
print(students.ndim)
print(students.size)
print(students.dtype)
print(students.shape[0])
print(students.shape[1])
print(x)
print(y)