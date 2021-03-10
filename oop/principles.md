There are 4 cornerstones of object oriented programming:
--------
1. Abstraction
2. Encapsulation
3. Inheritance
4. Polymorphism
--------

## 1. Abstraction
This principle said that we can't and we don't need to transfer
things from real life into a code completely. 

We have to create a model for this things that give such 
a behaviour and condition that we need to solve problem
or deal with our tasks.

For example: we have a plane, but in different projects
this things from real life get a different model. 

If we are department of company which sells a tickets on plane,
our model in code looks like:

```python
class Plane:
    def __init__(self, number_of_places):
        self.number_of_places = number_of_places
        self.sold_tickets = 0    

    def sell(self):
        if self.sold_tickets < self.number_of_places:
            self.sold_tickets += 1
            return True
        return False
```

If we are company developed a simulator for pilots, we have to
take into account all details that affect to flight. Our model
in code looks like:

```python
class Plane:
    def __init__(self, speed, altitude, fuel):
        self.speed = speed 
        self.altitude = altitude
        self.fuel = fuel
    
    def fly(self, weather_cond):
        pass
```
_________________

## 2. Encapsulation
This principle declare that class can have some fields and 
methods which is not available for users. And devs should
think about it while coding some class: does this method
really useful for end-users? Devs should follow some 
**interface** which have a description of functionality but
not realization.

Class can have a private (nothing give an access) or
protected (only subclasses can use it) fields/methods.

Interfaces and abstract classes and methods based on 
encapsulation and abstraction principles.

For example:

```python
from abc import abstractmethod

class FlyingTransport:
    """ Class interface """

    @abstractmethod
    def landing(self):
        raise NotImplementedError

class Helicopter(FlyingTransport):
    """ Class which uses interface FlyingTransport and have to
        implement method landing """
    def landing(self):
        pass

class Plane(FlyingTransport):
    """ Class which uses interface FlyingTransport and have to
        implement method landing """
    def landing(self):
        pass


class Airport:
    IS_ACCEPT = True
    def accept(self, flying_object: FlyingTransport):
        if self.IS_ACCEPT:
            self.IS_ACCEPT = False
            flying_object.landing()
            self.IS_ACCEPT = True
        pass
```

As you can see class Airport doesn't have switches like

if isinstance(flying_object, Helicopter): ...
elif isinstance(flying_object, Plane): ...

Airport knows that all this classes have method landing
because this classes are from interface FlyingTransport.

-------------------------

## 3. Inheritance

This principle allow to create classes based on existing ones. 
Subclasses get fields and methods from parent class. Subclass
cannot exclude some thing from parent but can redefine it.
In some programming languages we can declare only parent or
several parents according to language realization.

---------------------------

## 4. Polymorphism

If some function parameter is mapped to only one type of data,
then this function is called monomorphic. So if some parameter
can be different types this function is called polymorphic.

This principle states that when we use one function for processing
another types of object which classes are subclasses of one parent
class and this function uses interface methods from parent class - it is ok.