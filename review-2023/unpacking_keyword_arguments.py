# **variable collects keyword arguments and convert them into a dictionary
# They can be used in a fuction to collect keywords arguments into dictionary or they can be used in a function called, to unpacked a dictionary into keyword arguments

def named(**kwargs):
    # Parametro convertido a diccionario **kwargs
    print(kwargs) # -> {'name'="kunjo", 'lastname'='lee' "} 
named(name="kunjo", lastname="lee")

# unpacked dictionary into keywords arguments - takes the key of the dictionary as the name of the argument, and the value of the dictionary key as the value of keyword argument

def named2(name, age ):
    print('named2',name, age )
details_for_named2={'age': "my_age",'name': "my_name"}
# convierte el dictionario a keyword arguments 
named2(**details_for_named2) # -> named2(age="my_age..", name="my_name")

def greet1(**kwargs):
    # este parametro es convertido a diccionario
    print('greet1',kwargs)
# este diccionario es convertido a keyword arguments
greet1(**{'hello': "im saying hello"}) #-> greet1(hello="i'm saying hello")


def named3(**kwargs):
    print('im in named3',kwargs)

def print_nicely(**kwargs):
    named3(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")
print_nicely(name="Bob",age=20)


# BOTH: *args, **kwargs. args should go first before kwargs, this is used to accept unlimited number of arguments 
def both(*args, **kwargs):
    print(kwargs) # -> args = (1,2,4)
    print(args) # -> {"name":"bob", "age": 25}

both(1,2,4, name="Bob", age="df")