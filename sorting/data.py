import math
import requests
from typing import List, TypeVar, Generic, Protocol, Self
from algorithms import bubble_sort, heap_sort, insertion_sort, quick_sort, selection_sort
from sortableInterface import ComparableDisplayable, Sortable


# Implementing Different ComparableDisplayable Classes
class Human(ComparableDisplayable):
    def __init__(self, age: int, height: float):
        self.age = age
        self.height = height

    def compare(self, item: Self) -> bool:
        return self.age > item.age

    def display(self):
        print(f"Age: {self.age}, Height: {self.height}")

class StringData(ComparableDisplayable):
    def __init__(self, data: str):
        self.data = data

    def compare(self, item: Self) -> bool:
        return len(self.data) > len(item.data)

    def display(self):
        print(f"Length of {self.data}: {len(self.data)}")

class Rectangle(ComparableDisplayable):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.area = width * height

    def compare(self, item: Self) -> bool:
        return self.area > item.area

    def display(self):
        print(f"Area of rectangle {self.width}x{self.height}: {self.area}")

class DNA(ComparableDisplayable):
    def __init__(self, data: List[int]):
        self.data = data

    def qua_diff(self) -> int:
        return abs(self.data.count(1) - self.data.count(0))

    def compare(self, item: Self) -> bool:
        return len(self.data) < len(item.data)

    def display(self):
        print(self.data)

# Fetch Weather Data for Cities
class City(ComparableDisplayable):
    def __init__(self, city_name: str):
        self.city_name = city_name
        self.temperature = self.get_weather()

    def compare(self, item: Self) -> bool:
        return self.temperature > item.temperature

    def display(self):
        print(f"Weather in {self.city_name}: {self.temperature}°C")

    def get_weather(self) -> float:
        base_url = f"http://wttr.in/{self.city_name}?format=%C+%t+%h"
        try:
            response = requests.get(base_url)
            if response.status_code == 200:
                temp_str = response.text.strip()
                temp_str = temp_str.split("°C")[0].strip().split("+")[-1]
                return float(temp_str)
        except:
            pass
        return float("inf")  # Default to high value if request fails

# Testing Sorting Algorithms
print("Bubble Sort - String Data")
bubble_sort(Sortable([StringData("12323"), StringData("12"), StringData("1"), StringData("122313")])).show()

print("Insertion - Rectangles")
insertion_sort(Sortable([Rectangle(45, 90), Rectangle(10, 10), Rectangle(2, 2), Rectangle(100, 1)])).show()

print("Heap Sort - DNA Sequences")
heap_sort(Sortable([
    DNA([0, 0, 1, 1, 1, 1, 1, 1]),
    DNA([1, 1, 1, 1, 0, 0, 0]),
    DNA([1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]),
    DNA([1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1])
])).show()

print("Quick Sort - City Temperatures")
quick_sort(Sortable([City("London"), City("Paris"), City("Shanghai"), City("Tokyo"), City("Stockholm")])).show()
