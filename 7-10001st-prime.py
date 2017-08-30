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

def nth_prime(n):
	prime_cnt = 2
	i = 5

	if n == 1:
		return 2
	if n == 2:
		return 3

	while prime_cnt < n:
		if is_prime(i):
			prime_cnt += 1
		i += 2
	return i-2

if __name__ == "__main__":
  print nth_prime(10001)