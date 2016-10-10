def fib(n):
  if n == 0 or n == 1:
    return n
  return fib(n-2) + fib(n-1)
n = 10
for i in range(n):
  	print (fib(i)) #prints out fibonacci sequence
