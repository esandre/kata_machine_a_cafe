import unittest

from QuantiteCafe import QuantiteCafe
from ValueOutsideOfBoundsException import ValueOutsideOfBoundsException


class QuantiteCafeTest(unittest.TestCase):
    def test_quantite_non_negative(self):
        with self.assertRaises(ValueOutsideOfBoundsException):
            QuantiteCafe(-1)


if __name__ == '__main__':
    unittest.main()
