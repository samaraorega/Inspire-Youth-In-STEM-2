'''print("***The values below are odd numbers***")
for odd_numbers in range(1,101):
    if(odd_numbers%2 != 0):
        print(odd_numbers)

print("***The values below are even numbers***")
for even_numbers in range(1,101):
    if(even_numbers%2 == 0):
        print(even_numbers)
'''
S = 1
E = 100
for num in range(S, E+1):
    if num>1:
        for i in range(2,num):
            if(num % i==0):
                break
        else:
            print(num, end=" ")