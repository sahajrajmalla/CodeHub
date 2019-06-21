from propertyFolder import property

from abc import ABC, abstractmethod


class parent(ABC):
    @abstractmethod
    def child(this):
        pass


class child1(parent):
    def child(this):
        return "i am from child1"


class child2(parent):
    def child(this):
        return "i am from child2"


def iterate(childs):
    for n in childs:
        print(n.child())


mychild1_object = child1()
mychild2_object = child2()

iterate([mychild1_object, mychild2_object])
