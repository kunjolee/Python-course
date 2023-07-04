# Vamos a crear un decorador que reciba parametros, para eso necesitamos crear una funcion que recibe el parametro que queremos y luego retorne el decorador
import functools

# Esta es una funcion que recibe un parametro personalizado
def make_secure(roleType):
    # El decorator A
    def decorator(func):

        def privateAccess():
            print('hey ', roleType)
            func()
            print('hey2')

        return privateAccess 

    return decorator
            

@make_secure('role type')

def hey():
    print('Hey in the middle')
hey()


@make_secure('aaaaaaaa')
def heyBoth():
    print('\n\nHey both everyone')
    
heyBoth()