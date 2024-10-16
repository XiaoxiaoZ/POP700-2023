import random
from typing import List, Tuple

import pygame


from acoEnv import Environment, PygameRenderer
from acoInterface import IAnt, IAntColonyAlgorithm, IEnvironment, IRenderer

import random

class Ant(IAnt):
    def __init__(self, environment: IEnvironment):
        self.environment = environment
        self.tour = []  # The current path the ant is following
        self.visited = set()  # Track visited cities

    def initialize(self):
        # Start the ant at a random city
        self.tour = []
        self.visited = set()
        start_city = random.choice(self.environment.get_cities())
        self.tour.append(start_city)
        self.visited.add(start_city)

    def move(self):
        print(self.environment.get_cities())
        if len(self.tour) < len(self.environment.get_cities()):
            current_city = self.tour[-1]
            next_city = self._choose_next_city(current_city)
            if next_city is not None:
                self.tour.append(next_city)
                self.visited.add(next_city)

    def has_found_goal(self):

        # The ant has found the goal if it has visited all cities
        return len(self.tour) == len(self.environment.get_cities())

    def deposit_pheromone(self):
        # Deposit pheromone along the path taken by the ant
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            distance = self.environment.get_distance(city1, city2)
            # Deposit pheromone inversely proportional to the distance of the tour
            self.environment.update_pheromone(city1, city2, 1 / distance)

    def _choose_next_city(self, current_city):
        # Get the cities that have not been visited yet
        unvisited_cities = set(self.environment.get_cities()) - self.visited
        if not unvisited_cities:
            return None  # No more cities to visit
        
        # Compute probabilities based on pheromone levels and distances
        probabilities = []
        total_sum = 0

        for city in unvisited_cities:
            pheromone_level = self.environment.get_pheromone_level(current_city, city)
            distance = self.environment.get_distance(current_city, city)
            if distance == 0:
                distance = 0.00001  # Avoid division by zero

            desirability = (pheromone_level ** 2) * (1 / distance)  # Typical formula: pheromone^alpha * (1/distance)^beta
            probabilities.append((city, desirability))
            total_sum += desirability

        if total_sum == 0:
            return random.choice(list(unvisited_cities))  # If all probabilities are 0, randomly choose a city

        # Normalize probabilities
        probabilities = [(city, desirability / total_sum) for city, desirability in probabilities]

        # Select next city using roulette wheel selection
        return self._roulette_wheel_selection(probabilities)

    def _roulette_wheel_selection(self, probabilities):
        r = random.random()
        cumulative_sum = 0.0
        for city, probability in probabilities:
            cumulative_sum += probability
            if r <= cumulative_sum:
                return city
        return probabilities[-1][0]  # Return the last city as a fallback


class AntColonyAlgorithm(IAntColonyAlgorithm):
    def __init__(self, num_ants, cities, num_iterations, evaporation_rate=0.2, step_delay=500):
        self.environment = Environment(cities, evaporation_rate)
        self.ants = [Ant(self.environment) for _ in range(num_ants)]
        self.renderer = PygameRenderer()
        self.num_iterations = num_iterations
        self.step_delay = step_delay  # Delay between each step (in milliseconds)

    def initialize(self):
        for ant in self.ants:
            ant.initialize()

    def run(self):
        for iteration in range(self.num_iterations):
            self.environment.evaporate_pheromone()  # Evaporate pheromones
            self.initialize()  # Initialize ants for a new iteration

            # Move each ant to complete their tour
            for ant in self.ants:
                while not ant.has_found_goal():
                    ant.move()

                    # Render after each ant's move
                    self.renderer.handle_events()  # Handle window close events
                    self.renderer.render_environment(self.environment)
                    self.renderer.render_ants(self.ants)
                    self.renderer.update()

                    pygame.time.delay(self.step_delay)  # Pause for step visualization

            # Update pheromones based on ants' tours
            for ant in self.ants:
                ant.deposit_pheromone()

        # Keep the window open until manually closed
        while True:
            self.renderer.handle_events()



def generate_random_cities(num_cities, x_range=(0, 8), y_range=(0, 6)):
    """Generates a list of cities with random (x, y) coordinates."""
    cities = []
    for _ in range(num_cities):
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        cities.append((x, y))
    return cities

num_cities = 15
cities = generate_random_cities(num_cities)  # Generate 10 random cities

algorithm = AntColonyAlgorithm(num_ants=10, cities=cities, num_iterations=200,evaporation_rate=0.4, step_delay=1)
algorithm.run()