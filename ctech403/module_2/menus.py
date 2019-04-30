menus = {'Burgertopia': ['burgers', 'fries', 'shakes'],
               'Pizza Thyme': ['pizza', 'pasta'],
               'Taco Thursday': ['tacos', 'tortas']}

for restaurant in menus:
    dishes = ' and '.join(menus[restaurant])
    print (restaurant + ' serves ' + dishes)
