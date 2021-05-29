import unittest 
import q1code 

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(q1code.fizzBuzz(), 'Hello World')

if __name__ == '__main__':
    unittest.main()