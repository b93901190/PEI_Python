

class Student(object):
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __lt__(self, other):
        return self.name < other.name


students = [Student('A', 4.0), Student('B', 2.0), Student('C', 3.1), Student('D', 3.9)]

studentsSortedByName = sorted(students)

print 'students : ', [n.name for n in students]
print 'studentsSortedByName : ', [n.name for n in studentsSortedByName]

students.sort(key=lambda student : student.gpa, reverse=True)

print 'studentsSortedByGPA : ', [(n.name, n.gpa) for n in students]
