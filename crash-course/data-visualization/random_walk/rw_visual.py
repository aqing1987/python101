import matplotlib.pyplot as plt
import datetime

from random_walk import RandomWalk

while True:
    # create a RadomWalk instance, and draw it
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6))

    print(rw.x_values)
    print(rw.y_values)

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolor='none', s=1)
    #plt.scatter(rw.x_values, rw.y_values, s=15)

    # highlight start and end points
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # hide axis
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # save figure
    now_dt = datetime.datetime.now()
    now_str = now_dt.strftime('%Y%m%d%H%M%S')
    fname = 'rw_' + now_str + '.png'
    plt.savefig(fname, bbox_inches='tight')

    plt.show()

    keep_running = input("Make another walk ? (y/n): ")
    if keep_running == 'n':
        break
