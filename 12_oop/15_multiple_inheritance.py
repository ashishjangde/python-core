class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class dancer:
    def __init__(self, style):
        self.style = style

    def display(self):
        print("Dance style:", self.style)

class dancer_employee(employee, dancer):
    def __init__(self, name, salary, style):
        employee.__init__(self, name, salary)
        dancer.__init__(self, style)

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Dance style:", self.style)
        
de = dancer_employee("John", 20000, "Hip-Hop")
de.display()