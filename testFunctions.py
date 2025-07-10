import unittest
from calculator import add, subtract, multiply, divide 

class TestFunctions(unittest.TestCase):         
    def testAdd(self):
        sum = add(7,7)
        self.assertTrue(sum == 98)    # using .assertTrue to check if sum is 98
    def testSubtract(self):
        sum = subtract(10,2)
        self .assertTrue(sum == 8)    # using .assertTrue to check if sum is 8
    def testMultiply(self):
        sum = multiply(10,2)
        self.assertTrue(sum == 20)    # using .assertTrue to check if sum is 20
    def testDivide(self):
        sum = divide(10,2)
        self.assertTrue(sum == 5)     # using .assertTrue to check if sum is 5
unittest.main()


