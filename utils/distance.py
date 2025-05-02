import math

# --- Distance calculation ---
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def calculate_total_distance(trucks):
    total = 0
    curr_dest_x=0
    curr_dest_y=0
    for truck in trucks:

        for package in truck.packages:

            total += calculate_distance(curr_dest_x, curr_dest_y, package.destination[0], package.destination[1])
            curr_dest_x = package.destination[0]
            curr_dest_y = package.destination[1]
        total+=calculate_distance(curr_dest_x, curr_dest_y,0, 0)
    return total

def can_fit_all_packages(packages, trucks):
    total_package_weight = sum(pkg.weight for pkg in packages)
    total_truck_capacity = sum(truck.weightcap for truck in trucks)
    return total_package_weight <= total_truck_capacity


'''def truck_distance(truck):
    total = 0
    x1, y1 = 0, 0  # Start from shop
    for pkg in truck.packages:
        x2, y2 = pkg.destination
        total += calculate_distance(x1, y1, x2, y2)
        x1, y1 = x2, y2
    #  return to shop
    total += calculate_distance(x1, y1, 0, 0)
    return total

def total_distance(trucks):
    return sum(truck_distance(truck) for truck in trucks)'''