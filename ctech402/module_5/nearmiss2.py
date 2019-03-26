def near_miss_list(target, tolerance, guesses):
    for guess in guesses:
        if guess > target:
            difference = guess - target
        else:
            difference = target - guess
        if difference <= tolerance:
            return True
    return False


print('target = 5, tolerance = 1, guesses = [5,10,15]')
print(near_miss_list(5,1,[5,10,15]))

print('target = 5, tolerance = 1, guesses = [10,15]')
print(near_miss_list(5,1,[10,15]))
