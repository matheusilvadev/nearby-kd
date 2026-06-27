# K-d Tree Nearest Courier Finder

This project implements a **2-dimensional K-d Tree** to efficiently solve the **nearest-neighbor search problem** in a geographic context. It is designed to simulate a delivery system where the goal is to find the closest courier to a given pickup location using latitude and longitude coordinates.

---

## Overview

Given a set of couriers positioned in a 2D geographic space, the system:

1. Stores couriers in a **K-d Tree (2D spatial binary search tree)**.
2. Efficiently queries the **nearest courier** to a delivery/pickup point.
3. Uses the **Haversine formula** to compute real-world distances on the Earth's surface.

This approach reduces the search space compared to brute-force distance checking.

---

## Features

- Implementation of a **2D K-d Tree**
- Recursive insertion with alternating split dimensions (latitude / longitude)
- Optimized nearest-neighbor search with **branch pruning**
- Accurate geodesic distance calculation using the **Haversine formula**
- Simple simulation of courier data input

---

## Project Structure

```text
├── main.py       # Entry point (simulation and execution)
├── kd_tree.py    # K-d Tree implementation (Node + KdTree)
└── utils.py      # Haversine distance function
```
---

## How It Works

### 1. Data Representation

Each courier is represented as a node containing:

- Unique identifier
- Latitude
- Longitude

---

### 2. K-d Tree Construction

The tree is built by recursively inserting nodes while alternating the splitting axis:

- Depth 0 → latitude
- Depth 1 → longitude
- Depth 2 → latitude
- ...

This ensures spatial partitioning of the dataset.

---

### 3. Nearest Neighbor Search

The algorithm:

1. Traverses the tree following the most promising branch first
2. Computes the distance to each visited node using the Haversine formula
3. Applies **branch pruning** by evaluating whether the opposite subtree could contain a closer point

This significantly reduces unnecessary computations compared to brute-force search.

---

### 4. Distance Calculation

Distances are computed using the **Haversine formula**, which accounts for Earth’s curvature:

\[
d = 2R \cdot \arcsin\left(\sqrt{a}\right)
\]

Where:

- \( R \) = Earth radius (6371 km)
- \( a \) = angular distance component

---

## Use Case

This project models a simplified version of systems used in:

- Delivery platforms (Uber Eats, iFood, Rappi)
- Ride-matching systems
- Geospatial indexing engines

---

## Technologies

- Python 3.x
- Standard library (`math` module only)

---

## Key Concepts

- K-d Trees (Spatial Data Structures)
- Nearest Neighbor Search
- Computational Geometry
- Geodesic Distance (Haversine Formula)

---

## Complexity

- **Insertion:** O(log n) average (balanced tree assumption)
- **Nearest search:** O(log n) average with pruning, O(n) worst case

---

## License

This project is intended for educational and demonstrative purposes.
