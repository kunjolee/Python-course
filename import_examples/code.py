def divide(my_list) -> float:
    return sum(my_list) / len(my_list)


print('Im in code file: ',__name__)

# Importando todo el modulo
# Cuando se importa un archivo de un directorio, se tiene que crear un __init__.py file para que especialmente en versiones antiguas de python pueda reconocer que esa carpeta es un module y de ahi vamos a importar algos
import libs.module 