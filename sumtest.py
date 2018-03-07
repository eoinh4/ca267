import unittest
from summ import summ
#"sum" is a built in function
class SummTestCase(unittest.TestCase):

    def test_5(self):
        self.assertEqual(summ(5),15)

    def test_10(self):
        self.assertEqual(summ(10),55)

    def test_20(self):
        self.assertEqual(summ(20),210)

    def test_1(self):
        self.assertNotEqual(summ(1),2)

#    def test_oops(self):
#        self.assertEqual(summ(1),0,"oops")
#^^this is the syntax to write error messages,
#uncomment it to see it fail and print "oops"

#run this with F5 key, while in the same directory assum.py

if __name__ == "__main__":
    unittest.main()
