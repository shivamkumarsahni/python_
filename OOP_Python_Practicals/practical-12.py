# Practical 12: Create an Employee class

# Practical 12: Employee class

class Employee:
    count = 0

    def __init__(self, emp_no, name, dept, basic, da, hra):
        # Check for negative salary components
        if basic < 0 or da < 0 or hra < 0:
            raise SystemExit(
                "Error: Basic, DA and HRA cannot be negative."
            )

        self.emp_no = emp_no
        self.name = name
        self.dept = dept
        self.basic = basic
        self.da = da
        self.hra = hra

        Employee.count += 1

    # Calculate total salary
    def salary(self):
        return self.basic + self.da + self.hra

    # Decrease object count when an object is destroyed
    def __del__(self):
        if Employee.count > 0:
            Employee.count -= 1

    # Display employee details
    def __str__(self):
        return (
            f"Employee Number: {self.emp_no}\n"
            f"Name: {self.name}\n"
            f"Department: {self.dept}\n"
            f"Basic Salary: {self.basic}\n"
            f"DA: {self.da}\n"
            f"HRA: {self.hra}\n"
            f"Total Salary: {self.salary()}"
        )


# Create an employee object
emp1 = Employee(101, "Rahul", "IT", 20000, 5000, 3000)

print(emp1)
print("Total Employee Objects:", Employee.count)

