def make_pizza(*toppings):
    """print all customer's toppings"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


def make_pizza2(size, *toppings):
    """show the toppings info"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

make_pizza2(16, 'pepperoni')
make_pizza2(12, 'mushrooms', 'green peppers', 'extra cheese')
