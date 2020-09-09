import datetime

class Employees:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.__greeting = "Hello!" #Private Property

        Employees.num_of_emps += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __privateMethod(self):
        print(self.__greeting)

    def publicMethod(self):
        self.__privateMethod()

    ################# Class and Static Methods ###############################
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    ##########################################################################

    ################# Special (Magic/Dunder) Methods #########################

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullName, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullName)

    ##########################################################################

    ################# Property Decorators: Getters, Setters, Deleters #######
    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    @fullName.setter
    def fullName(self, name):
        self.first, self.last = name.split(" ")

    @fullName.deleter
    def fullName(self):
        print("Deleted Name!")
        self.first, self.last = None, None

    #########################################################################

###################### Inheritance ##########################################

class Developer(Employees):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # equivalent to Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employees):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullName)

#############################################################################

#Testing
emp_1 = Employees("Foxlooo", "Omega", 50000)
emp_2 = Employees("Mary", "Lu", 60000)
print(emp_1.__dict__)
#emp_1.__privateMethod() This line will Error out
#print(emp_1.__greeting) This will Error out
emp_1.publicMethod()
print()

################### Testing Class Methods and Static Methods #######################
print("Class Methods and Static Methods: ")
emp_str_1 = "John-Doe-70000"
new_emp_1 = Employees.from_string(emp_str_1)
print(str(new_emp_1))

my_date = datetime.date(2016, 7, 10)
print(Employees.is_workday(my_date))
print()
####################################################################################

################## Testing Special (Magic/Dunder) Methods ##########################
print("Special Methods:")
print(repr(emp_1))
print(str(emp_1))
print(emp_1 + emp_2)
print(len(emp_1))
print()
####################################################################################

########## Testing Property Decorators: Getters, Setters, Deleters #################
print("Decorators: ")
print(emp_1.fullName)
print(emp_1.email)

emp_1.fullName = 'Corey Schafer'
print(emp_1.fullName)
print(emp_1.email)

del emp_1.fullName
print(emp_1.fullName)
print()
####################################################################################

############################# Testing Employees ####################################

dev_1 = Developer('Corey', 'Schafer', 50000, "Python")
# print(help(Developer))
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(str(dev_1))

print()
mgr1 = Manager("Sue", "Smith", 90000, [emp_2])
mgr1.add_emp(dev_1)
mgr1.remove_emp(emp_2)
mgr1.print_emps()

print(isinstance(mgr1, Employees))
print(isinstance(mgr1, Developer))
print(issubclass(Developer, Employees))
####################################################################################