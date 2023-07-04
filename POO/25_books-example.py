class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self):
        return f'<Book {self.name} {self.book_type} {self.weight}>'

    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.TYPES[0], weight + 100)

    @classmethod
    def paperback(cls, name, weight):
        return cls(name = name, weight = weight, book_type=cls.TYPES[1])

book1 = Book.hardcover('Harrpy potter', 232) # <- this is the same than doing Book(...arguments)

book2 = Book.paperback(name='test', weight=100)

print(book1)
print(book2)
