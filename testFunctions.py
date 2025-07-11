import unittest
from calculator import add, subtract, multiply, divide 

class TestFunctions(unittest.TestCase):         
    def testAdd(self):
        self.assertEqual(add(7,7)== 98)    # using .assertTrue to check if sum is 98
    def testSubtract(self):
        self.assertEqual(subtract(10,2) == 8)    # using .assertTrue to check if sum is 8
    def testMultiply(self):
        self.assertEqual(multiply(10,2) == 20)    # using .assertTrue to check if sum is 20
    def testDivide(self):
        self.assertEqual(divide(10,2) == 5)     # using .assertTrue to check if sum is 5
# unittest.main()

if __name__ == "__main__":
    unittest.main()

