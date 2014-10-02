# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
print(  a, end  = '.')

while b < 10:
  print(b)
  a, b = b, a+b
