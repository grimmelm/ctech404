import sys

with open(sys.argv[1]) as f:
    text = f.read()
lines = text.split('\n')
for line in lines:
    print(line.split(' ')[0])
