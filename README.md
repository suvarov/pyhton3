# Python3
## Objects and Methods
### Objects
Objects whose values can be changed during the course of program execution are called **mutable**.
Objects whose value is unchangeable after they've been created are **immutable**.

Each object in Python has 3 characteristics:
* Type
* value
* identity

Most objects has either data or methods associated with them, they are called **attributes**.
*Instance* is one occurrence of an object.

### Modules
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

### Numbers and basic calculations
Three numerical types are available in Python - int, float, complex. `Int` have unlimited precision.

### Random choice
```Python
import random
random.choice(['aa','bb','cc'])
```

### Expressions and Booleans
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

## Sequence Objects
### Sequences
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
#### Lists
Lists are mutable Sequences.

#### Tuples
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

#### Ranges
Ranges are immutable Sequences often used in `for` loops.
```Python
range(5) # creates range(0,5)
list(range(5)) # returns a list [0, 1, 2, 3, 4]
list(range(1,6)) # returns a list [1, 2, 3, 4, 5]
list(range(1,13,2)) # returns a list [1, 3, 5, 7, 9, 11]
```
Using ranges saves a lot of memory.

#### Strings
```python
s = "abc"
3*s # creates s + s +s string --> "abcabcabc"
```
#### Sets
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

#### Dictionaries
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
