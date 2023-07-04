class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    # Todos los metodos in python tienen que recibir el parametro 'self object' que es el mismo el que creamos en el metodo init
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    
student1 = Student(name="Kunjo", grades=(83,43,32))
student2 = Student("bob", (23,100,99))

print(student1.average_grade())
print(student2.average_grade())


# How it works internally with methods. call the method inside of the class and then pass the object that we created as a self
# print(Student.average_grade(self=student1))

# Python does it internally for us so we can just call the method with the object we just created, and then python asign the self parameter as the object that is calling the method. e.g student1.average_grade()
