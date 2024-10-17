import random
from typing import List, Tuple

import pygame


from acoEnv import Environment, PygameRenderer
from acoInterface import IAnt, IAntColonyAlgorithm, IEnvironment, IRenderer

import random

class Ant(IAnt):
    def __init__(self, environment: IEnvironment):
        self.environment = environment
        self.tour = []
    """ YOU NEED TO FIX THIS CLASS"""
    def initialize(self):
        pass

    def move(self):
        pass

    def has_found_goal(self):
        pass

    def deposit_pheromone(self):
        pass


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