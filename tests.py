from unittest import TestCase
import ps0 as s

#TODO Unit tests are supposed to test individual units right?
# So how do I test functions that call other function? If the deeper call
# fails, the shallower call shouldn't necessarily.

#TODO I had experimented with the timeout decorator as a quick-and-dirty test
# for infinite loops. Figure out whether travis automatically detects that
# or I need to reimplement it myself.


class TestIsEven(TestCase):
  
  def test_zero(self):
    p = s.is_even(0)
    self.assertTrue(p)
  
  def test_three(self):
    p = s.is_even(3)
    self.assertFalse(p)
    
  def test_eight(self):
    p = s.is_even(8)
    self.assertTrue(p)
    
#  def test_float(self):
#    with self.assertRaises(TypeError):
#      s.is_even(2.5) 
    
#  def test_negative(self):
#    with self.assertRaises(ValueError):
#      s.is_even(-6)
    
    

class TestNumDigits(TestCase):

  def test_zero(self):
    digits = s.num_digits(0)
    self.assertEqual(digits, 0)
    
  def test_five(self):
    digits = s.num_digits(5)
    self.assertEqual(digits, 1)
    
  def test_ten(self):
    digits = s.num_digits(10)
    self.assertEqual(digits, 2)
    
  def test_thousands(self):
    digits = s.num_digits(1331)
    self.assertEqual(digits, 4)
    
#  def test_negative(self):
#    with self.assertRaises(ValueError):
#      s.num_digits(-12)
      


class TestSumDigits(TestCase):
  
  def test_zero(self):
    sum = s.sum_digits(0)
    self.assertEqual(sum, 0)
    
  def test_five(self):
    sum = s.sum_digits(5)
    self.assertEqual(sum, 5)
    
  def test_twelve(self):
    sum = s.sum_digits(12)
    self.assertEqual(sum, 3)
    
  def test_thousands(self):
    sum = s.sum_digits(1673)
    self.assertEqual(sum, 17)
    
#  def test_negative(self):
#    with self.assertRaises(ValueError):
#      s.sum_digits(-34)
 
    
    
class TestSumLessInts(TestCase):

  def test_zero(self):
    sum = s.sum_less_ints(0)
    self.assertEqual(sum, 0)
    
  def test_one(self):
    sum = s.sum_less_ints(1)
    self.assertEqual(sum, 0)
    
  def test_five(self):
    sum = s.sum_less_ints(5)
    self.assertEqual(sum, 10)
    
#  def test_float(self):
#    with self.assertRaises(TypeError):
#      s.sum_less_ints(1.5) 
    
#  def test_negative(self):
#    with self.assertRaises(ValueError):
#      s.sum_less_ints(-34)  
  
class TestFactorial(TestCase):

  def test_zero(self):
    fact = s.factorial(0)
    self.assertEqual(fact, 1)
  
  def test_one(self):
    fact = s.factorial(1)
    self.assertEqual(fact, 1)
    
  def test_five(self):
    fact = s.factorial(5)
    self.assertEqual(fact, 120)
    
#  def test_float(self):
#    with self.assertRaises(TypeError):
#      s.factorial(3.4)
      
#  def test_negative(self):
#    with self.assertRaises(ValueError):
#      s.factorial(-4)
    
  
  
class TestIsFactor(TestCase):
  
#  def test_zero_factor(self):
#    with self.assertRaises(ValueError):
#    result = s.is_factor(10, 0)
    
  def test_proper_factor_1(self):
    result = s.is_factor(81, 3)
    self.assertTrue(result)
    
  def test_proper_factor_2(self):
    result = s.is_factor(100, 50)
    self.assertTrue(result)
    
  def test_same_value(self):
    result = s.is_factor(28, 28)
    self.assertTrue(result)
    
  def test_not_factor(self):
    result = s.is_factor(49, 3)
    self.assertFalse(result)
  


class TestIsPrime(TestCase):
  
  def test_prime(self):
    result = s.is_prime(7)
    self.assertTrue(result)
    
  def test_composite(self):
    result = s.is_prime(9)
    self.assertFalse(result)
    
#  def test_zero(self):
#    with self.assertRaises(ValueError):
#      s.is_prime(0)

#  def test_negative(self):
#    with self.assertRaises(ValueError):
#      s.is_prime(-5)
      
#  def test_float(self):
#    with self.assertRaises(TypeError):
#      s.is_prime(2.3)
  
  
  
class TestIsPerfect(TestCase):
  
  def test_perfect(self):
    result = s.is_perfect(6)
    self.assertTrue(result)
    
  def test_not_perfect(self):
    result = s.is_perfect(8)
    self.assertFalse(result)
    
#  def test_zero(self):
#    with self.assertRaises(ValueError):
#      s.is_perfect(0)
  
#  def test_negative(self):
#    with self.assertRaises(ValueError):
#      s.is_perfect(-5)
      
#  def test_float(self):
#    with self.assertRaises(TypeError):
#      s.is_perfect(2.3)
  

class TestDigitSumIsFactor(TestCase):

  def test_one_digit(self):
    result = s.digit_sum_is_factor(6)
    self.assertTrue(result)
    
  def test_factor(self):
    result = s.digit_sum_is_factor(12)
    self.assertTrue(result)
    
  def test_not_factor(self):
    result = s.digit_sum_is_factor(101)
    self.assertFalse(result)
    
#  def test_negative(self):
#    with self.assertRaises(ValueError):
#      result = s.digit_sum_is_factor(-3)
    
#  def test_float(self):
#    with self.assertRaises(TypeError):
#      s.digit_sum_is_factor(214.123)
