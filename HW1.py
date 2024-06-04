# AAE 718 Week 01 Python Basics
# Rachel Mu

# Problem 1
# Write a function called hello that takes one input, a string, and returns the string
# "Hello input 1, my name is your name". 

def hello(name):
    return f"Hello {name}, my name is Rachel."

# Test
hello("Rick")

# Problem 2
# Write a function called divisible that returns a list of all numbers 0 to 10,000 that
# are divisible by the input number.
# For example, if the input is 2, the output is [0, 2, 4, ..., 10000].
# I recommend using a single list comprehension. I also suggest you google the phrase “Python modulo
# operator” you’ll see %. It’ll be useful.

def divisible(x):
    return [n for n in range(10001) if n % x == 0]

# Test
divisible(2000)

# Problem 3
# Write a function called remove none with a single dictionary input and returns a
# dictionary with no values on None.

def remove_none(input):
    return {key: value for key, value in input.items() if value is not None}

# Test
remove_none({"a": 1, "b": "Mitch", "c":None})

# Probleme 4
# Write a function called length that finds the length of a list.
# Do not use the built-in “len” function.
# The one input is a list and the one output is a number

def length(list):
    count = 0
    for _ in list:
        count += 1
    return count

# Test
length([1,2,3,5,8])

# Problem 5
# Write a function called my reverse that reverses a list.
# Do not use the built-in “reverse” function.
# The one input is a list and the one output is also a list.

def my_reverse(list):
    return list[::-1]

# Test
my_reverse([1,2,3,4])


# Problem 6 (5 pt) Write a function that finds the minimal element of a list.
# Do not use the built-in “min” function.
# The function should be called my min. The one input is a list and the output is a number.

def my_min(list):
    value = list[0]
    for item in list[1:]:
        if item < value:
            value = item
    return value

# Test
my_min([2,8,5,7,1,4])


# Problem 7
# Write a function called written numbers that returns a dictionary 
# whose keys are integers less than the input and values are strings.


def written_numbers(input): 
    dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten"}
    return {i: dict[i] for i in range(input+1)}

# Test
written_numbers(5)


# The input is a number, for this problem we can assume the number is positive and less than 1000. So
# your function should work for any integer between and including 0 and 999.


def number_names(n):

    name = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
        40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
        80: "eighty", 90: "ninety", 100: "hundred"
    }

    hundreds = n // 100
    tens = (n % 100 // 10) * 10
    digits = n % 10

    if n <= 20 or n % 10 == 0:
        # ex. 12: twelve
        return name[n]
    
    elif n < 100:
        # ex. 58: fifty eight
        return name[tens] + name[digits]

    elif tens == 0 and digits == 0:
        # ex. 300: three hundreds
        return name[hundreds] + " hundreds"
        
    elif tens == 1:
        # ex. 615: six hundred and fifteen
        return name[hundreds] + " hundred and " + name[n % 100]
        
    else:
        # ex. 521: five hundred and twenty one
        return name[hundreds] + " hundred and " + name[tens] + " " + name[digits] 

# Test
number_names(521)

# now correctly outputs "five hundred and twenty one"
# so next I just need to incorporate this into my original function
# I'll upload this file for now (tornado warning!!!) and might come back to revise it later
# my laptop was heating up too badly so I needed to come to the library to borrow a loaner
# and now a couple dozen of us are all in the library basement 


# Problem 8
# Write a function called fizzbuzz. There should be one input, a positive integer n
# and output a string. The function will iterate over all integers from 0 to n − 1 if the integer is a multiple
# of 3, add fizz to the output, if it’s a multiple of 5, add buzz and if it’s a multiple of both 3 and 5, print
# fizzbuzz. Don’t forget the newline character “\n” at the end of each line

def fizzbuzz(n):
    result = ""
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            result += "fizzbuzz \n"
        elif i % 3 == 0:
            result += "fizz \n"
        elif i % 5 == 0:
            result += "buzz \n"
    return print(result)

# Test
fizzbuzz(16)


