# http://projecteuler.net/problem=2
# Problem 2
# Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

def GetFibonacciSequence(upperLimit):
	"""Get a list containing the Fibonacci sequence upto (and including) upperLimit
	"""
	a, b = (1, 2)	
	sequence = [a, b]
	c = a + b
	while c <= upperLimit:
		sequence.append(c)
		a, b = b, c
		c = a + b
	return sequence

if __name__ == '__main__':
	sequence = GetFibonacciSequence(4 * 1000 * 1000)
	sum = 0
	for x in sequence:
		if x % 2 == 0:
			sum += x
	print sum
		
			