class Student:
    def __init__(self, name, school, *args, **kwargs):
        print("inside super class initializer")
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, args, kwargs)


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        print("inside sub class constructor")
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


anna = WorkingStudent('Anna', 'Oxford', 60000, 'Software Engineer')
friend = WorkingStudent.friend(anna, 'Greg', 55000, job_title='Software Engineer')

print(friend.name)
print(friend.school)
print(anna.salary)
print(friend.salary)