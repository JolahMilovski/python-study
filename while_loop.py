current_number = 5
while current_number < 10:
    print(current_number)
    current_number += 1
    print(current_number)


#break
someone=""
print("Input someone and I repeat it\n If you input is STOP, I stop it")
while someone != 'STOP':
    someone = input()
    if someone == 'STOP':
        break
    print(someone)

#continue
print("input number smoller than 20")
current_number = int(input())

while current_number < 20:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


unconfirmed_user = ["qwe", "asd", "wer", "ert", "ert"]
confirmed_user =[]

while unconfirmed_user:
    current_user = unconfirmed_user.pop(0)
    confirmed_user.append(current_user.upper())
print(confirmed_user)


car = ["bmw", 'audi', "WV", "bmw", 'asd', "wer","bmw", "ert"]

while 'bmw' in car:
    car.remove("bmw")

print(car)


responses = {}

polling_active = True

while polling_active:

    name = input(f'What is your name ?\n')
    response = input(f"Which mountain would you like?")

    responses[name] = response

    print(f'Whoild you like to respond another people (yes|no)?')
    yes_no = input()
    if yes_no == 'yes':
        continue
    polling_active = False

    print(responses)

