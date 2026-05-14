import random
#   die and sides
class Die:

    def __init__(self, sides = 6):
        self.sides = sides  
        
    def roll_die(self): 
        number = random.randint(1, self.sides)
        print(f" Now side is {number}")

die_rollig = Die(100)
die_rollig.roll_die()

# Lottery    


lottery = []

for n in range(10):
    num = random.randint(1, 10)
    sumbol = chr(random.randint(97, 122))
    lottery.append(num)
    lottery.append(sumbol)

print(f"список {lottery}")

    #   random.shuffle(lottery)
    #   print(f"перемешали список {lottery}")
    #   print("Взяли 3 случайных")
    #   print(lottery[:3])


win_num = 0

#while win_num != 4:
#    my_ticket = []
#    for n in range(2):    
#        num = random.randint(1, 10)
#        sumbol = chr(random.randint(97, 122))
#        my_ticket.append(num)
#        my_ticket.append(sumbol) 
#
# проверка вхождения каждого элемента в список
# for i in my_ticket:
#    if i in lottery:
#        win_num += 1


    
    # проверка вхождения всех элементов в список через метод all()
while win_num != 4:
    my_ticket = []

    for n in range(2):    
        num = random.randint(1, 10)
        sumbol = chr(random.randint(97, 122))
        my_ticket.append(num)
        my_ticket.append(sumbol)     

    if all(item in lottery for item in my_ticket):
        win_num = 4
        break


print(f"{win_num} значений в билете совпало ")
print(f"Числа моего билета {my_ticket}")
