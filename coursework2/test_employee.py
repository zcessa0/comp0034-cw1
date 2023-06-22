# Deliberately badly written and with inappropriate test case names

@pytest.fixture
def emp():
    e = Employee(name="A N Other", title="Manager", employee_id="12345")
    return e


def testemp1(emp):
    assert emp.department == "HR"


def testemp2(emp):
    emp.calculate_salary(250)
    assert emp.salary == 250
