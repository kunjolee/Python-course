# They are Key pair values. A key can be any kind of hashable type (string, int)

friend_ages = {
    'Kunjo': 19,
    'Julio': 29,
    'Jonatan': 19
}

# Get and item of my dictionary

print(f'printing just one {friend_ages["Kunjo"]}')
print(friend_ages)

# Add a key or change an existing key

friend_ages['Brandon'] = 24
print(friend_ages)

print('\nList of dictionaries: ')

list_soccer_players = [
    { 'name': 'Cr7', 'age': 38 },
    { 'name': 'Neymar', 'age': 31 },
    { 'name': 'Mesi', 'age': 34 },
    { 
        'otherDictionary': { 
            'name': 'Brandon',
            'age': 12
        } 
    }
]


print(list_soccer_players)
print(list_soccer_players[3]['otherDictionary'])

print('\nIterating a dictionary: ')

students_attendance = { "Rolf": 97, "Bob": 80, "Anne": 100 }
# I get the key 
for student in students_attendance:
    print(f'{ student }: { students_attendance[student] } ')
    
# A better way of doing this
for student, attendance in students_attendance.items():
    print(f'My student: { student }: {attendance}')
# We can use in keyword with a dictionary to check if x is in a dictionary (we can verify only the keys)
print('\nIf statement with a dictionary: ')
# By doing this we are only verifying the keys of our dictionary
if 'Bob' in students_attendance:
    print(f'Bob: { students_attendance["Bob"] }')
else: 
    print('Bob is not a studen in this class')

print('\nGet only the values of a dictionary: ')
# This will return an array with the values
attendance_values = students_attendance.values() #This is a list
attendance_average = sum(attendance_values) / len(attendance_values)
print( f'The average of attendance {attendance_average}' )
