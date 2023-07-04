#Example 1
def divide (num1: int, num2: int):

    if (num2 == 0):
        raise ZeroDivisionError(f"Can't divide {num1} with 0")

    return num1 / num2

def calculator (*args, operator):
    # Using operator as a function. Very similar to a callback in JS
    return operator(*args)

res = calculator(20,2, operator = divide) # -> 10
res = calculator(50,3, operator = divide) # -> 20

print(res)


# Example 2


def search(sequence, expected, finder):
    for item in sequence:
        if finder(item) == expected:
            return item

    raise RuntimeError(f'{expected} not founded')

friends = [
    { "name": "Marlon", "age": 20 },
    { "name": "Cristian", "age": 20 },
    { "name": "Julio", "age": 19 },
]

friendFounded = search(friends, 'Julio', lambda friendParameter: friendParameter['name'])

print(friendFounded)


