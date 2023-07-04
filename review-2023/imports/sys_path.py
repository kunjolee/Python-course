import sys
# Primero va a a buscar en el folder del primer path para ver si el archivo que estoy importando existe ahi. Si si esta ahi, python va a tratar de usar ese path


# Si no existe en ese path, se va a ir al otro path que esta en la lista (una variable de entorno llamada PYTHONPATH), y asi suscesivamente hasta que llegue al ultimo path, y si no lo encuentra en el ultimo path va a raise an error

# eg. ['/Users/kunjolee/udemy/python/python-refresher/review-2023/imports', '/Library/Frameworks/Python.framework/Versions/3.11/lib/python311.zip', '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11', '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload', '/Users/kunjolee/udemy/python/bootcamp_100/25-pandas/env/lib/python3.11/site-packages']

print(sys.path)



# Al usar sys.modules, python mostrara todas las importaciones que hemos realizado, incluyendo las built in que vienen en python. Al momento de nosotros hacer una importacion python va a agregar el path de nuestra importacion a esta lista sys.modules, y si nosotros volvemos a importar un mismo modulo que ya esta dentro de sys.modules, python usara ese path, en vez de volver a importar, para evitar que el codigo vuelva a correr una y otra vez. y en vez de eso, simplemente usar el codigo que ya ha sido corrido

print(sys.modules)