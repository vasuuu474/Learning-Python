class Employee:
    def __init__(self, employee_name, employee_id, salary):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.salary = salary
    def increase_salary(self, amount):
        if amount > 0:
            self.salary += amount
        else:
            print("Increase amount must be positive.")
    def display_details(self):
        print("----- Employee Details -----")
        print(f"Name: {self.employee_name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")
        print("-----------------------------")

name = input("Enter Employee Name: ")
id = int(input("Enter Employee id : "))
sal = float(input("Enter Salary Amount : "))

employee1 = Employee(name,id,sal)
employee1.display_details()

inc_sal = float(input("Enter Salary Increase Amount : "))
employee1.increase_salary(inc_sal)
employee1.display_details()