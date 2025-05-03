import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def plot_truck_paths(trucks,f):
    num_trucks = len(trucks)
    colors = plt.get_cmap('tab20', num_trucks)
    plt.figure(figsize=(14, 10))

    for idx, truck in enumerate(trucks):
        coords = [(0, 0)]  # Start at depot
        for pkg in truck.packages:
            coords.append(tuple(pkg.destination))
        coords.append((0, 0))  # Return to depot

        xs, ys = zip(*coords)

        # Plot path
        plt.plot(xs, ys, marker='o', color=colors(idx), linewidth=4, label=f'Truck {truck.number}')

        # Draw arrows
        for i in range(len(coords) - 1):
            x0, y0 = coords[i]
            x1, y1 = coords[i + 1]
            dx, dy = x1 - x0, y1 - y0
            plt.arrow(x0, y0, dx * 0.85, dy * 0.85,
                      head_width=2.0, head_length=4.0,
                      length_includes_head=True,
                      fc=colors(idx), ec=colors(idx), alpha=0.8)

        # Annotate package priorities
        for i, pkg in enumerate(truck.packages):
            x, y = pkg.destination
            plt.text(x + 1, y + 1, f'P{pkg.priority}', fontsize=9, color='black', weight='bold')
    if (f==1):
        plt.title('Optimized Delivery Routes(Simulated Annealing Algorithm)', fontsize=14, weight='bold')
    else:
        plt.title('Optimized Delivery Routes(Genetics Algorithm)', fontsize=14, weight='bold')
    plt.xlabel('X Coordinate', fontsize=12)
    plt.ylabel('Y Coordinate', fontsize=12)
    plt.grid(True, linestyle='-', alpha=0.5)
    plt.xticks(np.arange(0, 101, 10))
    plt.yticks(np.arange(0, 101, 10))
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.legend(loc='upper right', fontsize=10, frameon=True)
    plt.tight_layout()
    plt.show()



