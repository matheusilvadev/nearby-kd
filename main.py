from kd_tree import KdTree

# Simulated dataset representing couriers retrieved from a database.
couriers = [
    {"id": "Courier_A", "lat": -23.5631, "lon": -46.6543},  # Paulista
    {"id": "Courier_B", "lat": -23.5920, "lon": -46.6727},  # Itaim Bibi
    {"id": "Courier_C", "lat": -23.5406, "lon": -46.6341},  # Centro
    {"id": "Courier_D", "lat": -23.5705, "lon": -46.6451},  # Paraíso
]

# Pickup location (restaurant / delivery point)
pickup_lat = -23.5615
pickup_lon = -46.6560

# Build and populate the K-d Tree
tree = KdTree()
for courier in couriers:
    tree.insert(courier)

# Query nearest courier to the pickup location
best_node, best_distance = tree.find_nearest(pickup_lat, pickup_lon)

# Output result
if best_node:
    print("-" * 50)
    print("          NEAREST COURIER FOUND          ")
    print("-" * 50)
    print(f"Courier ID: {best_node.id}")
    print(f"Distance to pickup: {best_distance:.2f} km")
    print(f"Coordinates: Lat {best_node.latitude}, Lon {best_node.longitude}")
    print("-" * 50)
else:
    print("No courier found in the tree.")