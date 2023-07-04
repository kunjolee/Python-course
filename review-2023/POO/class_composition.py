# You will use composition much more than inheritance
# Composition Allows your classes to be simpler, and reduces the complexity of your code overall
# Composition es tener una clase que contiene muchas otras clases


# Inheritance: book is a bookshelf too
# composition: bookshelf has many books



class BookShelf:
    # La logica aca es tengo una biblioteca que va a recibir muchas intancias de clase libro y vamos a contar cuantos libros tengo
    # *books is tuple that has a bunch of books instances
    def __init__(self, *books):
        self.books = books;

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book { self.name }"
    
book1 = Book("Python1")
book2 = Book("Python2")


shelf = BookShelf( book1, book2 )

print(shelf)
for x in shelf.books:
    print(x)