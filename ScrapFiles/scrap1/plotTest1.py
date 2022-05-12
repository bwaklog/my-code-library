import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3


def update(n, x, y, z, point):
    point.set_data(x[n:n+1], y[n:n+1])
    point.set_3d_properties(z[n:n+1])
    return point


fig = plt.figure()
ax = p3.Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)


# parametric curve
t = np.arange(0, 2*np.pi, 2*np.pi/100)
x = np.cos(t)
y = np.sin(t)
z = t/(2.*np.pi)

# plot first point
point = ax.plot(x[0], y[0], z[0], '.')


line = plt.plot(x, y, z, color='blue')
ax.set_xlim3d([-1.5, 1.5])
ax.set_ylim3d([-1.5, 1.5])
ax.set_zlim3d([-1.5, 1.5])

# Method1: remake plot at every frame


def m1_update(n, x, y, z, ax):
    ax.cla()
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])
    point = ax.scatter(x[n], y[n], z[n], color='orange')
    line = ax.plot(x, y, z, color='blue')
    return point


anim = animation.FuncAnimation(fig, m1_update, 99, fargs=(x, y, z, ax))

plt.show()
