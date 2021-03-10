class Human:
    """ It is class.
    1) "Human" - it is a name of class.
    2) all objects in __init__ - fields (or condition).
       combination of it is unique for each object,
       but all object of the class get this fields.
    3) all objects with "def ..." at the beginning - methods (or behaviour). """
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def run(self, destination):
        pass

    def sleep(self, hours):
        pass

    def eat(self):
        pass

    def work(self):
        pass


class Animal:
    """
    It is a superclass (or parent class) for class Cat.
    Superclass have similar behaviour and condition that have all subclasses.
    Subclasses can redefine some behaviour and add some new behaviour/condition.
    """
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def run(self, destination):
        pass

    def sleep(self, hours):
        pass

    def eat(self):
        pass


class Cat(Animal):
    def __init__(self, name, gender, age, length_moustache):
        super().__init__(name, gender, age)  # For giving all fields from superclass.
        self.length_moustache = length_moustache  # New field for class Cat.

    def meow(self):
        """ It is a behaviour inherent only for cats. """
        pass

    def eat(self):
        """ It is a redefining a behaviour for cats. """
        # ask human for a food
        pass
