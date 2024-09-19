from abc import ABC, abstractmethod
from typing import List, Self
class Campare(ABC):
    def compare(self, item: Self)->bool:
        """Returns true if the item is bigger than self"""
        pass
class display(ABC):
    def print(self):
        """Print data"""
        pass

class Sortable(ABC):
    def __init__(self,data:List[Campare]):
        self.data = data
    @abstractmethod
    def get(self, index: int):
        """Get element according to index"""
        pass
    @abstractmethod
    def set(self, index: int, value):
        """Set element according to index"""
        pass
    @abstractmethod
    def length(self) -> int:
        """Get length of the sortable structure"""
        pass
    @abstractmethod
    def swap(self, index1: int, index2: int):
        """Switch localation of two emelents by using index"""
        pass
    @abstractmethod
    def print(self):
        """Print this data"""
        pass



class SortableData(Sortable,display):
    def __init__(self,data:List[Campare]):
        self.data = data
    def get(self, index: int):
        return self.data[index]
    def set(self, index: int, value):
        self.data[index] = value
    def length(self) -> int:
        return len(self.data)
    def swap(self, index1: int, index2: int):
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]
    def print(self):
        for item in self.data:
            item.print()
    

def bubble_sort(data: Sortable):
    n = data.length()
    for i in range(n):
        for j in range(0, n-i-1):
            if data.get(j).compare(data.get(j+1)):
                data.swap(j, j+1)
    return data

class Human(Campare,display):
    def __init__(self, age:int, height:float):
        self.age = age
        self.height = height
    def compare(self, item: Self) -> bool:
        return self.age> item.age
    def print(self):
        print("age:"+str(self.age)+",height:"+str(self.height))

bubble_sort(SortableData([Human(10,100),Human(20,180),Human(12, 200)])).print()