import stats

my_list = [4,1,5,7,6,8,9,10,8,3,3,8,12]


mean  = stats.mean(my_list)
print('The mean is: ' +  str(mean))

median = stats.median(my_list)
print('The median is: ' +  str(median))

range = stats.range(my_list)
print('The range is: ' +  str(range))

std_dev = stats.standard_deviation(my_list)
print('The standard deviation is: ' + str(std_dev))
