# import numpy as np

# song = np.array([0.7, 0.9, 0.6])
# user_taste = np.array([0.6, 0.8, 0.5])
# w = np.array([0.6, 0.8, 0.5])
# b = 0.3
# operator = song * user_taste
# dot_product = song @ user_taste
# score =(song @ w) + b
# print(operator)
# print(dot_product)
# print(score)
# print(operator.shape)
# print(dot_product.shape)
# =============================3===============
# import numpy as np

# song1 = np.array([0.9, 0.1])
# song2 = np.array([0.85, 0.15])
# song3 = np.array([-0.9, -0.1])
# dot_product = song1 @ song2
# dot_product1 = song1 @ song3
# norm1 = np.linalg.norm(song1)
# norm2 = np.linalg.norm(song2)
# norm3 = np.linalg.norm(song3)
# cosine_sim = dot_product / (norm1 * norm2)
# cosine_sim2 = dot_product1 / (norm1 * norm3)
# # print(dot_product)
# # print(norm1)
# # print(norm2)
# # print(norm3)
# print(cosine_sim)
# print(cosine_sim2)
# ==================================4================
# import numpy as np

# songs = np.array([
#     [0.7, 0.9, 0.6],
#     [0.6, 0.8, 0.5],
#     [0.85, 0.15, 0.3],
#     [0.5, 0.4, 0.7],
#     [0.9, 0.1, 0.5]
# ])
# w = np.array([0.6, 0.8, 0.5])
# b = 0.3
# scores = songs @ w + b
# print(scores)
# =================================5===================
# import numpy as np

# stats = np.random.rand(4, 3)
# skill_matrix = np.random.rand(3, 5)
# matrix = stats @ skill_matrix
# print(matrix.shape)
# print(matrix[3])
# ===================================6=========================
# import numpy as np

# X_chars = np.array([
# [80, 40, 60],
# [30, 90, 50],
# [70, 70, 70],
# [95, 20, 40]
# ])
# W_skills = np.random.randn(3, 3)
# b_skills = np.array([1.0, -0.5, 0.2])

# z = X_chars @ W_skills + b_skills
# print(z[:, 0])
# print(z.shape)
# =====================================7=====================
import numpy as np



