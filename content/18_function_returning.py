# None en python means, no value, missing value or undeclared value 
# by default function returns none 

#is not recommended to return 2 types of data in a function in python

def divide(num1,num2=2):
    if num2 != 0:
        return num1 /num2
    else: 
        return 'you fool'

res = divide( 10, 0 )

print(res)