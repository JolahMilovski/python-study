from employee import Employee
import pytest

@pytest.fixture
def test_employee():
    print("созали учетную ведомость")
    emp = Employee("Nisk","Brown", 15000)
    return emp

def test_emp(test_employee):

    assert test_employee.annual_salary == 15000
    test_employee.give_raise()

    assert test_employee.annual_salary == 20000
    assert test_employee.bonus_for_annual_salary == 22000

    