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
print(x.shape)
print(y.shape)
# هر row یک دانشجو
# هر ستون یک ویژگی
# 
# =====================================2=================

rule_based_label = np.where(y >= 60, "pass", "fail")
print(rule_based_label)
print(np.sum(rule_based_label == "pass"))
print(np.sum(rule_based_label == "fail"))

# =========================================3================
study_hours = np.mean(x[:, 0])
attendance_percent = np.max(x[:, 1])
attendance_percent_min = np.min(x[:, 1])
effort_score = x[:, 0] * x[:, 1] / 100
x_new = np.column_stack([x, effort_score])
print(study_hours)
print(attendance_percent)
print(attendance_percent_min)
print(effort_score)
print(x_new)
print(x_new.shape)