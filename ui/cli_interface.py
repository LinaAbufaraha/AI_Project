from models.truck import Truck
from utils.file_io import read_file
from utils.distance import *

# --- Ask user for truck info ---
def display_menu():
    trucks = []
    num_trucks = int(input("Enter the number of trucks to deploy: "))
    for i in range(1, num_trucks + 1):
        capacity = float(input(f"Enter Truck {i} weight capacity: "))
        trucks.append(Truck(str(i), capacity))
    return trucks

def display_solution(best_solution, packages, trucks):
    total_assigned = set()
    for truck in trucks:
        truck_num = truck.number
        package_indices = best_solution.genes.get(truck_num, [])
        total_assigned.update(package_indices)

        assigned_packages = [packages[i] for i in package_indices]
        print(f"\nTruck {truck_num} | Capacity: {truck.weightcap} kg | Packages: {len(package_indices)}")
        total_weight = sum(pkg.weight for pkg in assigned_packages)
        print(f"  Total Weight: {total_weight:.2f} kg")

        for pkg in assigned_packages:
            print(f"  - {pkg}")

        if assigned_packages:
            x, y = 0, 0
            route_distance = 0
            for pkg in assigned_packages:
                x2, y2 = pkg.destination
                route_distance += calculate_distance(x, y, x2, y2)
                x, y = x2, y2
            route_distance += calculate_distance(x, y, 0, 0)
            print(f"  Route Distance: {route_distance:.2f} km")

    return total_assigned

