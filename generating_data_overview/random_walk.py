from random import choice
import matplotlib.pyplot as plt
class RandonWalk:

    def __init__(self, num_points=4000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):    

        while len(self.x_values) < self.num_points:
            
            x_direction = choice([1, -1])
            x_distence = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distence

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue
            
            #Calc a new position

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

rw = RandonWalk()
rw.fill_walk()

#Plot the points in the walk.
plt.style.use("classic")
fig, ax = plt.subplots()

ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')

plt.show()
