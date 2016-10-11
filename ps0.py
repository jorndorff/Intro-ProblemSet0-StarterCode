
# 0. Write a boolean function that takes in a positive integer or zero as a parameter and returns whether the number is odd or even.
def is_even(number):
  return number % 2 == 0


# 1. Write a function that takes a non-negative integer as a parameter and returns the number of digits in it.
def num_digits(number):
  digits = -1
  quotient = 1
  
  # This loop will divide by increasing powers of 10
  while quotient >= 1:
    digits += 1
    powerOfTen = 10 ** digits
    quotient = number / powerOfTen
    
  return digits
  

# 2. Write a function that takes a non-negative integer as a parameter and returns the sum of its digits.  
def sum_digits(number):
  
  sum = 0
  currentPlace = num_digits(number) -1
  
  while number > 0:
    placeValue = 10 ** currentPlace
    currentDigit = number // placeValue
    sum += currentDigit
    
    # Update number so it is only the unused portion
    number -= currentDigit * placeValue
    currentPlace -= 1
    
  return sum
  
  
# 3. Write a function that takes a non-negative integer as a parameter and returns the sum of all the integers that are less than the given number.
def sum_less_ints(number):
  
  sum = 0
  
  for i in range(number):
    sum += i
  
  return sum
  

# 4. Write a function that takes a non-negative integer as a parameter and returns its factorial.
def factorial(number):
  product = 1
  for i in range(1, number + 1):
    product *= i
    
  return product


# 5. Write a boolean function that takes two positive integers as parameters and figures out whether the second number is a factor the first.
def is_factor(first, second):
  return first % second == 0


# 6. Write a boolean function that takes a positive integer as a parameter and returns whether the number is a prime.
def is_prime(number):
  isPrime = True
  for i in range(2, number):
    if number % i == 0:
      isPrime = False
      
  return isPrime


# 7. Write a boolean function that takes a positive integer as a parameter and returns whether the number is perfect.
def is_perfect(number):
  factorSum = 0
  for i in range(1, number):
    if is_factor(number, i):
      factorSum += i
  
  return number == factorSum


# 8. Write a boolean function that takes a positive integer as a parameter and returns true if the sum of the digits of the number divides evenly into the number, false otherwise.
def digit_sum_is_factor(number):
  sum = sum_digits(number)
  return number % sum == 0


  
  


