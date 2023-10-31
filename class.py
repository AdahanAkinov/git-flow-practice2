class Diary:
    def __init__(self, student):
        self.student = student
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)


class Subject:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.diary = None

    def set_diary(self, diary):
        self.diary = diary


# Examples

student1 = Student("Ada", 18)
diary = Diary(student1)

subject1 = Subject("Analysis")
subject2 = Subject("FYS")

diary.add_subject(subject1)
diary.add_subject(subject2)

subject1.add_student(student1)
subject2.add_student(student1)

print(student1.name)
print([subject.name for subject in diary.subjects])
