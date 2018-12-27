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
`import math`
`from math import pi`
`math.sqrt(math.pi / 2)`

#### What is a Namespace?
`import math`
`import numpy as np`
`math.sqrt(2)`
`np.sqrt([2,3,4])`
**math** and **np** are different Namespaces.

`name = "Amy"
type(name)
dir(name) // to get all available methods`
