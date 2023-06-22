# This is deliberately badly written and does not conform to python naming standards

from employee import Employee

def testemp1():
  e = Employee(name = "A N Other", title = "Manager", employee_id = "")
  assert e.salary == 25000
  
  
def testemp2():
  e = Employee(name = "A N Other", title = "Manager", employee_id = "")
  e.set_salary(250)
  assert e.salary == 250
