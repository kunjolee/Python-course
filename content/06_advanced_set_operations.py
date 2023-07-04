my_abroads_friends = {'Julio', 'Michael', 'eee'}

my_friends = {'Karli', 'Julio', 'Joanne'}

# Difference method va a agarrar el set que se esta aplicando el metodo y luego lo va a comparar con el set que se pase como argumento, si un item dentro de los sets se repite sera quitado del set que esta aplicando el metodo, generando un nuevo set

local_friends = my_friends.difference(my_abroads_friends)

print('Here',local_friends)

# Union of sets

friends = my_friends.union(my_abroads_friends)

print(friends)

# intersection will return a set with the items in a set that repeats its value

both = my_friends.intersection(my_abroads_friends)

print(both)