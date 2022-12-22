from abc import ABCMeta, abstractmethod, ABC

# abc can contain both method, abstract and normal function
class Employee(ABC):
    @abstractmethod
    def create(self):
        pass


class HR(Employee):
    def create(self, name):
        print(f"HR {name} is created")

class Engineer(Employee):
    def create(self, name):
        print(f"Engineer {name} is created")


class EmployeeFactory(object):
    @classmethod
    def createEmployee(cls, designation, name):
        eval(designation)().create(name)

if __name__ == '__main__':
    EmployeeFactory.createEmployee('Engineer', 'Vikas')
