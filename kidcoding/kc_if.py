temp = -1 # temperature value used to test

if temp < 0:
    print('Freezing...')
elif 0 <= temp <= 20:
    print('Cold')
elif 21 <= temp <= 25:
    print('Normal')
elif 26 <= temp <= 35:
    print('Hot')
else:
    print('Very Hot!')
