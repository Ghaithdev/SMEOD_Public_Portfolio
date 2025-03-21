import unittest

def run(n):
		#
		# Write your code below; return type and arguments should be according to the problem\'s requirements
		x=n
		thousands=0
		while x>=1000:
			x-=1000
			thousands+=1
		thousands_out=thousands*"M"
		five_hundreds=0
		if x>=500:
			x-=500
			five_hundreds+=1
		hundreds=0
		while x>=100:
			x-=100
			hundreds+=1
		if five_hundreds+hundreds==5:
			hundreds_out="CM"
		elif hundreds==4:
			hundreds_out="CD"
		else:
			hundreds_out=f"{five_hundreds*'D'+ hundreds*'C'}"
		fifties=0
		if x>=50:
			x-=50
			fifties+=1
		tens=0
		while x>=10:
			x-=10
			tens+=1
		if fifties+tens==5:
			tens_out="XC"
		elif tens==4:
			tens_out="XL"
		else:
			tens_out=f"{fifties*'L'+tens*'X'}"
		fives=0
		if x>=5:
			fives+=1
			x-=5
		units=0
		while x>=1:
			x-=1
			units+=1
		if fives+units==5:
			units_out="IX"
		elif units==4:
			units_out="IV"
		else:
			units_out=f"{fives*'V'+units*'I'}"
		n_in_roman_alphabet = f"{thousands_out}{hundreds_out}{tens_out}{units_out}"
		return n_in_roman_alphabet


class SolutionMethods(unittest.TestCase):
	##
	# First Example
	
	def test_1954(self):
		#Arrange
		n=1954
		
		#Act
		result=run(n)

		#Assert
		self.assertEqual(result, "MCMLIV")

	def test_1990(self):
		#Arrange
		n=1990
		
		#Act
		result=run(n)

		#Assert
		self.assertEqual(result, "MCMXC")

	def test_2014(self):
		#Arrange
		n=2014
		
		#Act
		result=run(n)

		#Assert
		self.assertEqual(result, "MMXIV")
	
	

if __name__ == "__main__":
	unittest.main()
