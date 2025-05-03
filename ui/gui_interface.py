import math
import random
import copy

from utils.distance import calculate_total_distance
from utils.validation import can_fit_all_packages, apply_solution_to_trucks
from algorithms.genetic_algorithm import GeneticAlgorithm
from algorithms.simulated_annealing import SimulatedAnnealing
from utils.schedule import cooling_schedule
from utils.file_io import read_file
from utils.initial_assignment import initial_solution
from ui.cli_interface import display_menu, display_solution
from models.truck import Truck
from models.package import Package
from utils.graphs import plot_truck_paths


def operate():
    packages = read_file("data/test_case_2.txt")
    print(f"\n Loaded {len(packages)} packages.\n")


    print("Choose An Algorithm \n")
    print("1 - Simulated Annealing\n")
    print("2 - Genetic Algorithm\n")
    choice = input("Enter choice (1 or 2): ")
    trucks = display_menu()
    if choice == "1":
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

        if not can_fit_all_packages(packages, best_sa_solution):
            print("\nWarning: The total weight of packages exceeds the combined capacity of all trucks.\n")

        print(f"Total Distance (SA): {calculate_total_distance(best_sa_solution):.2f} km")
        plot_truck_paths(best_sa_solution, 1)
    elif choice == "2":
        print("\nRunning Genetic Algorithm...\n")
        ga = GeneticAlgorithm(packages, trucks)
        best_solution = ga.run()
        apply_solution_to_trucks(best_solution, packages, trucks)  # maps gene to trucks

        print("\nBest Package Assignments:\n")
        total_distance = best_solution.fitness
        assigned_packages = display_solution(best_solution, packages, trucks)

        if not can_fit_all_packages(packages, trucks):
            print("\nWarning: The total weight of packages exceeds the combined capacity of all trucks.\n")

        unassigned_count = len(packages) - len(assigned_packages)
        if unassigned_count > 0:
            print(f"Warning: Not enough total truck capacity to carry {unassigned_count} package(s).\n")

        print(f"Total Distance: {total_distance:.2f} km")
        plot_truck_paths(trucks, 0)  # now trucks contain packages from best_solution

    else:
        print("Invalid Choice\n")
