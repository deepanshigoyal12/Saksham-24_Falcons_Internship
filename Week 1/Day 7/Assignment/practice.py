#factorial

def factorial(num):
  if num < 0:
    print("Factorial is not defined for negative numbers.")
    return None  
  elif num == 0:
    return 1
  else:
    result = 1
    for i in range(1, num + 1):
      result *= i
    return result

# Example usage
number = 5
factorial_result = factorial(number)

#fibb
def fibonacci(n):
  
  if n <= 1:
    return n
  a, b = 0, 1
  for i in range(2, n + 1):
    c = a + b
    a, b = b, c  # Update values for next iteration
  return c

# Example usage
number = 10
for i in range(number):
  print(fibonacci(i), end=" ")  # Print each Fibonacci number
print()  

#gcd
def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

# Example usage
num1 = 12
num2 = 18
gcd_result = gcd(num1, num2)
print(f"GCD of {num1} and {num2} is: {gcd_result}")

