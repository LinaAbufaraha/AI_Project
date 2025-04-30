import math
import random

# --- Package class ---
class Package:
    def __init__(self, destination, weight, priority):
        if not (isinstance(destination, list) and len(destination) == 2):
            raise ValueError("Destination must be a list of two coordinates [x, y]")
        self.destination = destination
        self.weight = weight
        self.priority = priority

    def __str__(self):
        return f'Destination: ({self.destination[0]}, {self.destination[1]}) | Weight: {self.weight} | Priority: {self.priority}'
