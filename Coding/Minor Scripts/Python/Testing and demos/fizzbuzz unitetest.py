import unittest
from fizzbuzz import Solution

class TestSolution(unittest.TestCase):
    def test_example(self):
        solution=Solution()
        assert solution.run(1,5)=="1,2,Fizz,4,Buzz" 
        assert solution.run(1,10)=="1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz" 
        assert solution.run(1,1)=="1" 

    def test_error(self):
        solution=Solution()
        self.assertRaises(ValueError, solution.run, "string", 1)
        self.assertRaises(ValueError, solution.run, 3.5, 1)



if __name__ == '__main__':
    unittest.main()