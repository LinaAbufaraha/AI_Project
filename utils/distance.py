import math

# --- Distance calculation ---
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def truck_distance(truck):
    total = 0
    x1, y1 = 0, 0  # Start from shop
    for pkg in truck.packages:
        x2, y2 = pkg.destination
        total += calculate_distance(x1, y1, x2, y2)
        x1, y1 = x2, y2
    # Optional: return to shop
    total += calculate_distance(x1, y1, 0, 0)
    return total

def total_distance(trucks):
    return sum(truck_distance(truck) for truck in trucks)