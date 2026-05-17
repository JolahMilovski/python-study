from pathlib import Path
import csv
import matplotlib.pyplot as plt



path = Path('sitka_weather_2021_simple-original.csv')

line = path.read_text().splitlines()

reader = csv.reader(line)

haeder_raw = next(reader)

for index, colomn_header in enumerate(haeder_raw):
    print(index, colomn_header)

print(haeder_raw)

#Extract high temprature

highs = []

date, highs = [],[]
for row in reader:
    higth = int(row[4])
    highs.append(higth)

max_temp = max(highs)
max_index = highs.index(max_temp) 

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

ax.plot(highs, color = 'red')

ax.set_title("Daily High tempritures. July 2021", fontsize = 24)
ax.set_xlabel("", fontsize=16)
ax.tick_params(labelsize = 16)

ax.plot(max_index, max_temp, 'o', color='darkorange', markersize=12, 
        markeredgecolor='black', markeredgewidth=1.5)

plt.show()

#['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'petroff10', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']