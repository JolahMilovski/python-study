from employee import Employee


def calc_payroll():
    emp = Employee("Nisk","Brown", 15000)
    print(f"\n Расчитыем оклад {emp.first_name} {emp.last_name}")
    emp_give_rise = emp.give_raise()
    print(emp_give_rise)

calc_payroll()