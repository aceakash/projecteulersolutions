# http://projecteuler.net/problem=1
# Problem 1
# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def GetSumOfAllMultiples(a, b, limit):
	sum = 0
	for i in range(limit):
		if i % a == 0 or i % b == 0:
			sum += i
	return sum

if __name__ == '__main__':
	print GetSumOfAllMultiples(3, 5, 1000)
