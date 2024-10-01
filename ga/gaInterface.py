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



# Concrete implementation of GaPopInterface
class BinaryChromosome(GaPopInterface):
    def __init__(self, chromosome: List[int] = None, length: int = 100):
        if chromosome is None:
            # Generate a random chromosome if none provided
            self.chromosome = [random.randint(0, 1) for _ in range(length)]
        else:
            self.chromosome = chromosome
        self.length = length

    # Generate a random individual
    def gen_indiv(self) -> 'BinaryChromosome':
        return BinaryChromosome(length=self.length)

    # Fitness function: count the number of 1s in the chromosome
    def fitness(self) -> int:
        return sum(self.chromosome)

    # Crossover between two individuals
    def crossover(indiv1: 'BinaryChromosome', indiv2: 'BinaryChromosome') -> 'BinaryChromosome':
        # Single point crossover
        crossover_point = random.randint(1, indiv1.length - 1)
        new_chromosome = indiv1.chromosome[:crossover_point] + indiv2.chromosome[crossover_point:]
        return BinaryChromosome(new_chromosome)

    # Mutate the individual by flipping a random bit
    def mutate(self) -> 'BinaryChromosome':
        mutation_point = random.randint(0, self.length - 1)
        new_chromosome = self.chromosome[:]
        # Flip the bit
        new_chromosome[mutation_point] = 1 - new_chromosome[mutation_point]
        return BinaryChromosome(new_chromosome)

    def __repr__(self):
        return f'Chromosome: {self.chromosome} | Fitness: {self.fitness()}'
    
class SimpleGA(GaAlgorithmInterface):
    def __init__(self, iter_num: int, pop_size: int, indiv_class: GaPopInterface):
        self.iter_num=iter_num
        self.pop_size= pop_size
        self.indiv_class = indiv_class

    # Generate initial population
    def gen_pop(self):
        self.pop = [self.indiv_class().gen_indiv() for _ in range(self.pop_size)]

    # Perform crossover for a certain proportion of the population
    def crossover(self):
        new_pop = []
        for _ in range(self.pop_size // 2):
            parent1 = random.choice(self.pop)
            parent2 = random.choice(self.pop)
            new_pop.append(self.indiv_class.crossover(parent1, parent2))
        self.pop += new_pop

    # Mutate a small proportion of the population
    def mutate(self):
        for i in range(self.pop_size):
            if random.random() < 0.1:  # mutation probability
                self.pop[i] = self.pop[i].mutate()

    # Replace the old population with the new one based on fitness
    def replace(self):
        # Sort population by fitness and select the top pop_size individuals
        self.pop = sorted(self.pop, key=lambda x: x.fitness(), reverse=True)[:self.pop_size]

    # Main algorithm loop
    def main(self):
        self.gen_pop()
        for iteration in range(self.iter_num):
            self.crossover()
            self.mutate()
            self.replace()
            print(f"Iteration {iteration}: Best fitness = {self.pop[0].fitness()}")

    # Get the result of the algorithm (best individual)
    def result(self):
        best_individual = max(self.pop, key=lambda x: x.fitness())
        return best_individual


# Example usage:
if __name__ == "__main__":
    ga = SimpleGA(iter_num=500, pop_size=200, indiv_class=BinaryChromosome)
    ga.main()
    print(f"Best individual: {ga.result()}")