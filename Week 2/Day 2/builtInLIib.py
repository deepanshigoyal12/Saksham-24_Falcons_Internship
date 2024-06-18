import math

# Basic Math Functions
print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))
print("2 raised to the power of 3:", math.pow(2, 3))

# Trigonometric Functions
angle = math.pi / 4  # 45 degrees in radians
print("Sine of 45 degrees:", math.sin(angle))
print("Cosine of 45 degrees:", math.cos(angle))
print("Tangent of 45 degrees:", math.tan(angle))

# Logarithmic and Exponential Functions
print("Natural logarithm of 10:", math.log(10))
print("Base-10 logarithm of 1000:", math.log10(1000))
print("e raised to the power of 2:", math.exp(2))

# Constants
print("Value of pi:", math.pi)
print("Value of e:", math.e)


import random

# Basic Random Number Generation
print("Random float between 0 and 1:", random.random())
print("Random integer between 1 and 10:", random.randint(1, 10))

# Random Choice
options = ['apple', 'banana', 'cherry', 'date']
print("Random choice from list:", random.choice(options))
print("Three random choices from list:", random.choices(options, k=3))

# Shuffling
deck = list(range(1, 53))  # A deck of cards represented as numbers 1-52
random.shuffle(deck)
print("Shuffled deck:", deck)

# Seeding
random.seed(42)
print("Random number with seed 42:", random.random())

import statistics as s

l=[1,2,3,4,5,4,5]
print(s.mean(l))

print(s.median(l))

print(s.mode(l))

print(s.mode(l))

t=[1,2,3,4,5,4,5,5,5,4]
print(s.mode(t))


'''=========Doc string======'''

'''Doc string in python '''
# doc string => understand to wahat code we write 

def func():

    '''this is function about the printig the value 
    '''

print("hiii")

func()
