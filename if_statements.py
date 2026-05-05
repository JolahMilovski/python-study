cars = ['bmw', 'audi', 'SUBaru', 'TOyota', 'GEely', 'HOnda']

cars.sort()
for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car != 'audi':
        print(car.title())
    else:
        print(car.lower())
    
