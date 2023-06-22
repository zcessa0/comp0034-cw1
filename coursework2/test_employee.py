# Deliberately badly written and with inappropriate test case names

@pytest.fixture
def empfixt():
    e = Employee(name="A N Other", title="Manager", employee_id="12345")
    return e


def testemp1(e):
    assert e.department == "HR"


def testemp2(e):
    e.calculate_salary(250)
    assert e.salary == 250
