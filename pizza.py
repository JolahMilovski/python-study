def make_pizza(size, *topping):
    print(f'\n Making a {size} pizza with the following toppings: ')
    for t in topping:
        print(f" - {topping}")