# Importando una funcion en especifico
from code import divide

divide([2,3,4,2])



# build in constant that prints __main__ in the file is running and on other files will say the path of that file
print('Iam in imports file',__name__)


# Python primero mira a el path del current directory, lo segundo que mira python al importar es si esta definida una variable de entorno llamada PYTHONPATH(si no esta definida pasa al step siguiente). Despues ya mira a todos los demas directorios 

