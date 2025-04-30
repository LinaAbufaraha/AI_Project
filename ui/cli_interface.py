from models.truck import Truck

# --- Ask user for truck info ---
def display_menu():
    trucks = []
    num_trucks = int(input("Enter the number of trucks to deploy: "))
    for i in range(1, num_trucks + 1):
        capacity = float(input(f"Enter Truck {i} weight capacity: "))
        trucks.append(Truck(str(i), capacity))
    return trucks
