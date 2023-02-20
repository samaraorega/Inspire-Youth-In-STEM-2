numbers = (1,2,3,4,5,6,7,8,9,10)
sum_num = 0
for number in numbers:
    sum_num = sum_num + number

avg_num = sum_num / 10
print("The average ofthe numbers:",avg_num)

numbers = []
sum_num = 0

print("Enter first 10 numbers")
for number in range(0,10):
    num = int(input("Inout number: "))
    numbers.append(num)
    sum_num = sum_num + numbers[number]

print("Total of the list: ",sum_num)
avg_num = sum_num / len(numbers)
print("Average of list: ",avg_num)