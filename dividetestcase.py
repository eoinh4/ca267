import unittest
from divide import divide

class MultiplyTestCase(unittest.TestCase):

    def test_6_by_3(self):
        self.assertEqual(divide(6,3),2)

    def test_100_by_2(self):
        self.assertEqual(divide(100,2),50)

    def test_1000_by_1(self):
        self.assertNotEqual(divide(1000,1),2)
#run this in the same folder asdivide.py

if __name__ == "__main__":
    unittest.main()
    
