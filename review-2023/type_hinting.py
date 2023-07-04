from typing import List

def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)
list_avg([123,3,23])



class BookShelf:
    pass

class Book:
    def __init__(self, name: str):
        self.name = name

    @classmethod
    def hardcover(cls) -> "Book":
        # si estamos retornando la misma clase en la que estamos actualmente, tenemos que poner el nombre de la clase entre comillas

        return cls("HEllo this is test")

    @classmethod
    def shelf(cls) -> BookShelf:
        # Si retornamos otra clase que esta ya creada, entonces podemos retornar el nombre de esa clase
        return cls()
book1 = Book(name="Python 101")


print(book1)

