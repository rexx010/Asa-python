class Student:

    class_year = 2021
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 21)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)



print(student1.class_year)
print(Student.class_year)
print(Student.num_students)