"""Q1. A farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three
species:

chickens = 2 legs cows = 4 legs pigs = 4 legs The farmer has counted his animals and he gives you a subtotal for each
species. You have to implement a function that returns the total number of legs of all the animals.
"""

"""
Create a function that finds the highest integer in the list using recursion.
"""

"""
Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
The output should always be a string even if it is not a multiple of 3 or 5.
"""


def total_leg(chickens, cows, pigs):
    legs = 2 * chickens + 4 * cows + 4 * pigs
    return legs


def find_max(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        m = max(arr[1:])
        return m if m > arr[0] else arr[0]


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


if __name__ == '__main__':
    print(total_leg(3, 5, 7))
    arr = [3, 100, 4, 56, 67, 89, 23]
    print(find_max(arr))
    print(fizzbuzz(45))
