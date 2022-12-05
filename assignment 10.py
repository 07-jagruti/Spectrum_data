#Please write a program using generator to print the numbers which can be divisible by 5 and
#7 between 0 and n in comma separated form while n is input by console.
def NumGenerator(n):
  for i in range(n+1):
    if i%5 == 0 and i%7 == 0:
      yield i

n = int(input("Enter value"))
values = []
for i in NumGenerator(n):
  values.append(str(i))
print((",").join(values))

#Please write a program using generator to print the even numbers between 0 and n in comma
#separated form while n is input by console.
def NumGenerator(n):
  for i in range(n+1):
    if i%2 == 0:
      yield i

n = int(input())
values = []
for i in NumGenerator(n):
  values.append(str(i))
print((',').join(values))


# Please write a program using list comprehension to print the Fibonacci Sequence in comma
# separated form with a given n input by console.
def fib(n):
    a = 0
    b = 1
    print(a, end=",")
    print(b, end=",")

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c, end=",")
fib(7)

#Assuming that we have some email addresses in the "username@companyname.com" format,
#please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
email = "jagruti@google.com"
for i in email:
  if i == '@':
    break
  print(i, end = "")


# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape:
    pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        a = (self.length * self.length)
        print("the arear of square is : ", a)

length = int(input("Enter length of square: "))
x = Square(length)
x.area()








