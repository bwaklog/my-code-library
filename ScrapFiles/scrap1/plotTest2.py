import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3


def update(step, xs, ys, zs, point):
    # use the following two lines for matplotlib 3.4.3
    point.set_data(xs[step:step+1], ys[step:step+1])
    point.set_3d_properties(zs[step:step+1])

    # use the following two lines for matplotlib 3.5.1
    #point.set_data([xs[step]], [ys[step]])
    # point.set_3d_properties([zs[step]])
    return point


fig = plt.figure()
ax = p3.Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

point = ax.plot([], [], [], '.')[0]

xs = np.arange(100)
ys = np.arange(100)
zs = np.arange(100)

ax.set_xlim3d([0, 100])
ax.set_ylim3d([0, 100])
ax.set_zlim3d([0, 100])

anim = animation.FuncAnimation(fig, update, 100,
                               fargs=(xs, ys, zs, point), interval=1, blit=False)

plt.show()
