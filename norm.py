import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt 

x_up = np.arange(0.001,2,0.001)
y_up = 1.5 - norm.cdf(1/x_up)
p_up = norm.pdf(1/x_up)

x_down = np.arange(-2,0,0.001)
y_down = 0.5 - norm.cdf(1/x_down)
p_down = norm.pdf(1/x_down)

x = np.concatenate((x_down, x_up), axis = 0)
y = np.concatenate((y_down, y_up), axis = 0)
p = np.concatenate((p_down, p_up), axis = 0)

plt.plot(x,p)
plt.show()