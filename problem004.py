# http://projecteuler.net/problem=4
# Problem 4
# Largest palindrome product
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import time

def isPalindromicNumber(number):
	return str(number) == str(number)[::-1]

def solve():
	palindromes = [];
	for x in range(999, 100, -1):
		for y in range(999, 100, -1):
			product = x*y
			#print '{0} * {1} = {2}'.format(x, y, product)
			if isPalindromicNumber(product):				
				palindromes.append(product)
				#print '{0} * {1} = {2}'.format(x, y, product)
	
	largest = palindromes[0]
	for n in palindromes:
		if n > largest:
			largest = n		
	
	return largest

if __name__ == '__main__':
	startTime = time.time()
	answer = solve()
	endTime = time.time()
	print '{0} (Computed in {1:.3} s)'.format(answer, (endTime - startTime))