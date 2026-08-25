def sandwiches(*toppings):
    print(f"\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

sandwiches('Provolone', 'Cheddar')

sandwiches('Turkey')

sandwiches('Bacon')
