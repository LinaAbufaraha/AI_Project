from models.truck import Truck
from utils.file_io import read_file


# --- Ask user for truck info ---
def display_menu():
    trucks = []
    num_trucks = int(input("Enter the number of trucks to deploy: "))
    for i in range(1, num_trucks + 1):
        capacity = float(input(f"Enter Truck {i} weight capacity: "))
        trucks.append(Truck(str(i), capacity))
    return trucks

# ui/cli_interface.py

from algorithms.genetic_algorithm import GeneticAlgorithm
from utils.file_io import read_file
from models.truck import Truck

'''def run_genetic_algorithm():
    print("🔬 Running Genetic Algorithm for Package Delivery Optimization...\n")

    # تحميل البيانات
    packages = read_file("data/input.txt")


    # إعداد الشاحنات (يمكن لاحقًا قراءتها من ملف أو إدخال المستخدم)
    num_trucks = 3
    truck_capacity = 50

    # تشغيل الخوارزمية
    ga = GeneticAlgorithm(packages, num_trucks, truck_capacity,
                          population_size=50, generations=100, mutation_rate=0.05)
    best = ga.run()

    # عرض النتيجة
    print("\n✅ Best Solution Found:")
    for i, truck in enumerate(best.genes):
        print(f"  Truck {i + 1}:")
        for pkg_index in truck:
            pkg = packages[pkg_index]
            print(f"    - To {pkg.destination}, Weight: {pkg.weight}, Priority: {pkg.priority}")
    print(f"\n📏 Total Distance: {best.fitness:.2f} km")
    '''
