#Write a Python Program to Find Factorial of Number Using Recursion?
def fact(n):
  if n == 0:
    return 1
  return n * fact(n-1)
result = fact(5)
print(result)

#Write a Python Program to calculate your Body Mass Index?
mass = int(input("enter a mass of the body in kg"))
height = int(input("enter a height of the body in feet"))
print("body mass index is: ", round(mass/(height*height), 2))

#Write a Python Program to calculate the natural logarithm of any number?
import math
print(math.log(2))

#Write a Python Program for cube sum of first n natural numbers?
n = 5
sum = 0
for i in range(n+1):
  sum = sum + i*i*i
print(sum)

#Write a Python Program to find sum of array?

arr = [1,2,13,4,5,6]
sum = 0
for i in range(0, len(arr)):
  sum = sum + arr[i]
print(sum)


#Write a Python Program to find largest element in an array?
arr = [1,2,13,4,5,6]
max(arr)

