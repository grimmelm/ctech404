import sys

with open(sys.argv[1]) as f:
    text = f.read()
lines = text.split('\n')
print(lines)
