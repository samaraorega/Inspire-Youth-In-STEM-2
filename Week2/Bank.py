#Write a programme that calculates 16% tax income
#Ranging between 100k and 150k

#19% tax income is between 150k and 300k
#30% tax income is above 300k
#5% if income is less than 100k
#print gross income , net income 

#Formulae gross_income = net income + taxes

net_income = int(input("Enter your net income:"))

#above 300k
if(net_income >= 300000):
    gross_income = net_income + ((30/100)*net_income)
    print("Since your net income is {} your gross income is {} ".format(net_income, int(gross_income)))

#150k to 300k
elif(net_income >= 150000) & (net_income < 300000):
    gross_income = net_income + ((19/100)*net_income)
    print("Since your net income is {} your gross income is {} ".format(net_income, int(gross_income)))

#100k to 150k
elif(net_income >= 100000) & (net_income < 150000):
    gross_income = net_income + ((16/100)*net_income)
    print("Since your net income is {} your gross income is {} ".format(net_income, int(gross_income)))

#1 to 100k
elif(net_income >= 1) & (net_income < 100000):
    gross_income = net_income + ((5/100)*net_income)
    print("Since your net income is {} your gross income is {} ".format(net_income, int(gross_income)))

else:
    print("Invalid")