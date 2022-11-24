#Write a Python program to find sum of elements in list?
num = [4,5,6,7,8]
sum(num)

#Write a Python program to Multiply all numbers in the list?
import numpy
num = [4,5,6,7,8]
result = numpy.prod(num)
print(result)

#OR
list = [4,5,6,7,8]
result = 1
for i in list:
  result = result * i
print(result)

#Write a Python program to find smallest number in a list?
list = [4,5,6,7,8]
min(list)

#Write a Python program to find largest number in a list?
list = [4,5,6,7,8]
max(list)

#Write a Python program to find second largest number in a list?
list = [4,5,66,7,8,56,87,33,10]
list.sort()
list[-2]

#Write a Python program to find N largest elements from a list?
list = [4,5,66,7,8,56,87,33,10]
n = 3
list.sort()
print(list[-n:])

#Write a Python program to print even numbers in a list?
list = [4,5,66,7,8,56,87,33,10]
for i in list:
  if i%2 == 0:
    print(i)

#Write a Python program to print odd numbers in a List?
list = [4,5,66,7,8,56,87,33,10]
for i in list:
  if i%2 != 0:
    print(i)

#Write a Python program to Remove empty List from List?
list = [[2,3,4], [], [33,65,44], [6,5,4]]
list.remove([])
list

#Write a Python program to Cloning or Copying a list?
list = [4,5,66,7,8,56,87,33,10]
list.copy()

#Write a Python program to Count occurrences of an element in a list?
list = [4,5,66,7,8,56,87,33,10,5,44,33,5]
n = 5
list.count(n)

