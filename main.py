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
from ui.gui_interface import operate

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
    operate()


