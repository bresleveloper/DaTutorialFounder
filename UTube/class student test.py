class Student(object):
    name = ""
    age = 0
    major = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

def make_student(name, age, major):
    student = Student(name, age, major)
    return student




s1 = Student("a", 1, "b")

print(s1.name)

s1.bik = "bik"
print(s1.bik)
