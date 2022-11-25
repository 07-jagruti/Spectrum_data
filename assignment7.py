#Write a Python program to Extract Unique values dictionary values?
test_dict = {'hello' : [1,2,3,4],
             'jagruti' : [5,4,11,8],
             'here' : [9,13,11,12]}
print("the original dictionary is : ", str(test_dict))

x = list(test_dict.values())
y = []
z = []
for i in x:
  y.extend(i)
for i in y:
  if i not in z:
    z.append(i)
z.sort()

print("the unique value list is: ", str(z))

#Write a Python program to find the sum of all items in a dictionary?
def test_dict(dict):
  return sum(dict.values())

dict = {'a' : 100, 'b' : 200, 'c' : 300}
print(test_dict(dict))


#Write a Python program to Merging two Dictionaries?
dict1 = {'a' : 10, 'b' : 20}
dict2 = {'c' : 30, 'd' : 40}
dict2.update(dict1)
print(dict2)

#Write a Python program to insertion at the beginning in OrderedDict?
from collections import OrderedDict
dic1 = {'a' : 10, 'b' : 20}
insert = {'c' : 30}

final = OrderedDict(list(insert.items()) + list(dic1.items()))
print("Resultant dictionary is: ")
print(final)

#Write a Python program to sort Python Dictionaries by Key or Value?
dic = {'a' : 40, 'b' : 20, 'c' : 30}

sorted(dic.values())



