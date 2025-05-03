from ui.cli_interface import display_menu , display_solution
from models.truck import Truck
import random
import copy

from utils.distance import *
from utils.validation import can_fit_all_packages , apply_solution_to_trucks
from algorithms.genetic_algorithm import GeneticAlgorithm
from algorithms.simulated_annealing import SimulatedAnnealing
from utils.schedule import cooling_schedule
from utils.file_io import read_file
from utils.initial_assignment import initial_solution


# --- Assign packages initially (no weight violation) ---
def initial_solution(packages, trucks):
    for package in packages:
        possible_trucks = [truck for truck in trucks if truck.can_add_package(package)]
        if possible_trucks:
            chosen_truck = random.choice(possible_trucks)
            chosen_truck.packages.append(package)
        else:
            print(f" Warning: Package {package} could not be assigned (too heavy).")


# --- Main execution ---
if __name__ == "__main__":
    packages = read_file("data/test_case_4.txt")
    print(f"\n Loaded {len(packages)} packages.\n")

    trucks = display_menu()

    # ----------------- Run Simulated Annealing -----------------
    print("\nRunning Simulated Annealing...\n")
    trucks_sa = copy.deepcopy(trucks)
    
    sa = SimulatedAnnealing(initial_solution_func=initial_solution, schedule_func=cooling_schedule)
    best_sa_solution = sa.run(packages, trucks_sa)

    print("\nSimulated Annealing Result:\n")
    for truck in best_sa_solution:
        print(truck)
        for pkg in truck.packages:
            print(f"  - {pkg}")
        print()

    if not can_fit_all_packages(packages, trucks):
        print("\n Warning: The total weight of packages exceeds the combined capacity of all trucks. \n")

    
    print(f"Total Distance (SA): {calculate_total_distance(best_sa_solution):.2f} km")
       # print("Terminating optimization. Please add more trucks or increase their capacities.")
    

    # ----------------- Run genetic algorithm -----------------
    print("\nRunning Genetic Algorithm...\n")
    ga = GeneticAlgorithm(packages, trucks)
    best_solution = ga.run()
    apply_solution_to_trucks(best_solution, packages, trucks)

    # Display results
    print("\nBest Package Assignments:\n")
    total_distance = best_solution.fitness

    assigned_packages = display_solution(best_solution, packages, trucks)

    # Check if total capacity is sufficient
    if not can_fit_all_packages(packages, trucks):
        print("\n Warning: The total weight of packages exceeds the combined capacity of all trucks.")  

    unassigned_count = len(packages) - len(assigned_packages)
    if unassigned_count > 0:
        print(f" Warning: Not enough total truck capacity to carry {unassigned_count} package(s).\n")

    print(f"Total Distance: {total_distance:.2f} km")