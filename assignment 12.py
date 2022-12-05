#Create a function that takes three arguments a, b, c and returns the sum of
#the numbers that are evenly divided by c from the range a, b inclusive.
#Examples
#evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
def num(x,y,z):
    for i in range(x, y+1):
        if i%z == 0:
            print(i, end = ",")

x = print(num(1, 10, 2))

#Create a function that returns True if a given inequality expression is correct and
#False otherwise.
#Examples
#correct_signs(3 < 7 < 11) ➞ True
#correct_signs(13 > 33 > 1) ➞ False

def check(s):
    regex = eval(s)
    if regex:
        return True
    else:
        return False
print(check("3 < 7 < 11"))
print(check("22>11>10"))

#Question3. Create a function that replaces all the vowels in a string
# with a specified character.
#Examples
#replace_vowels("the aardvark") ➞ th# ##rdv#rk
#replace_vowels(minnie mouse) ➞ m?nn?? m??s?

def replacewithvowels(test_str, k):
    vowels = 'aeiou'
    for ele in vowels:
        test_str = test_str.replace(ele, k)
    return test_str
k = '#'
print(replacewithvowels("the aardvark", k))

#Write a function that calculates the factorial of a number recursively.
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
result = fact(5)
print(result)



