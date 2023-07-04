from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = []): #<- never do this
        self.name = name
        self.grades = grades

    def add_grades(self,grade: int):
        self.grades.append(grade)


kunjo = Student('Kunjo')

bob = Student('Bob')

kunjo.add_grades(69)

print(kunjo.grades)
print(bob.grades)