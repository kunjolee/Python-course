def divide(num1, num2):

    if num2 == 0:        
        raise ZeroDivisionError('Cannot divide by zero')

    return num1 / num2

    
grades=[59,80,90,100]
# grades=[]

print('Welcome to the calculator')

# they are executed in the following orders
try:
    divisor = divide(num1=sum(grades), num2=len(grades))

except ZeroDivisionError as e:
    print('No grades yet in your list:', e) 

else:
    # this will be executed only when try sucess, if when try the code it goes to the exception this line won't be executed
    print('My result is: ', divisor)
finally:
    print('Thank you!')
