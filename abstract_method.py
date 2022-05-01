"""
https://docs.python.org/3.5/library/abc.html#abc.abstractmethod
Here I show how abstractmethod works
"""

from abc import ABC, abstractmethod


class AbstractClass(ABC):

    @abstractmethod
    def abstract_method(self):
        return


class ConcreteClass(AbstractClass):
    def __init__(self):
        self.me = "me"

    def abstract_method(self):
        print("ConcreteClass is overloading abstract method")


class AnotherConcreteClass(AbstractClass):
    def __init__(self):
        self.me = "me"


if __name__ == '__main__':
    # Here you can see that I can create object from ConcreteClass
    my_concrete_object = ConcreteClass()
    my_concrete_object.abstract_method()

    #Here you can see the errors, and also it will raise TypeError!
    #my_another_concrete_class = AnotherConcreteClass()
    #my_another_concrete_class.abstract_method()