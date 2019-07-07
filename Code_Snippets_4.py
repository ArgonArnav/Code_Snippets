# Program to understand the concept of Iterators

# in order to create our own Iterator class, we need to implement __iter__() and __next__() methods in your class.

class ListIterator:

    def __init__(self, list):
        self.__list = list
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index == len(self.__list):
            raise StopIteration
        return self.__list[self.__index]


a = [1, 2, 3, 6, 5, 4]
mylist = ListIterator(a)
it = iter(mylist)

for i in it:
    print(i)


# Program to understand the use of Generators

# Python Generators  Example 1
def my_generators_func1():
    yield 'a'
    yield 'b'
    yield 'c'


x = my_generators_func1()

print(next(x))
print(next(x))
print(next(x))


# Python Generators  Example 2
def my_generators_func2():
    for i in range(5):
        print('--------', i)
        yield i


x = my_generators_func2()

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


# Python Generators  Example 3
def list_iterator(list):
    for i in list:
        yield i


a = [1, 2, 3, 6, 5, 4]
mylist = list_iterator(a)

for x in mylist:
    print(x)

# Program to understand the use of argparse and Command Line Arguments

import argparse

if __name__ == '__main__':
    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="my math script"
    )

    # Add the parameters positional/optional
    parser.add_argument('-n', '--num1', help="Number 1", type=float)
    parser.add_argument('-i', '--num2', help="Number 2", type=float)
    parser.add_argument('-o', '--operation', help="provide operator", default='+')

    # Parse the arguments
    args = parser.parse_args()
    print(args)
    result = None
    if args.operation == '+':
        result = args.num1 + args.num2
    if args.operation == '-':
        result = args.num1 - args.num2
    if args.operation == '*':
        result = args.num1 * args.num2
    if args.operation == 'pow':
        result = pow(args.num1, args.num2)

    print("Result : ", result)

# Program to understand the concept of Lambda, Filter, Reduce and Map in Python

from functools import reduce

double = lambda x: x * 2
add = lambda x, y: x + y
product = lambda x, y, z: x * y * z

print(double(10))
print(add(10, 20))
print(product(10, 20, 30))

# filter, reduce and map
my_list = [2, 5, 8, 10, 9, 3]
my_list2 = [1, 4, 7, 8, 5, 1]

a = map(lambda x: x * 2, my_list)
print(list(a))
b = map(lambda x, y: x + y, my_list, my_list2)
print(list(b))

c = filter(lambda x: x % 2 == 0, my_list)
print(list(c))

d = filter(lambda x: True if x >= 5 else False, my_list)
print(list(d))

e = reduce(lambda x, y: x + y, my_list)
print(e)
