"""
>In this module we are going to Discuss ___________________Inheritance_____and__________Type of inheritance_____________
💫 Inheritance ✅
💫 Multipal Inheritance
💫 Multi level Inheritance
💫 method Overriding in python
💫 Operator Overloading in python
💫 MRO Method Resolution in python
💫 Super() function in Inheritance
💫 💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫 Today in this module only [introduction].💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫
"""

# Inheritance : -
# Inheritance is fundamental concept of an OOPs that allow to create a new class based on existing class


# Parents class : -
# Parents class is the class in which we inherit attributes(property) and method to the child class
# It is commonly known as Existing class, superclass, parent class or  base class


# Child class : -
# Child class is a class that inherits properties (attributes) and methods from another class.
# It is commonly known as new class, subclass, child class or derived class .

# Note : -
# We use override method in child class from parents class means modify the behaviour of __init__().
# To do this modification we define an __init__() method in the child class. and if we want to keep
# the parent's constructor behavior, call the parent's __init__() using super() function


# Why use inheritance :-
# It promotes code reusability and helps organize your code by creating a hierarchy of related classes.
# It provides modularity, maintenance, polymorphism and Efficiency Boost in the programs.


# What is Super function : -
# super() is a built-in function that provides a way to access methods of a parent class from a child class
# super() allows to call a method in the parent class that we are overridden in the child
# when we call super(), it doesn't return a value directly. it returns a proxy object that allows you to call methods from a parent or superclass.
# super() uses the method resolution order (MRO) to find the next class in line.
# It’s especially useful in multiple inheritance to ensure cooperative method calls.


# CODES/SYNTAX : -
class MyClass:
    """this is base class"""
    def __init__(self):
        self.name = "person"

class UrClass(MyClass):
    """this is child class"""
    def detail(self):
        self.roll = 25
        return f"Name : {self.name} Age : {self.roll}"

_get = UrClass()
print(_get.detail())



# CODES/SYNTAX : -
class ParentsClass:
    """this is parents class"""
    def __init__(self, *arg):
        self.value = arg

class ChildClass(ParentsClass):
    """this is child class"""

    def __call__(self, *args, **kwargs):
        self.result = args
        return f"The value of {self.value} is : {self.result[0]}"

_vlu = ChildClass("laptop", "pen", "paper")
print(_vlu(30)) # this line trigger __call__



# CODES/SYNTAX : -
class OldClass:
    """this is super class"""
    def __init__(self, var):
        self.var = 30

class NewClass(OldClass):
    """this is child class"""
    def __init__(self, args):
        super().__init__(args)
        self.arg = 50
obj = NewClass(50)
# var and arg is accessible via arg
print(obj.var ,obj.arg)

