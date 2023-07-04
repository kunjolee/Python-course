# Obtener valores del inicio de un list y separarlo de los demas (los demas valores seran una nueva list)

numbers=[1,2,3,4,5,6,7,8,9]
one,two, *rest1 = numbers
print(one, two, rest1)

# Obtener ultimo(s) valor de un list y separarlo de los demas (los demas valores seran una nueva list)

*rest2, eight ,nine = numbers
print(rest2, eight, nine)


print('\n')


# Los parentesis no son necesarios al definir una tuple, solo si queremos espeficiar a fuerza que es una tuple 

# e.g1
z = 1,2,3,4,5,5,5
tuple1 = 5,1
x,y = tuple1

print(x,y)
print('\n')

# e.g2
student_attendance = { "Rolf": 96, "Bob": 80, "Anne": 100 }

for student, attendance in list(student_attendance.items()):
    print(student, attendance)

print('\n')

# e.g3
list1=["a","b","C"]

for counter, letter in enumerate(list1):
    print(counter, letter)
 
print('\n')

# e.g4

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
for name, age, profession in people:
    print(f"Name: { name }, Age: { age }, Profession: { profession } ")

print('\n')

# when you want to ignore one variable you use _

person = ("Bob", 43, "Mechanic")
  
name, _, profession= person

print(f"Hi i'm { name } and i do { profession }")



