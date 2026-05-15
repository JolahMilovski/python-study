from random import randint
import plotly.express as px

class Die:

    def __init__ (self, num_side=6):
        self.num_side = num_side

    def roll(self):
        return randint(1, self.num_side)
    
    
die = Die()

results = [die.roll() for _ in range(1000)]


print("Результаты 1000 бросков:")

for i in range(0, len(results), 50):
    batch = results[i:i+5]
    print(f'Броски {i + 1:3d} - {i+50:4d}:{batch}')


#Analize the results

frequencies =[]

title = "Results of Rolling One of 1000 times"
labels = {"x":"Result", 'y':"Frequency of Result"}

poss_result = range(1, die.num_side +1)
for value in poss_result:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#Visualize the results

fig = px.bar(x = poss_result, y = frequencies, title=title, labels=labels)
fig.show()

        
        