# Keywords arguments get collected into the **kwargs parameter and converts this kwargs parameter into a dictionary. The keyword argument name is now this key of the dictionary and the keyword argument value as the value of the dictionary key

# ** are used only with dictionaries

# I need to pass only keywords arguments
def example1 (**kwargs):
    print(kwargs)

example1(positional='witho7ut', then='keywords arguments')

# Unpacking dictionary into named(keywords) arguments

def example2 (name,age):
    print('Here',name,age)

my_dictionary = { "name": 'Look at this', "age": 19 }

example2(**my_dictionary)

# converts this kwargs as a dictionary
def example3(**kwargs):
    print('Are you here???',kwargs)
    print('Are you here??? :/',kwargs.items())


my_dictionary2 = {"hey": "Let me say something", "hello": "this is a greet"}

# convertis this dictionary as a keywords parameters hey='Let me say something', hello='this is a greet'
example3(**my_dictionary2)


# Print them to look nicer

def named(**kwargs):
    # I'll print a dictionary
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for randomfirst,randomesecond in kwargs.items():
        print(f'{ randomfirst }: { randomesecond }')

print_nicely(name='Samuel de luto', age=30)



# Unlimited number of arguments (using * args and **kwargs)
# error: **kwargs, *args.,... *args should go first
def both(*args, **kwargs):
    print(args)
    print(kwargs)

# both(hey='Imkunjo', 43, 32,21 <- esto da error, primero tienen que ir positional args

# porque convierte en tuple todos los positional arguments y los keyword arguments en dictionary
both(2,3,2,3,4,5,5, hey='Imkunjo', greet='I want to greet you' )


def bothTwo (*args, **kwargs):
    print(args, type(kwargs))


bothTwo(test="1", test2="2")

def tests(hello):
    print('random thuin s ',hello)

dictionary={"hello": 'nems'}
tests(**dictionary)

