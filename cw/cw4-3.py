# import numpy as np

# def sample(samples):
#     np.random.seed(0)
#     x = np.random.rand(samples, 5)
#     y = np.random.randint(0, 2, samples)
#     data = np.c_[x, y]
#     print(data.shape)
#     print(len(data))
#     print("Training Set:", int(len(data)* .8))
#     print("Validation Set:", int(len(data)* .1))
#     print("Test Set:", len(data) - int(len(data) * .8) - int(len(data)* .1))
#     total = int(len(data)* .8) + int(len(data)* .1) + len(data) - int(len(data) * .8) - int(len(data)* .1)
#     print("total:", total)
#     print("check:", len(data) == total)
# sample(10000)
# sample(12350)
# ===============================tamrin2=====================

import numpy as np

ground_truth = np.array(["Normal", "Urgent", "Normal", "Spam", "Urgent", "Normal", "Spam", "Normal"])
predictions  = np.array(["Normal", "Normal", "Normal", "Spam", "Urgent", "Spam", "Spam", "Normal"])
print("ground_truth:", ground_truth)
print("predictions:", predictions)
comparison = ground_truth == predictions
print("comparison correct:", comparison)
print("Correct number:", np.sum(comparison))
print("")