[# HarvardX PH526x: Using Python for Research](https://www.edx.org/course/using-python-for-research)
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
Scope Rules application acronym:
*L* ocal
*E* nclosing Function
*G* lobal
*B* uilt-in

```Python
def update():
  x.append(1)

x = [1, 1]
update()
x # [1, 1, 1]
```
This is so called **side effect**, generally you should avoid this style of programming.
It makes errors difficult to find.

```Python
def update(n, x):
  n = 2
  x.append(4)
  print('update: ', n, x)

def main():
  n = 1
  x = [0, 1, 2, 3]
  print('main: ', n, x)
  update(n, x)
  print('main: ', n, x)

main()
# main: 1, [1, 2, 3]
# update: 2, [1, 2, 3, 4]
# main: 1, [1, 2, 3, 4]
```

### 2.1.2: Classes and OOP
Inheritance
```Python
class MyList(list):
  def remove_min(self):
    self.remove(min(self))
    def remove_max(self):
      self.remove(max(self))

x = [10, 3, 5, 1, 2, 7, 6, 4, 8]
y = MyList(x)

y.remove_min() # y is [10, 3, 5, 2, 7, 6, 4, 8]
y.remove_max() # y is [3, 5, 2, 7, 6, 4, 8]
```

### 2.2.1: Introduction to NumPy Arrays
NumPy arrays used for representing vectors and matrices. In oppose to standard Python arrays they have size that is fixed on creation.
```Python
import numpy as np
zero_vector = np.zeros(5)
zero_matrix = np.zeros((5,3))

x = np.array([1, 2, 3])
y = np.array([2, 4, 6])
Z = np.array([[1, 3, 5], [5, 9, 4]])
Z.transpose()
```

### 2.2.2: Slicing NumPy Arrays
 ```Python
import numpy as np
x = np.array([1, 2, 3])
y = np.array([2, 4, 6])
X = np.array([[1, 2, 3], [4, 5, 6]])
X = np.array([[2, 4, 6], [8, 10, 12]])

x[0:2] # array([1, 2])
z = x + y # z is [3, 6, 9]
X[:, 1] # array([2, 5])
X[:, 1] + Y[:, 1] # array([6, 15])
X[1, :] # array([4, 5, 6])
X[1, :] + Y[1, :] # array([12, 15, 18])
X[1] # array([4, 5, 6])
 ```

### 2.2.3: Indexing NumPy Arrays
NumPy arrays can also be indexed with other arrays or other sequence-like objects.
```Python
import numpy as np
z1 = np.array([1, 3, 5, 7, 9])
z2 = z1 + 1 # array([2, 4, 6, 8, 10])
ind = [0, 2, 3]
z1[ind] # array([1, 5, 7])

ind = np.array([0, 2, 3])
z1[ind] # SAME RESULT: array([1, 5, 7])

# Boolean OR logical array can be used:
z1 > 6 # array([False, False, False, True, True], dtype = bool)
z1[z1 > 6] # array([7, 9])
z2[z1 > 6] # array([8, 10])
```
When you slice an array using the `colon` operator, you get a **view** of an object.
If you modify it the original array is also modified. This is in contrast with what happens when you **index** an array,
in which case what is returned to you is a copy of the original data.
```python
import numpy as np
z1 = np.array([1, 3, 5, 7, 9])
w = z1[0:3] # w is array([1, 3, 5])
w[0] = 3    # w is array([3, 3, 5])
z1          # array([3, 3, 5, 7, 9])

z1 = np.array([1, 3, 5, 7, 9])
ind = [0, 1, 2]
w = z1[ind] # array([1 , 3, 5])
w[0] = 3    # w is array([3, 3, 5])
z1          # array([1, 3, 5, 7, 9])
```

### 2.2.4: Building and Examining NumPy Arrays
```Python
import numpy as np
np.linspace(start = 0, stop = 100, num = 10) # array([0., 11,11111111, ..., 88,88888889, 100.])
np.logspace(start = 1, stop = 2, num = 10) # start = log(10) = 1, stop = log(100) = 2, array consisting of 10 elements where the first element is 10 and the last element is 100.

np.logspace(np.log10(250), np.log10(500), 10) # array([250., ..., 500.]) of 10 elements uniformly spaced in log10 space

X = np.array([[1, 2, 3], [4, 5, 6]])
X.shape # (2,3)
X.size # 6
# shape and size are DATA AATRIBUTES, not methods

x = np.random.random(10) # NumPy has it sown RANDOM Module
np.any(x > 0.9)   # True
np.all(x >= 0.1)  # True
```

### 2.3.1: Introduction to Matplotlib and Pyplot
