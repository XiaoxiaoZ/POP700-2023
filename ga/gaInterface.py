from abc import ABC
from typing import List, Self
import random


class GaPopInterface(ABC):
    def gen_indiv()->Self:
        pass
    def fitness(self)->int:
        pass
    def crossover(indiv1: Self, indiv2: Self)->Self:
        pass
    def mutate(self)->Self:
        pass

class GaAlgorithmInterface(ABC):
    iter_num: int
    pop: List[GaPopInterface]
    def gen_pop(self):
        pass
    def crossover(self):
        pass
    def mutate(self):
        pass
    def replace(self):
        pass
    def main(self):
        pass
    def restult(self):
        pass


