 This is deliberately badly written and does not conform to good practice for test case naming standards
import pytest

from employee import Employee


@pytest.fixture
def emp():
    e = Employee(name="A N Other", title="Manager", employee_id="12345", salary=45000)
    return e


def testemp1(emp):
    assert emp.department == "HR"


def testemp2(emp):
    result = emp.calculate_monthly_salary(hours_worked=155)
    assert result == 3875


def testemp3(emp):
    emp.salary = 9000
    assert emp.salary == 9000


def testemp4(emp):
    emp.salary = 19575.67
    assert emp.salary == 19575.67


def testemp5(emp):
    with pytest.raises(ValueError) as e:
        emp.salary = 14999
