# similar than parameters rest
# puede recibir n numeros de argumentos, y el parametro es un tuple

def my_function(*args):
    print(args)

my_function('Hello',2,3,4,23,23,{'hey': 'Kunjo'})

# podemos usar * para destructurar listas | tuples tipo spreed operator un js

num = [2,3]
print(*num)

def add (x,y):
    return x+y

print(add(*num))

# dictionaries with **

my_dictionary = {"x": 15, "y": 10}
def greet(x,y):
    print(x,y)

# python pasa el key del dictionario y su valio como argumentos (x: 15, y: 10)
greet(**my_dictionary)



def multiply(*args):
    total= 1
    print('Los args de multiple',args)

    return total

# haciendo esto es un tipo de sintaxis especial de python, donde va a recibir un monton de argumentos, y luego hasta el final tenemos que definir un keyword argument, si no definimos el keyword argument va a dar error.

def apply(*args, type):
    if(type == "+"):
        print('suma va',sum(args))
    elif type == "*": 
        multiply(*args)


apply(3,2,32,321323, type='*')



test=(1,2,1,43)
# this will spreed the tuple
print('Rapido tests',*test)

    