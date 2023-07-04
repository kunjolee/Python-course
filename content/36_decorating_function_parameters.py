import functools

user = {"name": 'Juan', "role": 'admin'}

def make_secure(func):  

    @functools.wraps(func)
    # what we usually do is receive unlimited number of arguments
    def add_privacy(*args, **kwargs):
        if user['role'] == 'admin':
            return func(*args, **kwargs)
        else:
            return 'User not allowed to join here'

    return add_privacy


@make_secure
def getPassword (panel):
    if panel == 'admin':
        return '12345'
    elif panel == 'billing':
        return 'super_secure_function' 

# getPassword get replaced by add_privacy so what i'm doing here is that i'm passing the argument to the add_privacy function, and then what i need to do is to pass that argument that add_privacy function receives to func (which is my original function getPassword)

res = getPassword('billing')
print(res)

