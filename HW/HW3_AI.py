# import numpy as np

# gym_data = np.array([
#     [28, 75, 175, 4],
#     [34, 68, 168, 3],
#     [45, 82, 180, 2],
#     [22, 58, 162, 5],
#     [38, 90, 0, 1],
#     [29, 65, 170, 0]
# ], dtype = float)
# member_names = np.array(["Ali", "Sara", "Reza", "Neda", "Hassan", "Maryam"])

# for col in range(1, gym_data.shape[1]):
#     column = gym_data[:, col]
#     print(col, column)
#     mean_val = np.mean(column[column != 0])
#     column[column == 0] = mean_val
# print(gym_data)
# features = gym_data[:, 1:]
# print(features)

# bmi = gym_data[:, 1] / (gym_data[:, 2] / 100) **2
# print(bmi)
# score = (bmi * 1) + (gym_data[:, 3] * 1)
# print(score)
# print("Highest score:", member_names[np.argmax(score)])

# session = gym_data[:, 3]
# mean_session = np.mean(session)
# std_session = session.std()
# sb_session = np.abs(session - mean_session)
# max_distance = sb_session.max()

# print(member_names[max_distance == sb_session])
# print(max_distance > std_session)
# print(std_session)
# print(sb_session)
# print(mean_session)
# =============================tamrin2======================
# import numpy as np

# recipes = np.array([
#     [15, 350, 2, 5],
#     [45, 600, 7, 10],
#     [10, 200, 0, 3],
#     [30, 450, 5, 7],
#     [60, 800, 8, 12]
# ])
# recipe_names = ["Salad", "Curry", "Toast", "Pasta", "Stew"]
# users = np.array([
#     [10, 250, 1, 4],
#     [50, 700, 8, 11],
#     [25, 400, 4,6]
# ])

# print(recipes.shape)
# print(recipes.ndim)
# recipe_min = recipes.min(axis = 0)
# recipe_max = recipes.max(axis = 0)
# recipe_scaled = (recipes - recipe_min) / (recipe_max - recipe_min)
# users_scaled = (users - recipe_min) / (recipe_max - recipe_min)
# users_resh = users_scaled.reshape(3, 1, 4)
# recipe_resh = recipe_scaled.reshape(1, 5, 4)
# diff = users_resh - recipe_resh
# square = diff ** 2
# square_root = np.sqrt(np.sum(square, axis = 2))
# names = np.array(recipe_names)
# closest = np.argmin(square_root, axis = 1)
# sorting = np.argsort(square_root, axis = 1)
# print(users_scaled.shape)
# print(recipe_scaled)
# print(users_scaled)
# print(users_resh)
# print(recipe_resh)
# print(diff.shape)
# print(square_root.shape)
# print(names[closest])
# print(names[sorting])
# print(diff.shape)
# # ===============================tamrin3===================
# import numpy as np

# scores = np.array([
#     [18, 15, 20],
#     [12, 14, 16],
#     [20, 19, 18],
#     [10, 8, 15]
# ])
# scheme_A = np.array([0.5, 0.3, 0.2])
# scheme_B = np.array([0.2, 0.3, 0.5])
# scheme_C = np.array([0.1, 0.2, 0.7])

# choices = ([
#     scheme_A, scheme_B, scheme_C
# ])
# scheme_D = np.array([0.2, 0.4, 0.4])
# choices.append(scheme_D)
# weight_matrix = np.vstack(choices)
# final_scores = scores @ weight_matrix.T
# the_most = np.argmax(final_scores, axis=1)
# class_means = np.mean(final_scores, axis=0)
# print(weight_matrix.shape)
# print(final_scores.shape)
# print(the_most)
# print(class_means)
# print(np.max(class_means))
# print(np.argmax(class_means))
# print(weight_matrix)
# ============================tamrin4==========================
# import numpy as np

# weather_data = np.random.randn(2, 8, 4) * 5 + 20
# day2 = weather_data[1]
# transposition = day2.T
# def analyze_day(data):
#     print(data.shape)
# analyze_day(transposition)
# result = weather_data.reshape(-1)
# print(result.shape)
# matrix = np.array([
#     [1, 2],
#     [3, 4]
#     ])
# print(matrix.T)
# print(matrix.reshape(-1))
# day3 = np.random.randn(8, 4)
# day3_new = day3.reshape(1, 8, 4)
# x = np.concatenate((weather_data, day3_new), axis=0)
# y = np.save("weather.npy", x)

# print(day3_new.shape)
# print(x.shape)
# print(y)
# ==================================tamrin5===============
import numpy as np

importance = np.array([3, 8, 1, 9, 4, 7])
model_out = np.array([[[0.9]]])

print(importance.shape)
importance_reshape = importance.reshape(6, 1)
print(importance_reshape)
importance_new = importance[:, np.newaxis]
print(importance_new)
print(model_out.shape)
print(type(model_out[0, 0, 0]))
print(type(model_out.item()))

notes = np.array([5, 10, 15, 20, 25])
pinned = notes[1:3].copy()
pinned[0] = 999
print(notes)
print(pinned)

notes = np.array([5, 10, 15, 20, 25])
pinned = notes[1:3]
pinned[0] = 999
print(notes)


