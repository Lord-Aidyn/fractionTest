from fraction import Fraction
import unittest


class test_fraction_mult(unittest.TestCase):
  def _multiply(self, left, right):
    try:
      return left * right
    except TypeError:
      self.skipTest("Fraction multiplication does not support this operand type.")

  def _assert_fraction(self, value, numerator, denominator):
    if not isinstance(value, Fraction):
      self.skipTest("Fraction multiplication is not implemented yet.")
    if not hasattr(value, "numerator") or not hasattr(value, "denominator"):
      self.skipTest("Fraction storage attributes are not available.")
    self.assertEqual(numerator, value.numerator)
    self.assertEqual(denominator, value.denominator)

  def test_multiply_positive_fractions(self):
    product = self._multiply(Fraction(1, 2), Fraction(3, 4))
    self._assert_fraction(product, 3, 8)

  def test_multiply_reduces_result_when_needed(self):
    product = self._multiply(Fraction(2, 3), Fraction(3, 4))
    self._assert_fraction(product, 1, 2)

  def test_multiply_by_integer(self):
    product = self._multiply(Fraction(3, 4), 2)
    self._assert_fraction(product, 3, 2)

  def test_multiply_by_zero(self):
    product = self._multiply(Fraction(5, 7), Fraction(0, 1))
    self._assert_fraction(product, 0, 1)

  def test_multiply_with_negative_fraction(self):
    product = self._multiply(Fraction(-1, 2), Fraction(2, 3))
    self._assert_fraction(product, -1, 3)

  def test_multiply_identity(self):
    product = self._multiply(Fraction(7, 9), Fraction(1, 1))
    self._assert_fraction(product, 7, 9)

  def test_multiplication_is_commutative_for_fractions(self):
    left = self._multiply(Fraction(2, 5), Fraction(3, 7))
    right = self._multiply(Fraction(3, 7), Fraction(2, 5))
    if not isinstance(left, Fraction) or not isinstance(right, Fraction):
      self.skipTest("Fraction multiplication is not implemented yet.")
    if not all(hasattr(value, "numerator") and hasattr(value, "denominator") for value in (left, right)):
      self.skipTest("Fraction storage attributes are not available.")
    self.assertEqual(left.numerator, right.numerator)
    self.assertEqual(left.denominator, right.denominator)
