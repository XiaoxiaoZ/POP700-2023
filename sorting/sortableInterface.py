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





