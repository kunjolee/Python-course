# in keyword works with lists,tuples,sets and also with strings


my_string = 'Hey i am kunjo'

print('a' in my_string)
print('llh' in my_string)

if ('a' in my_string):
    print(f'You just join here arent you')

user_input = input('Insert your letter: (y/n) ')

if(user_input in ('y','Y')):
    print('It worked! :)')
else:
    print('It didnt work :(')