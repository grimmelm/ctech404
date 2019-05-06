birds = {}

f = open('birds-repeats.txt')
for line in f:
    fields = line.split()
    bird_name = fields[0]
    bird_count = int(fields[1])
    if bird_name in birds:
        birds[bird_name] = birds[bird_name] + bird_count
    else:
        birds[bird_name] = bird_count
f.close()

for bird_name in birds:
    if birds[bird_name] > 5:
        print('There are more than 5 ' + bird_name + 's')
