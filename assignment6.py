#Write a Python program to find words which are greater than given length k?
s = "Write a Python program to find words which are greater than given length"
k = 5
word = s.split(" ")

for x in word:
  if len(x) > k:
    print(x)

#Write a Python program to split and join a string?
string = "Hello Jagruti here"
split_string = string.split()
join_string = '-'.join(split_string )
print(join_string)

#Write a Python to check if a given string is binary string or not?
stringA = '0110101010111'
b = {'1', '0'}
t = set(stringA)

if b == t:
  print("StringA is a binary string.")
else:
  print("StringA is not a binary string.")


stringB = '1101100012002'
u = set(stringB)
if b == u:
  print("StringB is a binary string.")
else:
  print("StringB is not a binary string.")


#Write a Python program to find uncommon words from two Strings?
def uncommon(A, B):
      x = A.split()
      y = B.split()

      for i in x:
          if i not in y:
              uc_words = i

      for j in y:
          if j not in x:
              uc_words1 = j
      return uc_words, uc_words1


A = "Jagruti Gajendrasing Girase"
B = "Juhi Gajendrasing Girase"
print(uncommon(A, B))


#Write a Python Program to check if a string contains any special character?
special_char = '''!@#$%^&*()_+='"?/><,:;'''
string = "j@grut!_girase*"

for i in string:
  if i in special_char:
    print(i)
