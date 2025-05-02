import math
import random
from models.package import *

# --- Truck class ---
class Truck:
    def __init__(self, number, weightcap):
        self.number = number
        self.weightcap = weightcap
        self.packages = []

    def current_weight(self):
        return sum(p.weight for p in self.packages)

    
    def can_add_package(self, package: Package) -> bool:
        return self.current_weight() + package.weight <= self.weightcap


    def __str__(self):
        return f'Truck {self.number} | Weight Capacity: {self.weightcap} | Packages: {len(self.packages)}'


