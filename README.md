Problem Set Zero
================
Written by: Computer Science Department, The Pingry School
Solved by: YOUR NAME HERE
<!-- The next line includes the build-passing or build-failing logo from travis-ci You may change it slightly to get the correct logo to show up for your repository -->
[![Build Status](https://travis-ci.org/Pingry-Python/ps0-with-testing.svg?branch=master)](https://travis-ci.org/Pingry-Python/ps0-with-testing)

About Problem Sets
------------------
A problem set is a series of classic problems in an introductory programming course. For these exercises, you must write your own functions from scratch. So you may not, for example, import a python function from another module, or use typecasting to make a problem trivial. You will have about a week to complete a problem set, and a small amount of class time to work on the project.


Submission
----------
This problem set will be submitted by pushing to github. Begin by accepting this assignment which will create your own repository. After cloning your repository to your local system, you can start solving the problems. The file structure is already sketched out for you.


Grading
-------
Most of the grade for a problem set will come from automated testing of the code. Examples of automated tests are available to you throughout your development, so if you want to see how your code is doing with the tests, come see me for details.

|Grade Category | Points Earned|
| --- | --- |
| Automated Tests | 15 pts |
| README and .gitignore files | 2 pts |
| Progressive Commits | 1 pt |
| Coding Style and Readability | 2 pts|

| Grade Penalty | Points Deducted |
| --- | --- |
| Importing Restricted Functions | 1 pt each |
| Casting to string in numberic problems | 1 pt each |
| Not calling `sum_digits` from `digit_sum_is_factor` | 1 pt|

The Problems
------------
### is_even
Write a boolean function that takes a non-negative integer as a parameter and returns True if the number is even, False if it is odd.

### num_digits
Write a function that takes a non-negative integer as a parameter and returns the number of digits in it. You may not cast to string to solve this problem. Zero is a zero-digit number.

### sum_digits
Write a function that takes a non-negative integer as a parameter and returns the sum of its digits.

### sum_less_ints
Write a function that takes a non-negative integer as a parameter and returns the sum of all the integers that are less than the given number.

For example:
```
>>> sum_less_ints(3)
3  # which is 1 + 2

>>> sum_less_ints(5)
10 # which is 1 + 2 + 3 + 4
```


### factorial
Write a function that takes a non-negative integer as a parameter and returns its factorial.

For example:
```
>>> factorial(3)
6  # because 6 = 3 * 2 * 1

>>> factorial(5)
120 # because 120 = 5 * 4 * 3 * 2 * 1
```

### is_factor
Write a boolean function that takes two positive integers as parameters and figures out whether the second number is a factor the first. In other words, returns true if the second number divides into the first number evenly, and false otherwise.

### is_prime
Write a boolean function that takes an integer greater than or equal to 2 as a parameter and returns whether the number is a prime.

### is_perfect
Write a boolean function that takes a positive integer as a parameter and returns whether the number is perfect. A perfect number is a number that equals the sum of proper its proper factors. A proper factor is any factor except the number itself.

For example:
```
>>> isPerfect(6)
True # because 6 = 1 + 2 + 3
```

### digit_sum_is_factor
Write a boolean function that takes a positive integer as a parameter and returns true if the sum of the digits of the number divides evenly into the number, false otherwise. You MUST call the sum_digits function you wrote in question 2 to define this function.

