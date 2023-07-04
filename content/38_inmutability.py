# Almost all things are mutable in python, expect for tuples, strings, integers, booleans and floats

a = []
b = a

b.append('heee')

print(id(a))
print(id(b))


print(a)
print(b)
