import math

def orientation(p, q, r):
    """Return the orientation of the triplet (p, q, r).
       0 -> collinear; >0 -> counterclockwise; <0 -> clockwise."""
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def distance_sq(p, q):
    """Return the squared Euclidean distance between points p and q."""
    return (p[0] - q[0])**2 + (p[1] - q[1])**2

def convex_hull(points):
    # Find the point with the lowest y (and lowest x in case of tie)
    start = min(points, key=lambda p: (p[1], p[0]))

    # Sort points by polar angle and distance from start
    sorted_points = sorted(points, key=lambda p: (
        math.atan2(p[1] - start[1], p[0] - start[0]),
        distance_sq(start, p)
    ))

    hull = []
    for p in sorted_points:
        # Remove points that make a clockwise turn
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    return hull

# Example points
points = [(0, 3), (1, 1), (2, 2), (4, 4),
          (0, 0), (1, 2), (3, 1), (3, 3)]

hull = convex_hull(points)
print("Convex Hull Points (in order):", hull)


def is_point_in_polygon(point, polygon):
    """Determine if a point (x, y) lies inside a polygon defined by a list of vertices."""
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]

        # Check if the point's y is between the y's of the edge
        if min(p1y, p2y) < y <= max(p1y, p2y):
            # Check if x is to the left of the edge (ray-casting)
            if p1y != p2y:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
            else:
                xinters = p1x

            if x <= xinters:
                inside = not inside

        p1x, p1y = p2x, p2y

    return inside

# Example polygon (a square) and test points
polygon = [(1, 1), (5, 1), (5, 5), (1, 5)]
test_points = [(3, 3), (6, 3), (5, 5), (0, 0)]

for pt in test_points:
    result = is_point_in_polygon(pt, polygon)
    print(f"Point {pt} inside polygon: {result}")


class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level      # Level in the decision tree (index of item being considered)
        self.profit = profit    # Total profit accumulated
        self.weight = weight    # Total weight accumulated
        self.bound = bound      # Upper bound on maximum profit achievable from this node

def bound(node, n, capacity, items):
    """Compute the upper bound on the maximum profit in the subproblem defined by this node."""
    if node.weight >= capacity:
        return 0
    profit_bound = node.profit
    j = node.level + 1
    totweight = node.weight

    # Take items in order while under the capacity
    while j < n and totweight + items[j][0] <= capacity:
        totweight += items[j][0]
        profit_bound += items[j][1]
        j += 1

    # If there is still capacity, take fraction of the next item
    if j < n:
        profit_bound += (capacity - totweight) * items[j][1] / items[j][0]
    return profit_bound

def knapsack_branch_and_bound(capacity, items):
    """Solve the 0/1 knapsack problem using branch and bound.
       items: list of tuples (weight, profit). Items are sorted by profit/weight ratio descending."""

    # Sort items by profit/weight ratio descending
    items = sorted(items, key=lambda x: x[1]/x[0], reverse=True)
    n = len(items)
    max_profit = 0
    queue = []

    # Start with a dummy node at level -1.
    v = Node(level=-1, profit=0, weight=0, bound=0)
    v.bound = bound(v, n, capacity, items)
    queue.append(v)

    while queue:
        v = queue.pop(0)  # Pop the first node (BFS style)
        if v.level == n - 1 or v.bound <= max_profit:
            continue

        # Next level (consider the next item)
        u_level = v.level + 1

        # Case 1: Include the next item if possible
        u = Node(level=u_level,
                 profit=v.profit + items[u_level][1],
                 weight=v.weight + items[u_level][0],
                 bound=0)

        if u.weight <= capacity and u.profit > max_profit:
            max_profit = u.profit

        u.bound = bound(u, n, capacity, items)
        if u.bound > max_profit:
            queue.append(u)

        # Case 2: Exclude the next item
        u2 = Node(level=u_level,
                  profit=v.profit,
                  weight=v.weight,
                  bound=0)

        u2.bound = bound(u2, n, capacity, items)
        if u2.bound > max_profit:
            queue.append(u2)

    return max_profit

# Define items as (weight, profit)
items = [(2, 40), (3, 50), (5, 100), (1, 20)]
capacity = 5
result = knapsack_branch_and_bound(capacity, items)
print("Maximum profit for the knapsack problem:", result)
