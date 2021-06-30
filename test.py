import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm
power_coef = 2.5
x = np.arange(0,2,0.01)
y = (x ** power_coef / 0.8) - (x ** power_coef /1.2)
rate = norm.cdf(x ** power_coef / 0.8-1) - norm.cdf(x ** power_coef/1.2-1)
right_side = x ** power_coef / 0.8 - 1
left_side = x ** power_coef / 1.2 - 1

# plt.plot(x, left_side)
# plt.plot(x, right_side)
# plt.plot(x, y)
# plt.show()