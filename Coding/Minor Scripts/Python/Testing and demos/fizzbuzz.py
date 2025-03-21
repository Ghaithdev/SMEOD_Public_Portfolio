class Solution:

	def run(self, N, M):
		#
		# Write your code below; return type and arguments should be according to the problem\'s requirements
		#
		sequence=""
		try:
			int(N)
			int(M)
		except(ValueError):
			print("invalid starting parameters")
			return
		if N<M:
			start=N
			finish=M
		elif N>M:
			start=M
			finish=N
		else:
			start=N
			finish=M

		while start<finish+1:
			if start%15==0:
				sequence+="FizzBuzz,"
			elif start%5==0:
				sequence+="Buzz,"
			elif start%3==0:
				sequence+="Fizz,"
			else:
				sequence+=f"{start},"
			start+=1
		sequence=sequence
		return sequence
		
import unittest
from fizzbuzz import Solution

class TestSolution(unittest.TestCase):
	
	def test_example(self):
		assert Solution.run(1,5)=="1,2,Fizz,4,Buzz" 
		assert Solution.run(1,10)=="1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz" 
		assert Solution.run(1,1)=="1" 

	def test_error(self):
		self.assertRaises(ValueError, self.run, "string", 1)
		self.assertRaises(ValueError, self.run, 3.5, 1)



if __name__ == '__main__':
    unittest.main()