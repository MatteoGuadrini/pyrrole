# pyrrole

_pyrrole_ is a python library that allows the use of class as a role rather than having N mixin classes that exploit the magic of MRO.

## Simple role

Here is an example of how a role can be done:

```python
import pyrrole

class FallFromTree(metaclass=pyrrole.Role):
    pass

class Fruit:
    pass

@FallFromTree
class Apple(Fruit):
    pass

apple = Apple()

print(apple.__roles__)
```

In this example, the `Apple` class inherits from `Fruit` but not `FallFromTree`. 
`FallFromTree` is a role class that applies to classes so that they acquire the **__roles__** attribute.

