# Program to understand the use of __name__ keyword

def add(a, b):  # if we import this function in some new python file then all the print statements will be executed
    return a + b


print(__name__)
if __name__ == "__main__":  # but this line indicates that we are currently in this file and would not affect the
    print(add(1, 9))  # the new file where we imported this file. The "main" works similar to the main function
    # in Java and C++.

# Program to understand the working of JSON data in Python

import json

a = {
    'name': 'max',
    'age': 22,
    'marks': [90, 50, 60, 80],
    'pass': True,
    'object': {
        'colour': ('red', 'blue')
    }
}
print(json.dumps(a, indent=4, sort_keys=True))  # dictionary along with indentation and in sorted order
print(json.dumps(["1", "2"]))  # List
print(json.dumps(("1", "2")))  # Tuple
print(json.dumps("Hello World"))  # String
print(json.dumps(100))  # Integer
print(json.dumps(15.56))  # Float
print(json.dumps(False))  # Boolean
print(json.dumps(True))
print(json.dumps(None))  # Null value

with open('demo.json', 'w') as fh:  # for creating and writing in a JSON file
    fh.write(json.dumps(a, indent=4))
with open('demo.json', 'r') as fh:  # for reading an existing JSON file
    json_str = fh.read()
json_value = json.loads(json_str)
print(type(json_value))
print(json_value['name'])

# Program to understand Exception Handling in Python

result = None
a = float(input('Number 1: '))
b = float(input('Number 2: '))

try:
    result = a / b
except ZeroDivisionError as e:
    print("ZeroDivisionError = ", type(e))
except TypeError as e:
    print("TypeError = ", type(e))
finally:
    print('__finally__')

print('Result = ', result)


# Program to raise exceptions in Exception Handling

class CoffeeCup:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            # print('Coffee Too Hot')
            raise Exception('Coffee Too Hot ')
        elif self.__temperature < 65:
            # print('Coffee Too Cold')
            raise ValueError('Coffee Too Cold ')
        else:
            print('Coffee Ok to Drink')


cup = CoffeeCup(10)
cup.drink_coffee()

# Program to raise custom exceptions in Exception Handling

class CoffeeTooHotException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class CoffeeTooColdException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class CoffeeCup:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            raise CoffeeTooHotException('Coffee Temperature:' + str(self.__temperature))
        elif self.__temperature < 65:
            raise CoffeeTooColdException('Coffee Temperature:' + str(self.__temperature))
        else:
            print('Coffee Ok to Drink')


cup = CoffeeCup(70)
cup.drink_coffee()
