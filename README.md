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
