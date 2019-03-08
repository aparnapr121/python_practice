from observer_pattern.observer_pattern.department import Department
from observer_pattern.observer_pattern.employees import Employee

dep1 = Department("Accounting")
dep2 = Department("Operations")
emp1 = Employee("Aparna", dep1)
emp2 = Employee("Anisha", dep2)
emp3 = Employee("Arjun", dep1)
emp4 = Employee("Roshan", dep1)
emp3.change_department(dep2)