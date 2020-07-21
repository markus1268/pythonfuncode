temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C, 32.3C etc.) : ")
degree = float(temp[:-1])
unit = temp[-1]

if unit.upper() == 'C':
    degree_str = 'Celsius'
    result = (degree * 9/5) + 32
    result_str = 'Fahrenheit'
elif unit.upper() == 'F':
    degree_str = 'Fahrenheit'
    result = (degree - 32) * 5/9
    result_str = 'Celsius'
else:
    print('Wrong input format!')
    quit()
#print('%.2f %s is: %0.2f %s' %(degree, degree_str, result, result_str))
#print('{:.2f} {:s} is: {:.2f} {:s}'.format(degree, degree_str, result, result_str))
print(f'{degree:.2f} {degree_str:s} is: {result:.2f} {result_str:s}')
