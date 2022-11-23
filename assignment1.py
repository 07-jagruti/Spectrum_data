#Write a Python Program to Check if a Number is Positive, Negative or Zero?
x = [1,2,3,-5,0,-55,89,-65]
for i in x:
    if i > 0:
        print("possitive: ", i)
    elif (i < 0):
        print("negative:", i)
    else:
        print("zero:", i)

#Write a Python Program to Check if a Number is Odd or Even?
x = int(input("Enter a number"))
r = x%2
if r == 0:
    print("Even")
if r == 1:
    print("odd")

#Write a Python Program to Check Leap Year?
x = int(input("Enter a year"))
r = x%4
if r == 0:
    print("leap year")
else:
    print("this is not a leap year")

#Write a Python Program to Check Prime Number?
x = int(input("Enter a number"))
for i in range(2,x):
    if x % i == 0:
        print("not prime")
        break
else:
    print("prime")

#Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
lower_value = int(input("Enter the Lowest Range Value: "))
upper_value = int(input("Enter the Upper Range Value: "))

for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)


