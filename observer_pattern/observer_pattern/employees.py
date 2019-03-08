from observer_pattern.observer_pattern.department import Department
class Employee:
    def __init__(self, name, department: Department):
        self.name = name
        self.department = department
        self.department.register_employess(self)


    def change_department(self,new_dept):
        old_department = self.department
        self.department = new_dept
        old_department.unregister_employees(self)
        self.department.register_employess(self)
        message = f"{self.name} moved from {old_department.name} to {self.department.name}"
        self.department.notify(message)


    def display(self,message):
        print(f"{self.name} received the message", message)



