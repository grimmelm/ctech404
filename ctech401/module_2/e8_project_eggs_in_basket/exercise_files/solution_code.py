total_eggs = int(input('How many eggs do you have? '))
cartons = total_eggs // 12
left_over = total_eggs % 12

print('Number of filled Cartons:')
print(cartons)
print('Number of eggs left over:')
print(left_over)
