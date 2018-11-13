class Employee:
    nextIdNum = 0

    def __init__(self, name):
        self.name = name
        self.id = Employee.nextIdNum
        Employee.nextIdNum += 1


    def get_name(self):
        return str(self.name)

    def weekly_pay(self, hours_worked):
        return 0

    # see if ID number is greater than other
    def __lt__(self, other):
        return self.id < other.id


class Nonexempt_Employee(Employee):

    def __init__(self, name, hourly_rate):
        Employee.__init__(self, name)
        self.hourly_rate = hourly_rate

    # Overrides the superclass method.
    def weekly_pay(self, hours_worked):
        pay = 0
        if hours_worked < 40:
            pay = (hours_worked * self.hourly_rate)
        else:
            pay = (40 * self.hourly_rate)
            pay += (hours_worked-40) * (self.hourly_rate * 1.5)
        return round(pay,2)

class Exempt_Employee(Employee):
    def __init__(self, name, annual_salary):
        Employee.__init__(self, name)
        self.annual_salary = annual_salary
    def weekly_pay(self, hourly_rate):
        return round(((self.annual_salary)/52),2)


class Manager(Exempt_Employee):
    def __init__(self, name, annual_salary, bonus):
        Exempt_Employee.__init__(self, name, annual_salary)
        self.bonus = bonus
    def weekly_pay(self, hourly_rate):
        return round(((self.annual_salary+ self.bonus) / 52),2)



def main():
    all_employees = []
    p1 = (Nonexempt_Employee("Aaron Wendell", 40.0))
    p2 = (Exempt_Employee("Alden Pexton", 60000.0))
    p3 = (Manager("Allison Fernandez", 94000.0, 50.0))
    all_employees.append(p1)
    all_employees.append(p2)
    all_employees.append(p3)
    print(p2 < p1)

    for employee in all_employees:
        hours = int(input("Hours worked by " + employee.get_name() + ": "))
        pay = employee.weekly_pay(hours)
        print("Salary: ", pay)



if __name__ == '__main__':
    main()
