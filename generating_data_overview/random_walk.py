from random import choice
import matplotlib.pyplot as plt
class RandonWalk:

    def __init__(self, num_points=400):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):

        direction = choice([-1,1]) #направление шага
        distance = choice([0, 1, 2, 3, 4, 5, 6 ,7]) #длинна шага
        step = direction * distance

        return step

    def fill_walk(self):    

        
        while len(self.x_values) < self.num_points: # проверка что количество шагов не привысило заданное
            
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue
            
            #Calc a new position

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)



rw = RandonWalk()
rw.fill_walk()

###Plot the points in the walk.
##plt.style.use("classic")
##fig, ax = plt.subplots()
##
##ax.scatter(rw.x_values, rw.y_values, s=15)
##ax.set_aspect('equal')

plt.figure(figsize=[12,12])
plt.plot(rw.x_values, rw.y_values, linewidth=1, color="blue")
plt.scatter(0,0,c='green', s=100, label="Start")
plt.scatter(rw.x_values[-1], rw.y_values[-1], c="grey", s=150, label ="End")

# Настройка внешнего вида
plt.title("Путь броуновского движения (случайное блуждание)", fontsize=14)
plt.xlabel("Координата X", fontsize=12)
plt.ylabel("Координата Y", fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)


plt.show()

