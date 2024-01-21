from operator import attrgetter

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age


a = Student('Alice', 'A', 15)

name, grade, age = attrgetter('name', 'grade', 'age')(a)

assert name == 'Alice'
assert grade == 'A'
assert age == 15
