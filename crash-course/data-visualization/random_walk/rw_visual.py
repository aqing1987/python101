import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # create a RadomWalk instance, and draw it
    rw = RandomWalk()
    rw.fill_walk()

    plt.figure(figsize=(10, 6))

    print(rw.x_values)
    print(rw.y_values)

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolor='none', s=15)
    #plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk ? (y/n): ")
    if keep_running == 'n':
        break
