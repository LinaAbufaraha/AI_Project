import copy
import random
import math
from typing import Dict, List
from models.truck import Truck
from models.package import Package

class Chromosome:
    def __init__(self, packages: List[Package], trucks: List[Truck]):
        """Initialize a chromosome with a random valid assignment of packages to trucks."""
        self.packages = packages
        self.trucks = trucks
        self.genes: Dict[str, List[int]] = {truck.number: [] for truck in trucks}  # truck_id: list of package indices
        self.fitness: float = float('inf')
        self._generate_valid_random_assignment()
        self._calculate_fitness()

    def _truck_weight(self, truck_id: str) -> float:
        """Calculate the total weight of packages assigned to a truck."""
        return sum(self.packages[pkg_index].weight for pkg_index in self.genes[truck_id])
    

    def _generate_valid_random_assignment(self):
        """Assign packages to trucks randomly, prioritizing high-priority packages."""
        unassigned = list(range(len(self.packages)))
        unassigned.sort(key=lambda i: self.packages[i].priority)  # Prioritize high-priority
        for pkg_index in unassigned:
            pkg = self.packages[pkg_index]
            truck_order = self.trucks.copy()
            random.shuffle(truck_order)
            for truck in truck_order:
                if self._truck_weight(truck.number) + pkg.weight <= truck.weightcap:
                    self.genes[truck.number].append(pkg_index)
                    break

    def _calculate_fitness(self):
        """Calculate fitness as total distance, with penalties for unassigned packages."""
        total_distance = 0
        assigned_packages = set()
        shop = (0, 0)

        for truck in self.trucks:
            truck_id = truck.number
            if not self.genes[truck_id]:
                continue
            x, y = shop
            for pkg_index in self.genes[truck_id]:
                if pkg_index in assigned_packages:
                    total_distance += 10000  # Penalty for duplicates
                assigned_packages.add(pkg_index)
                pkg = self.packages[pkg_index]
                x2, y2 = pkg.destination
                total_distance += math.sqrt((x2 - x)**2 + (y2 - y)**2)
                x, y = x2, y2
            total_distance += math.sqrt(x**2 + y**2)
        
        # Penalty for priority violations
        #priority_penalties = 0
        for truck_id in self.genes:
            for i in range(len(self.genes[truck_id]) - 1):
                pkg1 = self.packages[self.genes[truck_id][i]]
                pkg2 = self.packages[self.genes[truck_id][i + 1]]
                if pkg1.priority > pkg2.priority:  # Lower priority delivered first
                    total_distance += 200
        #print(f"Priority penalties applied: {priority_penalties}")  # Debug
        self.fitness = total_distance

    def mutate(self, mutation_rate: float = 0.2):
        """Mutate by swapping packages or shuffling routes, respecting capacity."""
        for _ in range(2):  # Multiple mutation attempts
            for truck in self.trucks:
                truck_id = truck.number
                if random.random() < mutation_rate and len(self.genes[truck_id]) > 1:
                    random.shuffle(self.genes[truck_id])
                if random.random() < mutation_rate and self.genes[truck_id]:
                    pkg_index = random.choice(self.genes[truck_id])
                    pkg = self.packages[pkg_index]
                    other_trucks = [t for t in self.trucks if t.number != truck_id]
                    random.shuffle(other_trucks)
                    for other_truck in other_trucks:
                        if self._truck_weight(other_truck.number) + pkg.weight <= other_truck.weightcap:
                            self.genes[truck_id].remove(pkg_index)
                            self.genes[other_truck.number].append(pkg_index)
                            break
        self._calculate_fitness()

    def crossover(self, other: 'Chromosome') -> 'Chromosome':
        child = Chromosome(self.packages, self.trucks)
        child.genes = {truck.number: [] for truck in self.trucks}
        used_packages = set()
        # Randomly select a subset of packages from each parent
        for truck in self.trucks:
            truck_id = truck.number
            source = self if random.random() < 0.5 else other
            pkg_indices = source.genes[truck_id].copy()
            random.shuffle(pkg_indices)
            for pkg_index in pkg_indices[:len(pkg_indices)//2]:  # Take half
                if pkg_index not in used_packages:
                    pkg = self.packages[pkg_index]
                    if child._truck_weight(truck_id) + pkg.weight <= truck.weightcap:
                        child.genes[truck_id].append(pkg_index)
                        used_packages.add(pkg_index)
        # Assign remaining packages randomly
        remaining = [i for i in range(len(self.packages)) if i not in used_packages]
        random.shuffle(remaining)
        for pkg_index in remaining:
            pkg = self.packages[pkg_index]
            truck_order = self.trucks.copy()
            random.shuffle(truck_order)
            for truck in truck_order:
                if child._truck_weight(truck.number) + pkg.weight <= truck.weightcap:
                    child.genes[truck.number].append(pkg_index)
                    break
        child._calculate_fitness()
        return child
                 