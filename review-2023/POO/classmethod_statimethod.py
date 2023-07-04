# Instance methods are used the most (when we interact with self)
# Class method are used for factory
# static method are used to just place a method inside a class


class ClassTest:
    def instance_method(self):
        print(f"Called instance method of { self }")
    
    @classmethod
    def class_method(cls):
        # Using the decorator @classmethodmake this function to recieve the argument cls. this is the class itself
        print(f'Called class_method of { cls }')

    @staticmethod
    def static_method():
        # doesn't recieve either the self or cls as an argument.
        # Doesn't have anything related to the class. 
        print("Called static_method.")

# We don't have to pass anything as an argument and python will recognize that we are passing the class itself e.g "ClassTest.class_method(ClassTtest)""
ClassTest.class_method()

# Python won't pasa anything as argument

ClassTest.static_method()

print("\nExamples")
# Ejemplos

class Book:
    TYPES = ("hardcover", "paperback")
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}>, {self.book_type}, weighing{self.weight}g"

    # Create an instance object inside a classmethod
    @classmethod
    def hardcover(cls, name, page_weight):
        hardcover_type = cls.TYPES
        return cls(name=name, book_type = hardcover_type, weight=page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        _, paperback = cls.TYPES
        return cls(name=name, book_type = paperback, weight=page_weight)
    
book_hardcover = Book.hardcover("Harry Potter", 1500)
book_paperback = Book.hardcover("Pyhon 101", 600)

print(book_hardcover)
print(book_paperback)