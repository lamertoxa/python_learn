import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0.01, 5, 0.01)


y = 5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)


plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Y(x)=5*cos(10*x)*sin(3*x)/(x^(1/2))')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()

plt.savefig('graph.png')

plt.show()
