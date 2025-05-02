def can_fit_all_packages(packages, trucks):
    total_package_weight = sum(pkg.weight for pkg in packages)
    total_truck_capacity = sum(truck.weightcap for truck in trucks)
    return total_package_weight <= total_truck_capacity

def apply_solution_to_trucks(best_solution, packages, trucks):
    for truck in trucks:
        truck.packages.clear()  
        
        if truck.number in best_solution.genes:
            pkg_indices = best_solution.genes[truck.number]
            truck.packages = [packages[i] for i in pkg_indices]