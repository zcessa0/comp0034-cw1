# Sample code for testing

class Employee:

    def __init__(self, name, employee_id, title):
        self.name = name
        self.employee_id = employee_id
        self.title = title
        self.department = department
        self.salary = salary

    def calculate_salary(self, salary, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.salary = self.salary + (overtime * (self.salary / 50))

    def assign_department(self, emp_department):
        self.department = emp_department

    def __str__(self):
        return '{} , id={}, is in {} and is a {}.'.format(self.name, self.employee_id, self.department, self.title)
