# Program to understand the use of Default Arguments

def studentExample1(name='unknown', age=0):
    print("name: ", name)
    print('age', age)


studentExample1()
studentExample1('tom')
studentExample1('tom', 22)


# Program to understand the use of *args(normal argumemts)

def studentExample2(name, age, *marks):
    print("name: ", name)
    print('age', age)
    print('marks', marks)
    for x in marks:
        print(x)  # Returns Tuple


studentExample2('tom', 22, 95, 70, 80, 50)


# Program to understand the use of **kwargs(keyword arguments) in Python

def studentExample3(name, age, **marks):
    print("name: ", name)
    print('age', age)
    print('marks', marks)
    for key, value in marks.items():
        print(key, ' ', value)  # Returns Dictionary


studentExample3('tom', 22, english=95, math=70, physics=80, biology=50)


# Program to understand the concepts of Encapsulation using Object Oriented Programming

class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def area(self):
        return self.__height * self.__width


rect1 = Rectangle(20, 60)
rect2 = Rectangle(50, 40)

print(rect1.area())
print(rect2.area())


# Program to understand the concept of inheritance and usage of access specifiers

class Polygon:
    __width = None  # declaration of private data members with double underscores
    __height = None

    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


class Rectangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height()


class Triangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height() / 2


rect = Rectangle()
tri = Triangle()
rect.set_values(50, 40)
tri.set_values(50, 40)
print(rect.area())
print(tri.area())


# Program to understand the use of Super Keyword and Multiple Inheritance in Python

class Parent:
    def __init__(self, name):
        print('Parent __init__', name)


class Parent2:
    def __init__(self, name):
        print('Parent2 __init__', name)


class Child(Parent2, Parent):
    def __init__(self):
        print('Child __init__')
        Parent2.__init__(self, 'max')
        Parent.__init__(self, 'tom')


print('-------------------Example 1--------------------')
child = Child()


class Child2(Parent):
    def __init__(self):
        print('Child __init__')
        super().__init__('max')


print('-------------------Example 2--------------------')
child2 = Child2()


# Program to understand the concept of Composition in Python

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus)  # Composition represents a "Part of" relationship

    def total_salary(self):
        return self.obj_salary.annual_salary()


emp = Employee('max', 25, 15000, 10000)
print(emp.total_salary())


# Program to understand the concept of Aggregation in Python

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.obj_salary = salary;

    def total_salary(self):
        return self.obj_salary.annual_salary()


salary = Salary(15000, 10000)
emp = Employee('max', 25, salary)  # Aggregation represents a "Has A" relationship
print(emp.total_salary())

# Program to understand the concept of Abstarct Classes in Python

from abc import ABC, abstractmethod  # ABC stands Abstract Base Classes


class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


square = Square(5)
print(square.area())
print(square.perimeter())

# Program to understand Operator Overloading in Python

import math


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, circle_object):
        return Circle(self.__radius + circle_object.__radius)

    def __lt__(self, circle_object):
        return (self.__radius < circle_object.__radius)

    def __gt__(self, circle_object):
        return (self.__radius > circle_object.__radius)

    def __str__(self):
        return "Circle area = " + str(self.area())


c1 = Circle(2)
c2 = Circle(3)
c3 = c1 + c2

print(c1.getRadius())
print(c2.getRadius())
print(c3.getRadius())

print(c1 < c2)
print(c3 > c2)

print(str(c1))
print(str(c2))
print(str(c3))
