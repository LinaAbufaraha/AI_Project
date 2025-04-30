from models.package import Package

# --- Read packages from file ---
def read_file(filename):
    packages = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 4:
                continue
            x, y = int(parts[0]), int(parts[1])
            weight = float(parts[2])
            priority = int(parts[3])
            package = Package([x, y], weight, priority)
            packages.append(package)
    return packages

          