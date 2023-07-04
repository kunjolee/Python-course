# Importaciones: corre otro archivo y me permite utilizar lo que esta dentro de ese archivo

# __name__ is a global variable in Python that changes depending on which file you're in

# when you run a file. __name__ will be __main__ and for the others files will be the name of the file
# in some PYthon versions we have to create a __init__ file inside any folder i want to import from 

# puedes correr folder y files as long as they are in your "sys.path"
# Importing from a folder usually requires __init__.py file to be defined specially in older python versions

from mymodule import testmodule

testmodule()

print("Printing __name__ in main", __name__)
