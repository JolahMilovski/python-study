cars = ['bmw', 'audi', 'SUBaru', 'TOyota', 'GEely', 'HOnda']

cars.sort()

for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car != 'audi':
        print(car.title())
    else:
        print(car.lower())
    
username = ['mike','bunnue','admin','nelson', 'broute', 'elizabeth']

for user in username:

    if len(username) == 0:
        print("Nobody at home")
    elif user == 'admin':
        print(f'Hi {user.title()}, come on!')
    else:
        print(f'Hi {user.upper()}, come on!')


new_user = ['nike','bannue','admin','nelsn', 'broute', 'elizabety']

not_in_new_user=[]

for nu in new_user:
    if nu in username:
        print(f"Hi {nu.upper()}")
    else:
        not_in_new_user.append(nu)

print(not_in_new_user)    



