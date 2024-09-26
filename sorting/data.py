import math
from typing import List, Self
from sortableInterface import Campare, Sortable, display
from algorithms import bubble_sort, heap_sort, insertion_sort, quick_sort, selection_sort


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
            
class Human(Campare,display):
    def __init__(self, age:int, height:float):
        self.age = age
        self.height = height
    def compare(self, item: Self) -> bool:
        return self.age> item.age
    def print(self):
        print("age:"+str(self.age)+",height:"+str(self.height))

class StringData(Campare,display):
    def __init__(self, data: str):
        self.data=data
    def compare(self, item: Self) -> bool:
        return len(self.data)> len(item.data)
    def print(self):
        print("Length of :"+self.data+" is"+ str(len(self.data)))

bubble_sort(SortableData([StringData("12323"),StringData("12"),StringData("1"),StringData("122313")])).print()

class Rectangle(Campare, display):
    def __init__(self, width:float, height:float):
        self.width = width
        self.height = height
        self.area = width* height
    def compare(self, item: Self) -> bool:
        return self.width<item.width
    def print(self):
        print("Area of rectangle with width "+str(self.width)+" and height " +str(self.height)+" is "+str(self.area))

bubble_sort(SortableData([Rectangle(45,90),Rectangle(10,10),Rectangle(2,2),Rectangle(100,1)])).print()
class DNA(Campare, display):
    def __init__(self, data: List[int]):
        self.data = data
    def ones(self)->int:
        return self.data.count(1)
    def zeros(self)->int:
        return self.data.count(0)
    def qua_diff(self):
        return abs(self.ones()-self.zeros())
    def compare(self, item: Self) -> bool:
        return len(self.data)<len(item.data)
    def print(self):
        print(self.data)

bubble_sort(SortableData([DNA([0,0,1,1,1,1,1,1]),DNA([1,1,1,1,0,0,0]),DNA([1,1,1,1,0,0,0,0,0,0,0]),DNA([1,1,1,1,0,0,0,1,1,1,1,1,1,1])])).print()

"""
print("bubble sort")
bubble_sort(SortableData([Human(10,100),Human(20,180),Human(12, 200),Human(32, 200),Human(22, 200),Human(24, 200)])).print()
print("selection sort")
selection_sort(SortableData([Human(10,100),Human(20,180),Human(12, 200),Human(32, 200),Human(22, 200),Human(24, 200)])).print()
print("insertion sort")
insertion_sort(SortableData([Human(10,100),Human(20,180),Human(12, 200),Human(32, 200),Human(22, 200),Human(24, 200)])).print()
print("heap sort")
heap_sort(SortableData([Human(10,100),Human(20,180),Human(12, 200),Human(32, 200),Human(22, 200),Human(24, 200)])).print()
print("quick sort")
quick_sort(SortableData([Human(10,100),Human(20,180),Human(12, 200),Human(32, 200),Human(22, 200),Human(24, 200)])).print()

"""
# string, sort based on length
# rectangle, sort based on area
# [0,1,0,1,1,1,1] type of binary list, sort based on the quantitative difference of 1 and 0
# get temperature of cities and compare, here is a function how to get data from webservice through api
import requests
def get_weather_no_api(city_name):
    base_url = f"http://wttr.in/{city_name}?format=%C+%t+%h"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        temp_str = response.text.strip()
        # Remove everything after '°C'
        if '°C' in temp_str:
            temp_str = temp_str.split('°C')[0].strip()  # Split and take the part before '°C'
        # Find the position of the '+' or '-' and extract everything after it
        if '+' in temp_str:
            temp_str = temp_str.split('+')[-1]
        elif '−' in temp_str or '-' in temp_str:  # Handle both the '−' character and regular '-'
            temp_str = temp_str.split('−')[-1] if '−' in temp_str else temp_str.split('-')[-1]
            temp_str = '-' + temp_str  # Add back the negative sign
            
        # Convert to float or int as needed
        try:
            print(float(temp_str))
        except ValueError:
            print("Could not parse temperature value.")
    else:
        print("Unable to get weather data")
get_weather_no_api('London')









"""
import requests
class City(Campare,display):
    def __init__(self, city_name: str):
        self.weather_data = 1000000000
        self.city_name = city_name
        self.get_weather_no_api()
    def compare(self, item: Self) -> bool:
        return self.weather_data> item.weather_data
    def print(self):
        print(f"Weather in {self.city_name}: {self.weather_data}")
    def get_weather_no_api(self):
        base_url = f"http://wttr.in/{self.city_name}?format=%C+%t+%h"
        response = requests.get(base_url)
        
        if response.status_code == 200:
            temp_str = response.text.strip()
            # Remove everything after '°C'
            if '°C' in temp_str:
                temp_str = temp_str.split('°C')[0].strip()  # Split and take the part before '°C'
            # Find the position of the '+' or '-' and extract everything after it
            if '+' in temp_str:
                temp_str = temp_str.split('+')[-1]
            elif '−' in temp_str or '-' in temp_str:  # Handle both the '−' character and regular '-'
                temp_str = temp_str.split('−')[-1] if '−' in temp_str else temp_str.split('-')[-1]
                temp_str = '-' + temp_str  # Add back the negative sign
                
            # Convert to float or int as needed
            try:
                self.weather_data = float(temp_str)
            except ValueError:
                print("Could not parse temperature value.")
        else:
            print("Unable to get weather data")


quick_sort(SortableData([City('London'),City('Paris'),City('Shanghai'),City('Tokio'),City('Stockholm')])).print()
"""