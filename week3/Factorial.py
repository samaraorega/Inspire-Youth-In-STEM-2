#Write a programme to print the factorial of a number using functions
import math
def factorial(n):
    for i in range(0,n):
        fact_n = n * (n-i)
        return fact_n
    
print(factorial(3))

import math
def fact(n):
    return(math.factorial(n))
num = int(input("Enter the number"))
f = fact(num)
print("Factorial of " ,num, "is" ,f)
 
#Write a programme to calculate simple interest
# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.
 
 
def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
     
    si = (p * t * r)/100
     
    print('The Simple Interest is', si)
    return si
     
simple_interest(50000, 6, 8)