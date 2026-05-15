import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sb



sb.set_theme(style = "whitegrid", context = "paper" )

input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81]

fig, ax = plt.subplots()

# Первая линия (квадраты)
ax.plot(input_values, squares, linewidth = 4)

ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 15)
ax.set_ylabel("square of Value", fontsize = 15)
ax.tick_params(labelsize=18)

# Точка (5,4) - координаты: x=5, y=4
ax.scatter(5, 4, color = 'red', s=25, zorder=5, label='Особая точка (2,4)')

ax.legend(
    loc='upper left',      # позиция: 'upper right', 'lower left', 'best'
    fontsize=12,            # размер шрифта
    frameon=True,           # рамка вокруг легенды
    shadow=True,            # тень
    title='Легенда',        # заголовок
    title_fontsize=14
)

# ВТОРАЯ ЛИНИЯ (линейная)
x_values = range(1,50)
y_values = [x*2 for x in x_values]

ax.scatter(x_values, y_values, linewidth= 2, cmap='cividis' , label = 'y=2x')            



plt.show()


