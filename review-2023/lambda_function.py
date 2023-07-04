# function that doesn't have name and is only used to operate inputs and return outputs. They are almost never usted to perform actions

# Lambda functions are meant to be short functions without giving them a name

add = lambda x, y: x+y
print("Normal add",add(5,2))

sequence = [1,3,5,9]

# We use list comprenhension over map in python
doubled = [ (lambda x: x * 2)(x) for x in sequence ]
doubled2 = list(map( lambda x: x * 2, sequence ))

print("List comprenhension", doubled)
print("Map", doubled2)

def test(x):
    return x * 2

print("Normal function map", list(map( test, sequence )))
print("Normal function list comprenhension", [ test(x) for x in sequence ])