# Similar a los parametros rest
# Puede recibir n numero de argumentos, "arg" es una tuple
def multiply( *args ):
    total = 1
    for arg in args:
        total*=arg
    return total

print(multiply(2,3,5))

# Podemos usar * con una lista | tuple al llamar una funcion, para destructurar los valores de la lista | tuple y asignar esos valores como argumentos

def add(num1, num2):
    print(num1+num2)
    return num1 + num2 

numbers = [1,2]

add(*numbers)


# **dic. Pasar valores a named arguments usando diccionarios. 
# El 'key' del diccionario va a ser el nombre de el argumento.
# El 'value del diccionario va a ser el valor del argumento


my_dic = {"x": 15, "y": 16}

def greet(x,y):
    print('hello', x,y)

greet(**my_dic)

# Una sintaxis especial en python. si tenemos un *args y seguido agregamos otro parametro, los ultimos parametros seran tomados como keyword arguments

# Parametros: *args, name, test -> name y test seran keyword arguments

def apply(*args, operator):
    if operator == '*':
        res = multiply(*args)
    elif operator == "+":
        res = sum(args)
    else:
        res = "NO valid operator to apply"
    return res

print("Multiplied",apply(1,3,5, operator="*"))
print("Sum",apply(1,3,5, operator="+"))
