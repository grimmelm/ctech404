def near_miss(target, tolerance, guess):
    if guess > target:
        difference = guess - target
    else:
        difference = target - guess
    if difference <= tolerance:
        return True
    else:
        return False

print('target = 5, tolerance = 1, guess = 5')
print(near_miss(5,1,5))

print('target = 5, tolerance = 1, guess = 10')
print(near_miss(5,1,10))

print('target = 5, tolerance = 10, guess = 10')
print(near_miss(5,10,10))
