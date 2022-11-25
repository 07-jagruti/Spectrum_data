#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
import math
C = 50
H = 30
D = int(input("Enter a value of D: "))
Q = (2 * C * D)/H
math.sqrt(Q)

#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program: without,hello,bag,world
#the output should be: bag,hello,without,world
words = input("Enter a word: ")
words_list = words.split(",")
words_list.sort()
print((',').join(words_list))

#Write a program that accepts a sequence of whitespace separated words as input and
#prints the words after removing all duplicate words and sorting them alphanumerically.
#Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again
#Then, the output should be: again and hello makes perfect practice world
sentence = input("Write something: ")
s_list = sentence.split(" ")
a = []

for i in s_list:
  if i not in a:
    a.append(i)
  else:
    continue
a.sort()
print("the output is: ")
print((' ').join(a))

# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program: hello world! 123
# Then, the output should be: LETTERS 10 DIGITS 3
sentence = input("Write something: ")
l = d = 0
for char in sentence:
    if char.isdigit():
        d = d + 1
    elif char.isalpha():
        l = l + 1
    else:
        pass
print("LETTERS : ", l)
print("DIGITS: ", d)

#A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
#Following are the criteria for checking the password:
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#1. At least 1 letter between [A-Z]
#3. At least 1 character from [$#@]
#4. Minimum length of transaction password: 6
#5. Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
#Passwords that match the criteria are to be printed, each separated by a comma.
import re

password = input("Enter: ")
password = password.split()

accepted_password = []
for i in password:
  if len(i) < 6 or len(i) > 12:
    continue

  elif not re.search("[a-z]", i):
    continue

  elif not re.search("[0-9]", i):
    continue

  elif not re.search("[A-Z]", i):
    continue

  elif not re.search("[@#$]", i):
    continue

  else:
    accepted_password.append(i)

print(('').join(accepted_password))






