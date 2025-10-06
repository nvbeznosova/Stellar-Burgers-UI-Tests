class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, reset_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = reset_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None and rest_days is not None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment
    
    def salary(self):
        return self.hours * self.hourly_payment 

emp1 = EmployeeSalary.get_hours(name="Nadia", hours=None, rest_days=5, email="nadia@email.com")
print(emp1.name, emp1.hours)

emp2 = EmployeeSalary.get_email(name="Denis", hours=25, rest_days=2, email=None)
print(emp2.name, emp2.email)

print(emp1.salary())

EmployeeSalary.set_hourly_payment(600)
print(emp1.salary())