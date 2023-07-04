# What do you want to put into your new list, for the variable you're using in array

numbers=[1,2,3,4,5,6,7,8,9,10]
# similar a usar un map
doubled_numbers = [ x * 2 for x in numbers]

print(doubled_numbers)


# If statement within a list comprenhension

friends=["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), "starts_s", id(starts_s))


# Examples


persons = [
    {
        "id": 1,
        "name": 'brandon',
        "lastname": "lee"
    },
    {
        "id": 13,
        "name": 'Kunjo',
        "lastname": "lee"
    },
    {
        "id": 134,
        "name": 'jonatan',
        "lastname": "ramirez"
    },
    {
        "id": 12,
        "name": 'eeee',
        "lastname": "lee"
    },
    {
        "id": 11,
        "name": 'kenia',
        "lastname": "mendez"
    },
    {
        "id": 125,
        "name": 'roberto',
        "lastname": "pascual"
    },
]

# filter de solo la familia lee
family_lee = [ x for x in persons if x['lastname'] == "lee" ]

print(family_lee)