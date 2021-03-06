import abc


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(abc.ABC):
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    @abc.abstractmethod
    def calc_bonus(self):
        pass

    @abc.abstractmethod
    def get_hours(self):
        pass


class Manager(Employee):
    def __init__(self, code, name, salary,
                 departament=Department('managers', 1)):
        super().__init__(code, name, salary)
        self.__departament = departament

    def calc_bonus(self):
        return self.salary * 0.15

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, name):
        self.__departament.name = name

    def get_hours(self):
        return 8


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, sale):
        self.__sales += sale

    def calc_bonus(self):
        return self.__sales * 0.15
