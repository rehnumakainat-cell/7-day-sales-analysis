import numpy as np

np.random.seed(42)

daily_sales = np.random.randint(100,500,7)

print("Daily sales:", daily_sales)

print("sales sum:", np.sum(daily_sales))
print("sales mean:", np.mean(daily_sales))
print("sales max:", np.max(daily_sales))
print("sales min:", np.min(daily_sales))

discounted_sales = daily_sales * 0.9
print("discounted sales:", discounted_sales)
