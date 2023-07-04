import functools

user = {"name": 'Juan', "role": 'admin'}

def make_secure(func):  

    # This function (add_privacy) is the one that will replace the function you want to decorate. So it also changes the name and documentation of the function we are decorating

    # This is telling add_privacy to not change the name of the functions is decorating | Also that i'll wrap add_privacy into func without changing the name
    @functools.wraps(func)
    def add_privacy():
        if user['role'] == 'admin':
            return func()
        else:
            return 'User not allowed to join here'

    return add_privacy


# getPassword get replaced by add_privacy function
@make_secure
# By the decorator changing the name of our origin function (getPassowrd). can be a bit of a problem because some libraries uses the name internally. In order to fix it we need to pass other decorator to function #C which is add_privacy 
def getPassword ():
    return '12345' 

res = getPassword()


print(getPassword.__name__)
