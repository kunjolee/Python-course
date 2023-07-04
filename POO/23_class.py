class Student:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def greet(self):
        print(self.name)
        print(self.lastname)
        print(self.age)

        if self.name == 'Kunjo':
            print('Estas aca logeado')
        else:
            print('Not logged')
    
kunjo = Student(name='Kunjo', lastname='Lee', age=19)
kunu = Student(name='kunu', lastname='Lee', age=29)


kunjo.greet()
kunu.greet()