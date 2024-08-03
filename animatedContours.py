import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x, y, t):
    return np.sin(x + t) * np.cos(y - t) + np.sin(x - t) * np.cos(y + t)

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

num_levels = 16
contour_levels = np.linspace(-2, 2, num_levels)

contour = ax.contour(X, Y, f(X, Y, 0), levels=contour_levels, colors="black", linestyles="solid")

def animate(t):
    Z = f(X, Y, t)
    ax.clear()
    contour = ax.contour(X, Y, Z, levels=contour_levels, colors="black", linestyles="solid")
    return contour

ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi, 60), blit=False)

writer = animation.PillowWriter(fps=30, bitrate=1800)
ani.save("contour_animation.gif", writer=writer)

#plt.show()
