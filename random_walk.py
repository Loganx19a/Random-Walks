from random import choice 

""" 
this class needs 3 variables: 
one to track the number of points in the walk,
and two lists to store the x and y-coordinates of each point in the walk
"""

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        # initialize attributes of a walk
        self.num_points = num_points

        # start each walk at the point (0, 0)
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """Calculate all the points in the walk"""

        # keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            x_step = get_step()
            y_step = get_step()

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the new position
            x = self.x_values[-1] + x_step   # add the value in x_step to the last value stored in x_values
            y = self.y_values[-1] + y_step   # and do the same for the y-values

            # once we have the new point's coordinates, append them to the lists: x_values and y_values
            self.x_values.append(x)
            self.y_values.append(y)

    def get_step():
        direction = choice([1, -1])             # which direction will the walk go?
        distance = choice([0, 1, 2, 3, 4])      # how far will it go in that direction?
        step = direction * distance 
        return step
