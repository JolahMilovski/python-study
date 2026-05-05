bicycles = ['trec', 'cannondale', 'redlone', 'spcialized']
to_loop_bicycles = bicycles.copy()
print(bicycles)
print(bicycles[1])
print(bicycles[0])



print(bicycles[2].title())
print(bicycles[-1].upper())

message=f"My bicycles was a {bicycles[-1].lower()}"
print(message)
print("\n")
bicycles[-1]='kendo'
message=f"My bicycles was a {bicycles[-1].lower()}"
print(message)

bicycles.append("night nemo")
message=f"My bicycles is a {bicycles[-1].lower()}"
print(message)

bicycles.insert(4,"numerico")
print(bicycles)

#copy bicycle to new_bicycles

new_bicycles = bicycles.copy()
print_new_bicycles=f'NEW bicycles it is a {bicycles}\n'
print(print_new_bicycles)

#sort
sort_bicycles = bicycles.copy()
sort_bicycles.sort()
print(sort_bicycles)
print_sort_bicycles=f'NEW sort bicycles its a {sort_bicycles}\n'
print(print_sort_bicycles)

#reverse
reverse_bicycles = sort_bicycles.copy()
reverse_bicycles.reverse()
print(reverse_bicycles)
print_reverse_bicycles=f'NEW REVERSE bicycles its a {reverse_bicycles}\n'
print(print_reverse_bicycles)

pop_bicycles_0=bicycles.pop(0)
pop_bicycles_end=bicycles.pop(-1)
pop_bicycles_pre_end=bicycles.pop(-2)

print(bicycles)
print(pop_bicycles_0)
print(pop_bicycles_end)
print(pop_bicycles_pre_end)

del bicycles[-1]
print(bicycles)

bad_bicycles='trec'
print(new_bicycles)
new_bicycles.remove(bad_bicycles)
print(new_bicycles)

print("\n")

#LOOP's
for on in to_loop_bicycles:
    print(f"Who is owner of {on.upper()}")

print("Thank you, everyone. That was a great magic show!")

#RANGE's

list_of_numbers = list(range(1, 20))
print(list_of_numbers)


list_of_square = []
for n in range(6):
    square = n ** 2
    list_of_square.append(square)

print(list_of_square)
print(min(list_of_square))    
print(max(list_of_square))    
print(sum(list_of_square))    

for n in range(7):
    list_of_square.append(n**2)
print(list_of_square)
print(min(list_of_square))    
print(max(list_of_square))    
print(sum(list_of_square))    

#SLICING

players = ['charles', 'nisko', 'martina', 'notikinta', 'elina', 'emanuele']
players_slice = players[0:2]
print(players_slice)
print(players[1:3])
print(players[1:])

print(players[-2:])

for n in players[:2]:
    print(n.title())

print(f"The first thee players in list is {players[0:2]}")

middle_index = len(players) // 2
print(middle_index)
print(f"The first thee players in list is {players[middle_index:middle_index+2]}")

first_pizza = ['kolbasa', 'testo', 'meet', 'chees', 'pipe']
print(first_pizza)
first_pizza.append('ogurec')
for n in first_pizza:
    print(n)
   

second_pizza = ['kolbasa', 'greep list', 'testo', 'egg', 'chees', 'pipe']
print(second_pizza)
second_pizza.append('rulets')
for n in second_pizza:
    print(n)







