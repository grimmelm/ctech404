colors = []
color = input('Pick a color or type \'quit\': ')
while color != 'quit':
    colors = colors + [color]
    color = input('Pick a color or type \'quit\': ')
print('You picked: ' + str(colors))
