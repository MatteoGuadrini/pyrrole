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

## Open source
_pyrrole_ is an open source project. Any contribute, It's welcome.

**A great thanks**.

For donations, press this

For me

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/guos)

For [Telethon](http://www.telethon.it/)

The Telethon Foundation is a non-profit organization recognized by the Ministry of University and Scientific and Technological Research.
They were born in 1990 to respond to the appeal of patients suffering from rare diseases.
Come today, we are organized to dare to listen to them and answers, every day of the year.

<a href="https://www.telethon.it/sostienici/dona-ora"> <img src="https://www.telethon.it/dev/_nuxt/img/c6d474e.svg" alt="Telethon" title="Telethon" width="200" height="104" /> </a>

[Adopt the future](https://www.ioadottoilfuturo.it/)


## Acknowledgments

Thanks to [Giacomo Montagner](https://github.com/kromg) for having the idea. Besides, being a contributor he is a great friend!

Thanks to Mark Lutz for writing the _Learning Python_ and _Programming Python_ books that make up my python foundation.

Thanks to Kenneth Reitz and Tanya Schlusser for writing the _The Hitchhiker’s Guide to Python_ books.

Thanks to Dane Hillard for writing the _Practices of the Python Pro_ books.

Special thanks go to my wife, who understood the hours of absence for this development. 
Thanks to my children, for the daily inspiration they give me and to make me realize, that life must be simple.

Thanks Python!