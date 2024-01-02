import matplotlib.pyplot as plt 

from random_walk import RandomWalk

while True:
    # Make a random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 8), dpi=137)               # adjust the size of Matplotlib's output to better fit screen
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, # to visualize the walk, we feed the walk's x and y-values to scatter()
        cmap=plt.cm.Blues, edgecolors='none', s=2)      
    ax.set_aspect('equal')                               # specify that both axes should have equal spacing between tick marks
    
    # emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break