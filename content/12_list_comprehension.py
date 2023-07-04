numbers = [1,2,3,4,5,6,7,8,9,10]

doubled = []

# List comprehension: A way to create a new list using a for loop

# consist of brackets containing the expression, which is executed for each element of the foor loop that is itering over each element of a list

# First you put what you want to add to your new list, Then you write your for loop

# sintax: newList = [expression(element) for element in oldList if condition]

plus_2_numbers = [ x * 2 for x in numbers]

print('Plus 2 numbers',plus_2_numbers)

even_numbers = [ x for x in range(1,11) if x % 2 == 0]

print(f'even numbers from 0 to 10 { even_numbers }')


friends = ['Sam', 'Samantha', 'Samuel']

start_s = [ friend for friend in friends if friend.startswith('S') ]

print(start_s)

print(id(friends), id(start_s))

