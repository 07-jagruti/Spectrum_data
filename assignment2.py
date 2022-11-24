#Write a python program to print multiplication table
num = int(input("Display multiplication table of"))
for i in range(1,11):
  print(num, 'x', i, '=', num*i)

#Write a Python Program to Print the Fibonacci sequence?
def fib(n):
  a = 0
  b = 1
  print(a)
  print(b)
  for i in range(2, n):
    c = a+b
    a = b
    b = c
    print(c)

fib(10)

#Write a Python Program to Find the Sum of Natural Numbers?
num = 10
if num < 0:
  print("Enter possitive number")
else:
  sum = 0
  while (num > 0):
    sum = sum + num
    num = num - 1
  print("the sum is : ", sum)

#Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
dec = int(input("Enter a number"))
print(bin(dec), "in binary")
print(oct(dec)), "in octal"
print(hex(dec)), "in hexadecimal"

