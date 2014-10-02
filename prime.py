
for n in range(2, 10):
   #  for x in range(2, n):
	 if n % 2 == 0:
             print(n, 'equals', 2, '*', n//2)
             break
	 else:
	# loop fell through without finding a factor
			print(n, 'is a prime number')