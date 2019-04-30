import sys

if len(sys.argv) < 3:
    sys.exit('Too few arguments!')
elif len(sys.argv) > 3:
    sys.exit('Too many arguments!')

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print(num1 + num2)
