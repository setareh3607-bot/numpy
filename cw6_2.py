# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score


# np.random.seed(42)
# girl_dist = stats.norm(4.0, 1.2)
# boy_dist = stats.norm(7.0, 1.5)

# x = np.linspace(0, 12, 1000)

# plt.figure(figsize=(9, 5))
# plt.plot(x, girl_dist.pdf(x), label="Girls")
# plt.plot(x, boy_dist.pdf(x), label="Boys")
# plt.xlabel("Hormone level")
# plt.ylabel("Probability density")
# plt.title("Hormone distributions")
# plt.legend()
# plt.grid(alpha=0.3)
# plt.show()

# n = 5000
# n_girls = int(0.7 * n)
# n_boys = n - n_girls
# girls = girl_dist.rvs(size=n_girls)
# boys = boy_dist.rvs(size=n_boys)
# X = np.concatenate([girls, boys]).reshape(-1, 1)
# y = np.concatenate([
#     np.zeros(n_girls, dtype=int),
#     np.ones(n_boys, dtype=int)
# ])
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
# knn = KNeighborsClassifier(n_neighbors=15)
# knn.fit(X_train, y_train)
# y_pred = knn.predict(X_test)
# print("Test accuracy:", accuracy_score(y_test, y_pred))
# =============================================================================================
import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(42)
n = 80
x = np.random.uniform(0, 20, n)
noise = np.random.normal(0, 8, n)
y = 7 * x -10 + noise
X = x.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)
w = model.coef_[0]
b = model.intercept_
print(w)
print(b)
print(abs(w-7))
print(abs(b + 1))

