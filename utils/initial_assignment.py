import random
import math
import copy
from typing import Dict, List
from models.truck import Truck


def initial_solution(packages, trucks):
    # Create a deep copy of the trucks to avoid modifying the original list
    temp_trucks = copy.deepcopy(trucks)

    # Shuffle the list of packages
    shuffled_packages = packages[:]
    random.shuffle(shuffled_packages)

    # Shuffle the trucks as well
    random.shuffle(temp_trucks)

    # Assign each package to a truck
    for package in shuffled_packages:
        for truck in temp_trucks:
            if truck.add_package(package):
                break

    return temp_trucks
