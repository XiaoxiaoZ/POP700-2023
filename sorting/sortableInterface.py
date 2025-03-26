from typing import List, TypeVar, Generic, Protocol, Self, runtime_checkable

# The requiaments of the data is that:
# 1. Data can be camparable and displayable
# 2. List of data has get, set, length, swap

class Comparable(Protocol):
    """Defines a protocol for objects that can be compared."""
    # Compare can be very creative, that is the key of how you can use your algorithm
    def compare(self, item: Self) -> bool:
        """Returns True if self is greater than item"""
        pass

class Displayable(Protocol):
    """Defines a protocol for objects that can be displayed."""
    def display(self):
        """Prints data"""
        pass

# Define ComparableDisplayable by combining Comparable and Displayable
@runtime_checkable
class ComparableDisplayable(Comparable, Displayable, Protocol):
    """Defines a protocol for objects that are both comparable and displayable."""
    pass

# Define a generic type variable for sortable elements
T = TypeVar('T', bound=ComparableDisplayable)

class Sortable(Generic[T]):
    """Generic sortable structure that works with any ComparableDisplayable object."""
    
    def __init__(self, data: List[T]):
        self.data = data

    def get(self, index: int) -> T:
        return self.data[index]

    def set(self, index: int, value: T):
        self.data[index] = value

    def length(self) -> int:
        return len(self.data)

    def swap(self, index1: int, index2: int):
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]

    def show(self):
        for item in self.data:
            item.display()

# Example class implementing Comparable and Displayable
class Item:
    def __init__(self, value: int):
        self.value = value

    def compare(self, item: Self) -> bool:
        return self.value > item.value

    def display(self):
        print(self.value)

# Example Usage
data = [Item(5), Item(2), Item(8)]
sortable_list = Sortable(data)

sortable_list.show()  # Output: 5, 2, 8
sortable_list.swap(0, 1)
sortable_list.show()  # Output: 2, 5, 8




