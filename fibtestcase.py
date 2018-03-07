import unittest
from fib import fib

class FibTestCase(unittest.TestCase):

    def test_5(self):
        self.assertEqual(fib(5),[1,2,3,5,8])

    def test_4(self):
        self.assertEqual(fib(4),[1,2,3,5])

    def test_10(self):
        self.assertEqual(fib(10),[1,2,3,5,8,13,21,34,55,89])

    def test_0(self):
        self.assertNotEqual(fib(1000),[])

#    def test_oops(self):
#        self.assertEqual(fib(1)[0], "oops")
# ^this is used to print an error message when a test case fails^

if __name__ == "__main__":
    unittest.main()
#run this in the same folder as fib
