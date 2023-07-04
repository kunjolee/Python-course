# These are considered magic methods cause python calls them for me
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
bob = Person(name="Bob", age=32)
# i'll print a representation of the object
print(bob) #-> <__main__.Person object at 0x104fc8c10> 

# two reasons for printing an object
# 1. for users: to show them about the object
# 2 for programmers  so they can see the object information

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        # this method gets called for you when you want to turn your object into string
        # print a nice easy to read object for users
        return f"Person { self.name }, {self.age} years old"
    

    def __repr__(self) -> str:
        # print out an unambiguous representation of the object. we can return a nice string for programmers, this method is being called when running a debugger
        return f"<Person('{self.name}', {self.age})>"

kunjo = Person2("Kunjo", 19)

print(kunjo)
    