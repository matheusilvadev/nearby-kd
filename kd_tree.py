"""
Implementation of a 2-dimensional K-d Tree used to organize courier locations
and perform nearest-neighbor searches.
"""

from utils import haversine_distance


class Node:
    """
    Represents a node in the K-d Tree.

    Each node stores a courier's identifier, geographic coordinates,
    and references to its left and right child nodes.
    """

    def __init__(self, courier_id, lat, lon):
        self.id = courier_id
        self.latitude = lat
        self.longitude = lon
        self.left = None
        self.right = None


class KdTree:
    """
    Two-dimensional K-d Tree for storing courier locations and finding
    the nearest courier to a target coordinate.
    """

    def __init__(self):
        # Root node of the tree.
        self.root = None

    def insert(self, courier):
        # Insert the first node as the tree root.
        if self.root is None:
            self.root = Node(courier["id"], courier["lat"], courier["lon"])
        else:
            self._insert_rec(self.root, courier, depth=0)

    def _insert_rec(self, current_node, courier, depth):
        if current_node is None:
            return Node(courier["id"], courier["lat"], courier["lon"])

        # Alternate the splitting axis: latitude (0) and longitude (1).
        axis = depth % 2

        if axis == 0:
            if courier["lat"] < current_node.latitude:
                current_node.left = self._insert_rec(current_node.left, courier, depth + 1)
            else:
                current_node.right = self._insert_rec(current_node.right, courier, depth + 1)
        else:
            if courier["lon"] < current_node.longitude:
                current_node.left = self._insert_rec(current_node.left, courier, depth + 1)
            else:
                current_node.right = self._insert_rec(current_node.right, courier, depth + 1)

        return current_node

    def find_nearest(self, delivery_lat, delivery_lon):
        """Find the nearest courier to the target location."""

        if self.root is None:
            return None

        return self._find_nearest_rec(
            self.root,
            delivery_lat,
            delivery_lon,
            depth=0,
            best_node=None,
            best_distance=float("inf"),
        )

    def _find_nearest_rec(
        self,
        current_node,
        delivery_lat,
        delivery_lon,
        depth,
        best_node,
        best_distance,
    ):
        if current_node is None:
            return best_node, best_distance

        # Compute the distance from the current node to the target location.
        current_distance = haversine_distance(
            current_node.latitude,
            current_node.longitude,
            delivery_lat,
            delivery_lon,
        )

        # Update the current best candidate.
        if current_distance < best_distance:
            best_distance = current_distance
            best_node = current_node

        # Determine the splitting axis.
        axis = depth % 2

        # Explore the subtree that is more likely to contain the nearest node.
        if axis == 0:
            if delivery_lat < current_node.latitude:
                next_branch = current_node.left
                opposite_branch = current_node.right
            else:
                next_branch = current_node.right
                opposite_branch = current_node.left
        else:
            if delivery_lon < current_node.longitude:
                next_branch = current_node.left
                opposite_branch = current_node.right
            else:
                next_branch = current_node.right
                opposite_branch = current_node.left

        best_node, best_distance = self._find_nearest_rec(
            next_branch,
            delivery_lat,
            delivery_lon,
            depth + 1,
            best_node,
            best_distance,
        )

        # Compute the distance from the target to the splitting boundary.
        if axis == 0:
            boundary_distance = haversine_distance(
                current_node.latitude,
                delivery_lon,
                delivery_lat,
                delivery_lon,
            )
        else:
            boundary_distance = haversine_distance(
                delivery_lat,
                current_node.longitude,
                delivery_lat,
                delivery_lon,
            )

        # Explore the opposite subtree only if it can contain a closer node.
        if boundary_distance < best_distance:
            best_node, best_distance = self._find_nearest_rec(
                opposite_branch,
                delivery_lat,
                delivery_lon,
                depth + 1,
                best_node,
                best_distance,
            )

        return best_node, best_distance