def make_car(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car = make_car('Toyota', 'Camry',
                color='Red',
                wheels='Star')

print(car)
