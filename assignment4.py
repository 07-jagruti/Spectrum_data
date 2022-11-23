#Write a Python Program to add Two Matrices?
m1 = matrix('1,2,3 ; 4,5,6 ; 7,8,9')
m2 = matrix('4,5,6 ; 8,9,7 ; 3,6,9')
m3 = m1+m2
print(m3)

#Write a Python Program to Multiply Two Matrices?
m1 = matrix('1,2,3 ; 4,5,6 ; 7,8,9')
m2 = matrix('4,5,6 ; 8,9,7 ; 3,6,9')
m3 = m1*m2
print(m3)

#Write a Python Program to Transpose a Matrix?
X = [[11,22,33],
     [44,55,66],
     [77,88,99]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(X)):
  for j in range(len(X)):
    result[j][i] = X[i][j]


for r in result:
  print(r)

#Write a Python Program to Sort Words in Alphabetic Order?
my_str = "Hello, this is jagruti girase"
words = [word.lower() for word in my_str.split()]
words.sort()
print("the sorted words are: ")
for word in words:
  print(word)

#Write a Python Program to Remove Punctuation From a String?
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = " Hello, Ramove punctuations! and write code@."
for word in (my_str):
  if word in punctuations:
    continue
  print(word, end = "")

