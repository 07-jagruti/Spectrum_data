#Write a function that stutters a word as if someone is struggling to read it.
# The first two letters are repeated twice with an ellipsis ...
# and space after each, and then the word is pronounced with a question mark ?.
#Examples
#stutter(incredible) ➞ in... in... incredible?
#stutter(enthusiastic) ➞ en... en... enthusiastic?
#stutter(outstanding) ➞ ou... ou... outstanding?

def slutter(word):
    s = word[:2]
    return(2 * (s + '...')) + word + '?'

print(slutter("incredible"))


#Create a function that takes an angle in radians and returns the corresponding
##angle in degrees rounded to one decimal place.
#Examples
#radians_to_degrees(1) ➞ 57.3
#radians_to_degrees(20) ➞ 1145.9

def converter(radian):
    pi = 3.14
    degree = radian * (180 / pi)

    return degree
print(round(converter(20),1))

#In this challenge, establish if a given integer num is a Curzon number.
#If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num,
# then num is a Curzon number. Given a non-negative integer num, implement a function
# that returns True if num is a Curzon number, or False otherwise.
#Examples
#is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11
#is_curzon(10) ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21
#is_curzon(14) ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29

def curzon(num):
    result = 2 ** num + 1
    result1 = 2 * num + 1
    if result % result1 == 0:
        print(True)
    else:
        print(False)
x = curzon(14)
print(x)

#Given the side length x find the area of a hexagon.
#Examples
#area_of_hexagon(1) ➞ 2.6
#area_of_hexagon(2) ➞ 10.4
#area_of_hexagon(3) ➞ 23.4

import math
def num(x):
    Area = (3 * math.sqrt(3) * x * x)/2
    return Area
print("Area of hexagaon is: ")
print(round(num(3), 1))










