# Custom math functions

def isPrime(number):
	"""Check if the given number is prime. 
	   A prime number is one that is divisible only by itself and 1.
	   1 itself is not considered a prime.

	   Returns (bool, factor) where the first value is whether number is a prime,
	   and second value is the smallest prime factor of number if it's not prime,
	   or None is it is prime.  			
	"""
	if number == 1:
		return (False, 1)

	if number == 2:
		return (True, 2)

	if number % 2 == 0:
		return (False, number/2)

	# only need to go upto square root of number, while skipping even numbers
	for x in range(3, int(number**0.5 + 1), 2):
		if number % x == 0:
			return (False, x)

	return (True, None)


def primeFactorsOf(number):
	"""Returns a list with all the prime factors of number.
	"""
	if isPrime(number)[0]:		
		#print 'Prime!'
		return [number]

	primeFactors = []
	factor = 2
	current = number
	while factor <= current:
		#print 'current: {0}, factor: {1}'.format(current, factor)
		if current % factor == 0:
			primeFactors.append(factor)
			current = current / factor
		elif isPrime(current)[0]:
			primeFactors.append(current)
			break	
		else:	
			factor = factor + 1
	return primeFactors


if __name__ == '__main__':
	def check(number):
		(prime, factor) = isPrime(number)
		if prime:
			print '%d is prime' % number
		else:
			print "%d is not prime, it's divisible by %d" % (number, factor)
	# check(3)
	# check(7)
	# check(9)
	# check(2)
	# check(49)
		
	
	print '{0}: {1}'.format(2, primeFactorsOf(2))
	print '{0}: {1}'.format(3, primeFactorsOf(3))
	print '{0}: {1}'.format(4, primeFactorsOf(4))
	print '{0}: {1}'.format(7, primeFactorsOf(7))
	print '{0}: {1}'.format(8, primeFactorsOf(8))
	print '{0}: {1}'.format(35, primeFactorsOf(35))
	print '{0}: {1}'.format(49, primeFactorsOf(49))
	print '{0}: {1}'.format(64, primeFactorsOf(64))
	print '{0}: {1}'.format(600851475143L, primeFactorsOf(600851475143L))
	



