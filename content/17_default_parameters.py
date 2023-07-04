# default parameters must go at the end, if they go first and then you create a required parameter is going to give you an error e.g (x=7,y)


# not recommended

default_y = 3

def sum(x, y=default_y):
    print(x+y)


sum(3)

default_y = 5

# this will still print 6. it does not change the value y even though default value changed, because when sum was defined, the value of default was 3. so that default value is not going to change

sum(3)