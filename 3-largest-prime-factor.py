def is_prime(x):
	if x <= 3:
		return True
	else:
		if x%2 == 0 or x%3 == 0:
			return False	
		i = 5
		w = 2
		while i*i <= x:
			if x%i == 0:
				return False
			i += w
			w = 6 - w
		return True


def largest_prime_factor(n):
	if is_prime(n):
		return n
	else:
		lrg_prime = 1
		i = 1
		while i <= n:
			if n%i == 0 and is_prime(i) and i > lrg_prime:
				lrg_prime = i
				n = n/i
			i += 1
		return lrg_prime

if __name__ == "__main__":
  print largest_prime_factor(600851475143)