# HarvardX PH526x: Using Python for Research[https://www.edx.org/course/using-python-for-research]
## Week 1: Basics of Python 3
### 1.1.3: Modules and Methods
#### Objects
Objects whose values can be changed during the course of program execution are called **mutable**.
Objects whose value is unchangeable after they've been created are **immutable**.

Each object in Python has 3 characteristics:
* Type
* value
* identity

Most objects has either data or methods associated with them, they are called **attributes**.
*Instance* is one occurrence of an object.

#### Modules
Sample module interaction:
```python
import math
from math import pi
math.sqrt(math.pi / 2)
```

#### What is a Namespace?
```python
import math
import numpy as np
math.sqrt(2)
np.sqrt([2,3,4])
```
**math** and **np** are different Namespaces.

```python
name = "Amy"
type(name)
dir(name) # to get all available methods
dir(str) # can use a type
help(name.upper)
```

### 1.1.4: Numbers and Basic Calculations
Three numerical types are available in Python - int, float, complex. `Int` have unlimited precision.

### 1.1.5: Random Choice
```Python
import random
random.choice(['aa','bb','cc'])
```

### 1.1.6: Expressions and Booleans
`OR`, `AND` and `NOT` are the only bool operatinos.
There are total of 8 comparison operations.
```Python
2 < 4 # True
2 <= 2 # True
2 == 2 # True
3 != 3 # False
[2,3] == [3,2] # False
[2,3] is [2,3] # False
[2,3] is not [2,3] # True
2.0 == 2 # True. 2nd operand will be converted to float => 2.0
```

## Part 2: Sequence Objects
### 1.2.1: Sequences
There are three basic Sequences: `list`, `tuple`, `range`.
```Python
s = (1,2,3,4,5,6,7,8)
s[0] # = 1
s[1] # = 2
s[-1] # = 8, very last objects
```
Sequence supports **slising**.
```Python
x = s[0:2] # x is (1,2)
y = s[:5] # y is (1,2,3,4,5)
z = s[5:] # z is (4,5,6,7,8)
```
### 1.2.2: Lists
Lists are mutable Sequences.

### 1.2.3: Tuples
Tuples are **immutable** Sequences.
```Python
x = 11.23
y = 12.31
coordinate = (x,y) # <-- this is called tuple packing
type(coordinate) # returns 'tuple'
(c1, c2) = coordinate # <-- and this is tuple unpacking
coordinates = [(0,0),(1,1),(2,4),(3,9),(4,16),(5,25),(6,36),(7,49),(8,64)]
for (x,y) in coordinates:
  print(x,y)
```

### 1.2.4: Ranges
Ranges are immutable Sequences often used in `for` loops.
```Python
range(5) # creates range(0,5)
list(range(5)) # returns a list [0, 1, 2, 3, 4]
list(range(1,6)) # returns a list [1, 2, 3, 4, 5]
list(range(1,13,2)) # returns a list [1, 3, 5, 7, 9, 11]
```
Using ranges saves a lot of memory.

### 1.2.5: Strings
```python
s = "abc"
3*s # creates s + s +s string --> "abcabcabc"
```
### 1.2.6: Sets
Sets are unordered collections of distinct hashable objects.
There is a `set`, and then there is a `frozen set` (yes, it is **immutable**).
Sets are especially useful for keeping track of distinct objects.
```Python
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
```

### 1.2.7: Dictionaries
Key - Value pairs, where `key` is **immutable**, and `value`  is anything.
Dictionaries can be used to perform very fast lookups on unordered data.
```Python
age = {} # empty Dictionary
age = dict() # same effect
age = {"Tim": 29, "Tom": 31, "Ally": 18}
age["Ally"] # prints 18
age["Tim"] += 1
names = age.keys
type(names) # returns "dict_keys"
```

## Part 3: Manipulating Objects
### 1.3.1: Dynamic Typing
Type checking is performed during runtime.
```Python
x = 3
# 1) Python creates an object '3'
# 2) Variable named 'x' created
# 3) Reference from 'x' to '3' created
```
How dynamic typing works with immutable objects:
```Python
x = 3     # immutable object '3' created, 'x' created and linked to '3'
y = x     # 'y' created and linked to '3', as variable name cannot reference other name  
y = y - 1 # '2' (as 3-1 = 2) created and 'y' is linked to '2'
print(x)  # '3' is printed
print(y)  # '2' is printed
```

How dynamic typing works with mutable objects:
```Python
L1    = [2, 3, 4]
L2    = L1
L1[0] = 24
print(L1)           # [24, 3, 4]
print(L2)           # [24, 3, 4]
L2 is L1            # True
```
### 1.3.2: Copies
### 1.3.3: Statements
### 1.3.4: For and While Loops
### 1.3.5: List Comprehensions
### 1.3.6: Reading and Writing Files
### 1.3.7: Introduction to Functions
### 1.3.8: Writing Simple Functions
### 1.3.9: Common Mistakes and Errors
## Homework \#1

# Week 2: Python Libraries and Concepts Used in Research
## Part 1: Scope Rules and Classes
### 2.1.1: Scope Rules
