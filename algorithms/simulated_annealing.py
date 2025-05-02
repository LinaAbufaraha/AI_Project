import math
import random
import copy
from utils.distance import calculate_total_distance as calculate_total_distance
from models.truck import Truck
from utils.initial_assignment import initial_solution

class SimulatedAnnealing:
    def __init__(self, initial_solution_func, schedule_func):
        self.initial_solution = initial_solution_func
        self.schedule = schedule_func

    def generate_neighbor(self, current_trucks):
        new_trucks = copy.deepcopy(current_trucks)

        # Collect all package positions
        package_positions = []
        truck_index = 0
        for truck in new_trucks:
            pkg_index = 0
            for _ in truck.packages:
                package_positions.append((truck_index, pkg_index))
                pkg_index += 1
            truck_index += 1

        if len(package_positions) < 2:
            return new_trucks

        # Pick two packages
        (t1, p1), (t2, p2) = random.sample(package_positions, 2)
        # print((t1, p1), (t2, p2))

        truck1 = new_trucks[t1]
        truck2 = new_trucks[t2]

        pkg1 = truck1.packages[p1]
        pkg2 = truck2.packages[p2]

        # If both packages are in the same truck
        if t1 == t2:
            # Make sure we delete the higher index first to avoid shifting issues
            if p1 > p2:
                del truck1.packages[p1]
                del truck1.packages[p2]
            else:
                del truck1.packages[p2]
                del truck1.packages[p1]
        else:
            # Different trucks, safe to delete without worrying about index shift
            del truck1.packages[p1]
            del truck2.packages[p2]

        # Try to insert each package into the other's position
        # We'll simulate the constraint check manually
        if truck1.can_add_package(pkg2) and truck2.can_add_package(pkg1):
            truck1.packages.insert(p1, pkg2)
            truck2.packages.insert(p2, pkg1)
        else:
            # Revert if not valid
            truck1.packages.insert(p1, pkg1)
            truck2.packages.insert(p2, pkg2)

        return new_trucks
    
    def calculate_penalty(self, trucks):
        penalty = 0
        for truck in trucks:
            actual = [pkg.priority for pkg in truck.packages]
            expected = sorted(actual)
            for i in range(len(actual)):
                if actual[i] != expected[i]:
                    penalty += 1
        return penalty

    #simulated_annealing
    def run(self, packages, trucks):
        current = initial_solution(packages, trucks)
        current_value = calculate_total_distance(current)
        current_penalty = self.calculate_penalty(current)

        best_solution = copy.deepcopy(current)
        best_value = current_value
        best_penalty = current_penalty
        # 13500 = 100*135 where 135 is the number of iterations per cooling rate
        for t in range(1, 13500):
            T = self.schedule(t)  # T = schedule(t)
            if T == 0:
                return best_solution

            next_solution = self.generate_neighbor(current)
            next_value = calculate_total_distance(next_solution)
            next_penalty = self.calculate_penalty(next_solution)

            if next_penalty < current_penalty and next_value <= current_value*1.2 :
                # Accept better penalty even if distance is slightly worse
                current = next_solution
                current_value = next_value
                current_penalty = next_penalty

                if next_penalty < best_penalty or (next_penalty == best_penalty and next_value < best_value):
                    best_solution = copy.deepcopy(next_solution)
                    best_value = next_value
                    best_penalty = next_penalty

            elif next_penalty == current_penalty:
                ΔE = current_value - next_value
                if ΔE > 0:
                    # Better distance with same penalty
                    current = next_solution
                    current_value = next_value
                    # penalty stays the same
                    if next_value < best_value:
                        best_solution = copy.deepcopy(next_solution)
                        best_value = next_value
                else:
                    # Possibly accept worse distance with same penalty
                    probability = math.exp(ΔE / T)
                    if random.random() < probability:
                        current = next_solution
                        current_value = next_value
        return best_solution



