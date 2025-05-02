from ui.cli_interface import display_menu
from models.truck import Truck
import random
from utils.distance import calculate_distance
from algorithms.genetic_algorithm import GeneticAlgorithm
from utils.file_io import read_file



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
    packages = read_file("data/input.txt")
    print(f"\n Loaded {len(packages)} packages.\n")

    trucks = display_menu()

    #initial_solution(packages, trucks)

    #print("\n Package Assignments:\n")
    #for truck in trucks:
     #   print(truck)
      #  for pkg in truck.packages:
       #     print(f"  - {pkg}")
        #print()
    #print("Total distance:", total_distance(trucks))

    # Run genetic algorithm
    print("\nRunning Genetic Algorithm...\n")
    ga = GeneticAlgorithm(packages, trucks)
    best_solution = ga.run()

    # Display results
    print("\nBest Package Assignments:\n")
    total_distance = best_solution.fitness
    for truck in trucks:
        truck_num = truck.number
        package_indices = best_solution.genes[truck_num]
        print(f"Truck {truck_num} | Weight Capacity: {truck.weightcap} | Packages: {len(package_indices)}")
        total_weight = sum(packages[pkg_index].weight for pkg_index in package_indices)
        print(f"  Total Weight: {total_weight:.2f} kg")
        for pkg_index in package_indices:
            print(f"  - {packages[pkg_index]}")
        route_distance = 0
        if package_indices:
            x, y = 0, 0
            for pkg_index in package_indices:
                x2, y2 = packages[pkg_index].destination
                route_distance += calculate_distance(x, y, x2, y2)
                x, y = x2, y2
            route_distance += calculate_distance(x, y, 0, 0)
        print(f"  Route Distance: {route_distance:.2f} km\n")
    print(f"Total Distance: {total_distance:.2f} km")