class ToManyReadPagesError(ValueError):
    pass

class Book:
    def __init__(self, name: str, page: int):
        self.name = name
        self.page = page
        self.page_read = 0

    def __repr__(self) -> str:
        return f'<Book { self.name } { self.page } { self.page_read }>'
    
    def add_read_pages (self, read): 

        if (self.page_read + read > self.page ):
            raise ToManyReadPagesError(
                'To many read pages error'
            )

        self.page_read += read


book1 = Book('Harry poter', 50)

try:

    book1.add_read_pages(30)
    book1.add_read_pages(30)
    print(book1)
    
except ToManyReadPagesError as e:
    print(e)
