import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



x = np.arange(0.01, 5, 0.01)
y = 5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)


fig = plt.figure()


ax = fig.add_subplot(111, projection='3d')


def animate(i):
    ax.clear()
    ax.plot(x[:i], y[:i], color='b')
    ax.set_xlim([0, 5])
    ax.set_ylim([min(y), max(y)])


ani = animation.FuncAnimation(fig, animate, frames=len(x), repeat=True)


fig.ani = ani


plt.show()
