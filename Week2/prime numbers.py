number = int(input('Enter a number'))
if number <= 1:
    print('You must enter a number greater than 1')
else:
    div, count = 2.0

while div <= number / 2 and count == 0:
    if number% div == 0:
        count += 1
    div += 1

if count == 0:
    print('Prime number')