from itertools import permutations

# Function to calculate total distance of a given path
def calculate_distance(graph, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    total_distance += graph[path[-1]][path[0]]  # Returning to the starting city
    return total_distance

# Function to find the shortest path using brute-force approach
def traveling_salesman(graph, start=0):
    num_cities = len(graph)
    cities = list(range(num_cities))
    cities.remove(start)  # Removing the starting city from permutations

    min_path = None
    min_distance = float("inf")

    for perm in permutations(cities):
        path = [start] + list(perm)  # Adding start city at the beginning
        distance = calculate_distance(graph, path)
        
        if distance < min_distance:
            min_distance = distance
            min_path = path

    return min_path, min_distance

# Example graph represented as an adjacency matrix
graph = [
    [0, 10, 15, 20],  # Distances from city 0
    [10, 0, 35, 25],  # Distances from city 1
    [15, 35, 0, 30],  # Distances from city 2
    [20, 25, 30, 0]   # Distances from city 3
]

# Running the TSP solver
start_city = 0  # Starting city index
best_path, best_distance = traveling_salesman(graph, start=start_city)

# Displaying the result
print(f"Best route: {best_path} with total distance: {best_distance}")
