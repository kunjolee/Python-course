users=[
    (0, "Bob",      "password"),
    (1, "Rolf",     "bob123"),
    (2, "Jose",     "longp4asword"),
    (3, "username", "1234"),
]

users_dictionary = { user[1].lower(): user for user in users }
print('This is users', users_dictionary)


username_input = input("Enter your username: ").lower()
password_input = input("Enter your password: ").lower()

try:
    _, username, password = users_dictionary[ username_input ]
    if password_input == password:
        print('Login correct!')
    else:
        print('incorrect loggin')
except Exception as e:  
    print("Not user founded", e)

