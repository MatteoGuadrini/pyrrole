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

## Role method

By default, no method or attribute is inherited from a role class. 
If you want a method to be inherited, just enclose the method to inherit in a _role_method_ decorator.

```python
import pyrrole

class FallFromTree(metaclass=pyrrole.Role):
    
    @pyrrole.role_method
    def fall(self, tree='tree'):
        return f"Fall from {tree}"

class Fruit:
    pass

@FallFromTree
class Apple(Fruit):
    pass

apple = Apple()

print(apple.fall('apple tree'))
```