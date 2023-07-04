

list = [1,2,3,4,5]

data = { 'Here_' + str(x): x for x in  list }

print(data)



users = [
    (0, 'kunjo', '1234' ),
    (0, 'lee', '1334' ),
    (0, 'saul', '122134' )
]

usersdata = { user[1]: user for user in users}

print(usersdata)

input_name = input('Insert your name: ')
input_pass = input('Insert your password: ')


print(usersdata[input_name])

_, name, password = usersdata[input_name]

if(password == input_pass):
    print('Logged!')
else:
    print('not credentials')


