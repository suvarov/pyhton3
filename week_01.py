import math
from math import pi
math.sqrt(math.pi / 2)

import math
import numpy as np
math.sqrt(2)
np.sqrt([2,3,4])

name = "Amy"
type(name)
dir(name) # to get all available methods
dir(str) # can use a type
help(name.upper)

import random
random.choice(['aa','bb','cc'])

2 < 4 # True
2 <= 2 # True
2 == 2 # True
3 != 3 # False
[2,3] == [3,2] # False
[2,3] is [2,3] # False
[2,3] is not [2,3] # True
2.0 == 2 # True. 2nd operand will be converted to float => 2.0

s = (1,2,3,4,5,6,7,8)
s[0] # = 1
s[1] # = 2
s[-1] # = 8, very last objects

x = s[0:2] # x is (1,2)
y = s[:5] # y is (1,2,3,4,5)
z = s[5:] # z is (4,5,6,7,8)

x = 11.23
y = 12.31
coordinate = (x,y) # <-- this is called tuple packing
type(coordinate) # returns 'tuple'
(c1, c2) = coordinate # <-- and this is tuple unpacking
coordinates = [(0,0),(1,1),(2,4),(3,9),(4,16),(5,25),(6,36),(7,49),(8,64)]
for (x,y) in coordinates:
  print(x,y)

range(5) # creates range(0,5)
list(range(5)) # returns a list [0, 1, 2, 3, 4]
list(range(1,6)) # returns a list [1, 2, 3, 4, 5]
list(range(1,13,2)) # returns a list [1, 3, 5, 7, 9, 11]

s = "abc"
3*s # creates s + s +s string --> "abcabcabc"

ids = set(list(range(1,10)))
ids # prints {1, 2, 3, 4, 5, 6, 7, 8, 9}
ids.pop() # pops "1" from the set
ids.add(10) # adds "10" object to the set

males = set([1, 3, 4, 6])
females = ids = males
females # prints {2, 5, 7, 8, 9, 10}
everyone = males | females # "|" means UNION for Sets
everyone & set([-1, -2, 3, 5, 11]) # returns {3, 5}

word = "antidisestablcihmentarianism"
letters = set(word)
len(letters) # gives us a number of unique letters in a string

age = {} # empty Dictionary
age = dict() # same effect
age = {"Tim": 29, "Tom": 31, "Ally": 18}
age["Ally"] # prints 18
age["Tim"] += 1
names = age.keys
type(names) # returns "dict_keys"

x = 3
# 1) Python creates an object '3'
# 2) Variable named 'x' created
# 3) Reference from 'x' to '3' created

x = 3     # immutable object '3' created, 'x' created and linked to '3'
y = x     # 'y' created and linked to '3', as variable name cannot reference other name
y = y - 1 # '2' (as 3-1 = 2) created and 'y' is linked to '2'
print(x)  # '3' is printed
print(y)  # '2' is printed

L1    = [2, 3, 4]
L2    = L1
L1[0] = 24
print(L1)           # [24, 3, 4]
print(L2)           # [24, 3, 4]
L2 is L1            # True
