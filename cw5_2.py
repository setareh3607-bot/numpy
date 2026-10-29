import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("QtAgg")


path = "/home/parsian/Downloads/student_performance_session2.csv"

y = pd.read_csv(path)
a = y["FinalScore"]
print(a.dtype)
z = y.select_dtypes(include="number").columns
print(z)
a = y.select_dtypes(include="number").corr()["FinalScore"].drop("FinalScore")
f = a.reindex(a.abs().sort_values(ascending = False).index)
print(f)

plt.figure()
plt.scatter(y["StudyHours"], y["FinalScore"])
plt.xlabel("study hours")
plt.ylabel("final score")
plt.title("study hours vs final score")
plt.show()


plt.figure()
plt.scatter(y["PreviousScore"], y["FinalScore"])
plt.xlabel("previous score")
plt.ylabel("final score")
plt.title("previous score vs final score")
plt.show()

plt.figure()
plt.scatter(y["PracticeTests"], y["FinalScore"])
plt.xlabel("practice test")
plt.ylabel("final score")
plt.title("practice tests vs final score")
plt.show()
