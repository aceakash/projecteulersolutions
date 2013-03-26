# http://projecteuler.net/problem=3
# Problem 3
# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from libMath import primeFactorsOf
import time

def largestPrimeFactorOf(number):
	return primeFactorsOf(number)[-1]


if __name__ == '__main__':
	startTime = time.time()
	answer = largestPrimeFactorOf(600851475143)
	endTime = time.time()
	print '{0} (Computed in {1:.3} s)'.format(answer, (endTime - startTime))