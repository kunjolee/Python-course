# Brackets are only needed when you specify python that you want a tuple there, otherwise you can omit the brackets

# Destructuring: with tuples you can get the value of the tuple by declaring a variable in the same order as the tuple. They have to have the same number of values
# e.g: name, lastname, profession = ( 'Kunjo','Lee','Developer' )

# When you use a '_' as a variable. It means that you don't care about that variable (That is what python community has decided) 

x = 5,11
print(x)

student, attendance = 'My student favorite', 100
print( student, attendance )
print('\n\n')


for name, lastname in [('Kunjo', 'Lee'), ('Jonatan','Lee')]:
    print(f'{ name }: {lastname}')

people = 'Pedro', 28, 'Valencia'

name, _ , country = people

print(name, country)

# * asteric with destructuring means that we want to separate a list into another list

# if we put an asterisc at the beginning, it is going to separate the first item of the list and the other items are going to be added to another list

# if we put an asterisc at the end of the list, it is going to separte the last item of a list and the other first items are going to be added to another list


first, *rest = [1,2,3,4,5,6,7]
print(rest)

*rest2, last = [1,2,3,4,5,6,7]

print(rest2)

