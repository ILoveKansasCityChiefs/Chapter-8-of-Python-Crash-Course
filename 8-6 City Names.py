def city_country(city, country):    
    """Return a dictionary of information about city country pairs"""
    areas = {'city': city, 'country': country}
    return areas

pair1 = city_country('Tokyo', 'Japan')
print(pair1)
pair2 = city_country('New York City', 'New York')
print(pair2)
pair3 = city_country('Paris', 'France')
print(pair3)
