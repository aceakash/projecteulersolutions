# http://projecteuler.net/problem=5
# Problem 5
# Smallest multiple
# 2520 is the smallest number that can be divided by each of the 
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

import time

def isDivisible(number, factors):
	"""Checks if number is evenly divisible by each number in factors
	"""
	for x in set(factors):
		if number % x != 0:
			return False
	return True

def solve():
	min = 3*7*11*13*17*19 # prime numbers
	min = 20 * min # definitely needs to be a multiple of 20
	testThese = [12, 14, 15, 16, 18] # only have to test divisibility for these, as everything else is a factor of 20 
	done = False	
	i = 1
	answer = None
	while True:
		current = min * i
		if isDivisible(current, testThese):
			answer = current
			break
		i = i + 1
	return answer


if __name__ == '__main__':
	startTime = time.time()
	answer = solve()
	endTime = time.time()
	print '{0} (Computed in {1:.3} s)'.format(answer, (endTime - startTime))