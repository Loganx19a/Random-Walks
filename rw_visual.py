import matplotlib.pyplot as plt 

from random_walk import RandomWalk

while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, # to visualize the walk, we feed the walk's x and y-values to scatter()
        cmap=plt.cm.Blues, edgecolors='none', s=15)      
    ax.set_aspect('equal')                               # specify that both axes should have equal spacing between tick marks
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break