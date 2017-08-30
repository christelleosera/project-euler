def lcm(a, b):
	greater = max(a,b)
	while True:
		if greater%a == 0 and greater%b == 0:
			lcm = greater
			break
		greater += max(a,b)
	return lcm

def smallest_multiple(n):
	res_lcm = n
	for i in range (n-1, 1, -1):
		curr_lcm = lcm(res_lcm, i)
		if res_lcm != curr_lcm:
			res_lcm = curr_lcm
	return res_lcm

if __name__ == "__main__":
  print smallest_multiple(20)