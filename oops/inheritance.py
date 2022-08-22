class Person(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))

# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        super().__init__( name, idnumber)

    # def details(self):
    # 	print("My name is {}".format(self.name))
    # 	print("IdNumber: {}".format(self.idnumber))
    # 	print("Post: {}".format(self.post))

    def details(self):
        super().details()
        print('-'*100)
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()

print('-'*100)

class Base:
    def __init__(self):
        self.a = 'test'
        self._b = 'b value'
        self.__c = 'c value'
        # print(self.a, self._b, self.__c)

class Derived(Base):
    def __init__(self):
        super().__init__()
        # super(Derived, self).__init__(x)
        print(self._b)

obj = Derived()
# print(obj.a, obj._b)

# print(obj._Base__c)

print(issubclass(Derived, Base))
print(isinstance(obj, Derived))

print('-'*100)

class Base:
    def __init__(self):
        print("In base class")

class Base1(Base):
    pass
    # def __init__(self):
    #     print("In base1 class")

class Derived(Base1):
    def __init__(self):
        # super().__init__()
        super(Derived, self).__init__()
        print("In Derived class")

obj = Derived()

print('-'*100)


# class object1(object):
#     def foo(self):
#         print("Object foo is c/d")

class ParentOne(object):
    def foo(self):
        print("ParentOne foo is c/d")

class ParentTwo(object):
    def foo(self):
        print("ParentTwo foo is c/d")

class Child(ParentOne, ParentTwo):
    def foo(self):
        print('call from child foo')

    def call_from_parent_one(self):
        # print(Child.__mro__)
        return super(ParentOne, self).foo()

    def call_from_parent_two(self):
        # pass
        return super(ParentTwo, self).foo()

    def call_from_super(self):
        return super(Child, self).foo()


obj = Child()
obj.call_from_parent_one() # return ParentTwo foo is c/d
obj.call_from_super()
obj.call_from_parent_two()

# child->one->two->obj

'''
    https://stackoverflow.com/questions/41356378/python-multiple-inheritance-calling-base-class-function

    Python constructs a method resolution order (MRO) when it builds a class. The MRO is always linear.
    If python cannot create a linear MRO, then a ValueError will be raised. In this case, your MRO
    probably looks like:

        Child -> ParentOne -> ParentTwo -> object

    Now when python see's a super(cls, self), it basically looks at self and figures out the MRO.
    It then uses cls to determine where we are currently at in the MRO and finally it returns an object
    which delegates to the next class in the MRO. So, in this case, a super(Child, self) call would
    return an object that delegates to ParentOne. A super(ParentOne, self) class would return an
    object that delegates to ParentTwo. Finally a super(ParentTwo, self) call would delegate to object.
    In other words, you can think of super as a fancier version of the following code:

    def kinda_super(cls, self):
        mro = inspect.getmro(type(self))
        idx = mro.index(cls)
        return Delegate(mro[idx + 1])  # for a suitably defined `Delegate`

    Note that since super(ParentTwo, self) returns a "Delegate" to object, we can see why you're
    getting an AttributeError when you try super(ParentTwo, self).foo() -- Specifically the reason
    is because object has no foo method.
'''