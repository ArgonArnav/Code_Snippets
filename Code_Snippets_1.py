# Program for finding the greatest number

numbers = [2,5,7,8]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# Program to remove duplicates from a List

numbers = [1,2,2,4,3,2,5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# Program to understand use of dictionaries

phn = input("Phone: ")
mobile = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for ch in phn:
    output += mobile.get(ch, " X") + " "
print(output)

# Program to understand the use of random package, functions and classes

import random

class Dice:
      def roll(self):
         first = random.randint(1,6)
         second = random.randint(1,6)
         return (first, second)


dice = Dice()
print(dice.roll())

# Program to understand path files

from pathlib import Path

path = Path()
for file in path.glob('*.py'): # (* means all files)
    print(file)
