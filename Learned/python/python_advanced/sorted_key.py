from operator import itemgetter
from operator import attrgetter

sample_dict = {
    1:'D',
    2:'B', 
    3:'C', 
    4:'E', 
    5:'A',
    }


class Student():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def __repr__(self):
        return repr((self.name, self.age, self.score))


print(sorted(sample_dict.items(), key=lambda x: x[1]))
print(sorted(sample_dict.items(), key=lambda x: x[1], reverse=True))
print(sorted(sample_dict.items(), key=itemgetter(0)))
print(sorted(sample_dict.items(), key=itemgetter(1)))


student_objects = [
    Student('John', 20, 100), 
    Student('Doe', 21, 90), 
    Student('Lee', 22, 80),
    ]

sorted_by_name = sorted(student_objects, key=attrgetter('name'))
sorted_by_name - sorted(student_objects, key=lambda x: x.name)
sorted_by_age = sorted(student_objects, key=attrgetter('age'))
sorted_by_name - sorted(student_objects, key=lambda x: x.age)
