import copy
import random
import math
from typing import List
from algorithms.chromosome import *
from models.truck import Truck
from models.package import Package


class GeneticAlgorithm:
    def __init__(self, packages: List[Package], trucks: List[Truck], population_size: int = 100, generations: int = 500, mutation_rate: float = 0.2, crossover_rate: float = 0.8):
        """Initialize the genetic algorithm with parameters."""
        self.packages = packages
        self.trucks = trucks
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population: List[Chromosome] = []
        self.best_solution: Chromosome = None

    def initialize_population(self):
        """Create an initial population of random chromosomes."""
        self.population = [Chromosome(self.packages, self.trucks) for _ in range(self.population_size)]

    def tournament_selection(self, tournament_size: int = 2) -> Chromosome:
        """Select a parent using tournament selection."""
        tournament = random.sample(self.population, tournament_size)
        return min(tournament, key=lambda c: c.fitness)  # Lower fitness (distance) is better
    
    def run(self) -> Chromosome:
        """Run the genetic algorithm and return the best solution."""
        self.initialize_population()
        self.best_solution = min(self.population, key=lambda c: c.fitness)
        for gen in range(self.generations):
            new_population = []
            sorted_pop = sorted(self.population, key=lambda c: c.fitness)
            elite_count = max(1, self.population_size // 20)
            new_population.extend(copy.deepcopy(c) for c in sorted_pop[:elite_count])
            unique_solutions = len(set(tuple(tuple(sorted(pkgs)) for pkgs in c.genes.values()) for c in self.population))
            temp_mutation_rate = self.mutation_rate * (1.5 if unique_solutions < self.population_size * 0.5 else 1.0)
            while len(new_population) < self.population_size:
                parent1 = self.tournament_selection()
                parent2 = self.tournament_selection()
                if random.random() < self.crossover_rate:
                    child = parent1.crossover(parent2)
                else:
                    child = copy.deepcopy(parent1)
                child.mutate(temp_mutation_rate)
                new_population.append(child)
            self.population = new_population
            current_best = min(self.population, key=lambda c: c.fitness)
            if current_best.fitness < self.best_solution.fitness:
                self.best_solution = current_best
            if gen % 100 == 0 or gen == self.generations - 1:
                print(f"Generation {gen + 1}: Best Distance = {self.best_solution.fitness:.2f} km")
        return self.best_solution
