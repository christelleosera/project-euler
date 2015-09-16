# Project Euler Problem 2 Solution

def even_fibonacci():
  a = 1
  b = 2
  sum = 0
  while(b < 4000000):
    a,b = b, a+b
    if a % 2 == 0:
      sum += a
  return sum
  
if __name__ == "__main__":
  print even_fibonacci()