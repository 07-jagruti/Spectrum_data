#Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
def div(n):
  for i in range(n):
    if i % 7 == 0:
      value = True
    else:
      value = False

    print(i, value)

n = 20
print(div(n))

#Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
#Suppose the following input is supplied to the program:
#New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
#Then, the output should be:
#2:2
#3.:1
#3?:1
#New:1
#Python:5
#Read:1
#and:1
#between:1
#choosing:1
#or:2
#to:1

import operator
text_line = input("Write something: ")
frequency = {}
for i in text_line.split(' '):
  if i.isalpha():
    if i not in frequency:
      frequency[i] = 1
    else:
      frequency[i] = frequency[i] + 1

  if i.isdigit():
    if i not in frequency:
      frequency[i] = 1
    else:
      frequency[i] = frequency[i] + 1

print(frequency)


#Please write a program to generate all sentences where subject is in ["I", "You"] and
#verb is in ["Play", "Love"] and the object is in ["Hockey", "Football"].
def generate_sentence(subjects, verbs, objects):
  list = []
  for i in subjects:
    for j in verbs:
      for k in objects:
        list.append(i+ " "+j+ " "+k)
  return list

subject = ["I", "You"]
verb = ["Play", "Love"]
object = ["Hockey", "Football"]

print(generate_sentence(subjects, verbs, objects))






