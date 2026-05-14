def person_of_sandwiches(*item):
    for i in item:
        print(i)

person_of_sandwiches('asdf','wert','dfgh','xcvb')

def make_car(manufac, model_name, **other_value):
    car = {
        'manufacturer':manufac,
        'car model':model_name,
        **other_value
        }
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
    