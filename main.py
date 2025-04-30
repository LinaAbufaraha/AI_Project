from utils.file_io import read_file
from ui.cli_interface import display_menu
from models.truck import Truck
import random
from utils.distance import total_distance


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

    initial_solution(packages, trucks)

    print("\n Package Assignments:\n")
    for truck in trucks:
        print(truck)
        for pkg in truck.packages:
            print(f"  - {pkg}")
        print()
    print("Total distance:", total_distance(trucks))

