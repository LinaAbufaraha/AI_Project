# 🚚 AI Package Delivery Optimization – ENCS3340 Project

This project was developed for the Artificial Intelligence course (ENCS3340) . It addresses a real-world logistics optimization problem: **minimizing the total travel distance of delivery trucks while respecting package priorities and vehicle capacity constraints**.

---

## 🧠 Problem Overview

A local delivery shop receives multiple packages each day, each with:
- A destination (x, y) on a 2D grid.
- A weight in kilograms.
- A priority level (1 = highest, 5 = lowest).

The shop owns a limited number of trucks with fixed capacity. The challenge is to:
- Assign packages to trucks.
- Plan each truck’s delivery route.
- Optimize for **minimum total travel distance**, while handling constraints like:
  - **Truck weight capacity**.
  - **Package priorities** (soft constraint, may be violated for efficiency).

---

## 🛠 Algorithms Used

### 🔹 Genetic Algorithm (GA)
- Chromosome-based representation of assignments.
- Selection, crossover, and mutation for evolving solutions.
- Priority violations penalized.
- Over-capacity trucks rejected.

### 🔹 Simulated Annealing (SA)
- Starts with a random solution.
- Neighbor generation via package swaps.
- Probabilistic acceptance of worse solutions (temperature-based).
- Lightweight and fast for smaller cases.

---

## 💡 Features

- Choose between GA and SA at runtime.
- Input configuration: number of trucks, their capacity, and package data.
- **Graphical User Interface (GUI)** to display assignments and distances.
- **Warning system** for overcapacity and unassigned packages.

---

## 📊 Parameter Tuning

### GA Parameters
- Population Size: `80`
- Mutation Rate: `0.1`
- Number of Generations: `500`

### SA Parameters
- Initial Temperature: `1000`
- Cooling Rate: `0.95`
- Stopping Temperature: `1`
- Iterations per Temperature: `100`

---
