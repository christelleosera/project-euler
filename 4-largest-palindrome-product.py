def is_palindrome(n):
	n = str(n)
	for i in range(len(n)/2):
		if n[i] != n[len(n)-i-1]:
			return False
	return True

def largest_palindrome_product():
	lrg_prod = 100001
	for i in range(999, 100, -1):
		if i*999 <= lrg_prod:
			break
		for j in range(999, i, -1):
			curr_prod = i*j
			if curr_prod > lrg_prod and is_palindrome(curr_prod):
				lrg_prod = curr_prod
	return lrg_prod

if __name__ == "__main__":
  print largest_palindrome_product()