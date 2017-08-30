def sum_square_difference(n):
	sum_of_squares = 1
	for i in range(2, n+1):
		sum_of_squares += i*i

	square_of_sum = sum(list(range(1, n+1)))
	square_of_sum *= square_of_sum

	return square_of_sum - sum_of_squares

if __name__ == "__main__":
  print sum_square_difference(100)