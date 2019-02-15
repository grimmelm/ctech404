import stats

numbers = []

while True:
    print('Current list: ' + str(numbers))
    numbers.append(int(input('Enter another number: ')))
    average = stats.mean(numbers)
    print('The new average is: ' + str(average))
    if average >= 5:
        print('That is more than 5.')
        break
    else:
        print('That is less than 5. Keep trying!')
        
print('All done. You win!')