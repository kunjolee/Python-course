class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ magic method is going to be called for you when you want to turn your  object into a string (printing the just instance of the class)

    # The purpose of this method is to return a nice easy to read object for the users
    def __str__(self):
        return f"{ self.name }, { self.age } years old"
    
    # Shows the programmers the class represented in a nicer string, this is call in a debugger or when we print the class (the str should not be defined for this method to be called wen we print the class | instance )

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

kunjo = Person('Kunjo', 19)
print(kunjo)