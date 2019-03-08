class Department:
    def __init__(self, name):
        self.name = name
        self.employees = set()
    def register_employess(self, employee):
        self.employees.add(employee)
    def unregister_employees(self, employee):
        self.employees.remove(employee)
    def notify(self, message):
        for x in self.employees:
            x.display(message)


