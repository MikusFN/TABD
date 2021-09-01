import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(i):    
    y_i = F[i]    
    scat.set_offsets(np.c_[x, y_i])

fig, ax = plt.subplots(figsize=(5, 3))
ax.set(xlim=(-3, 3), ylim=(-1, 1))
x = np.linspace(-3, 3, 9)
t = np.linspace(1, 25, 30)
X2, T2 = np.meshgrid(x, t)
sinT2 = np.sin(2 * np.pi * T2 / T2.max())
F = 0.9 * sinT2 * np.sinc(X2 * (1 + sinT2))
scat = ax.scatter(x, F[0])
anim = FuncAnimation(fig, animate, interval=100, frames=len(t) - 1)
plt.draw()
plt.show()