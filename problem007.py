# http://projecteuler.net/problem=7
# Problem 7
# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?
import time



def find_next_prime(primes, last):	
	found = False
	while not found:
		next = last + 2		
		found = is_prime(next, primes)
		last = next
	primes.append(next)
	return primes, next

	
def is_prime(number, primes):	
	start = primes[-1] + 2
	end = int(number ** 0.5) + 1
	if end % 2 == 0:
		end = end + 1
	prime = True
	for x in [i for i in primes if i <= end]:
		if number % x == 0:
			prime = False
			break
	return prime

def solve():
	primes = [2, 3]	
	last = 3
	required_number_of_primes = 10001
	while len(primes) < required_number_of_primes:		
		primes, last = find_next_prime(primes, last)
	return primes

if __name__ == '__main__':
	start = time.time()	
	answer = solve()[-1]
	end = time.time()

	print '{0} (computed in {1:.3} seconds)'.format(answer, end-start)



