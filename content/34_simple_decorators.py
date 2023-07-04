# This has to be private

# Estructura basica: 3 funciones (a,b,c)
# A es el decorador (make_secure)
# B es la funcion que queremos decorar (admin_password)
# C la funcion interior del decorador la cual tendra las nuevas funcionalidades que queremos darle a la funcion B, 

    # esta funcion C es la que el decorador va a retornar y asi a darle las nuevas funcionalidades a la funcion B

# Estructura

# A
def func_decoradora (myfunc):
    # C
    def function_interior():
        # Acciones adicionales que decoran

        print('Vamos a realizar un calculo: ')

        # B
        print(myfunc())
        print('terminamos la operaicon!')

    return function_interior

@func_decoradora

def my_sum():
    return 1+20

my_sum()



user = { "username": 'klee', "role": "guest" }

def admin_password() -> str:
    return '1234'


def make_secure(func):

    def secure_role():
        if user["role"] == 'admin':
            return func()
        else:
            return f'No admins permissions for the user {user["username"]}'

    return secure_role


admin_password = make_secure(admin_password)

print('here?',admin_password())