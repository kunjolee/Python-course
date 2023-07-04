from typing import List

# Only python 3.5 above
def test1( name: str ) -> str:
    return f"Hello I am { name }"

print(test1('Hey'))



class Book: 
    def __init__(self, name: str, age: int):
        print(name, age)

    def list_items() -> List:
        return []

    @classmethod 
    def list_books(cls) -> 'Book': #Here is saying return a Book object class
        return cls('Kunjo', 28)



Book.list_books()