from random import randint
import plotly.express as px
import plotly.graph_objects as go  # 👈 ЭТОТ ИМПОРТ БЫЛ ПРОПУЩЕН

class Die:
    def __init__(self, num_side=18):
        self.num_side = num_side

    def roll(self):
        return randint(1, self.num_side)
    
die_first = Die()
die_second = Die()

results_first = [die_first.roll() for _ in range(500)]
results_second = [die_second.roll() for _ in range(500)]

# Вычисление частот
frequencies_first = []
frequencies_second = []

poss_result = range(1, 18)

for value in poss_result:
    frequencies_first.append(results_first.count(value))
    frequencies_second.append(results_second.count(value))

# 🔥 ТЕПЕРЬ go ОПРЕДЕЛЕН И РАБОТАЕТ
fig = go.Figure()

# Первый кубик - светлые тона, прозрачный
fig.add_trace(go.Bar(
    x=list(poss_result),
    y=frequencies_first,
    name='Первый кубик',
    marker_color = px.colors.qualitative.Pastel[:18],
    opacity=0.6,
    text=frequencies_first,
    textposition='auto'
))

# Второй кубик - черный
fig.add_trace(go.Bar(
    x=list(poss_result),
    y=frequencies_second,
    name='Второй кубик',
    marker_color='black',
    opacity=0.8,
    text=frequencies_second,
    textposition='auto'
))

fig.update_layout(
    title="Результаты бросков двух кубиков",
    xaxis_title="Значение",
    yaxis_title="Частота",
    barmode='group',  # или 'overlay' для наложения
    legend_title="Кубики",
    template='plotly_white'
)

fig.show()