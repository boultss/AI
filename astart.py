import heapq

class Graph:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, name, neighbors):
        self.nodes[name] = neighbors
    
    def heuristic(self, node, goal):
        heuristic_values = {
            'A': 10, 'B': 8, 'C': 5, 'D': 7,
            'E': 3, 'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0
        }
        return heuristic_values.get(node, float('inf'))
    
    def a_star(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {node: float('inf') for node in self.nodes}
        g_score[start] = 0
        f_score = {node: float('inf') for node in self.nodes}
        f_score[start] = self.heuristic(start, goal)

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            for neighbor, cost in self.nodes[current].items():
                tentative_g_score = g_score[current] + cost
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None

# Create the graph
graph = Graph()
graph.add_node('A', {'B': 6, 'F': 3})
graph.add_node('B', {'A': 6, 'C': 2, 'D': 5})
graph.add_node('C', {'B': 2, 'D': 3, 'E': 4})
graph.add_node('D', {'B': 5, 'C': 3, 'E': 2, 'I': 4})
graph.add_node('E', {'C': 4, 'D': 2, 'H': 3})
graph.add_node('F', {'A': 3, 'G': 1})
graph.add_node('G', {'F': 1, 'I': 5})
graph.add_node('H', {'E': 3, 'I': 2, 'J': 6})
graph.add_node('I', {'D': 4, 'G': 5, 'H': 2, 'J': 3})
graph.add_node('J', {'H': 6, 'I': 3})

# Run A* Algorithm
start = 'A'
goal = 'J'
path = graph.a_star(start, goal)

# Display the output
if path:
    print(f"Shortest path from {start} to {goal}: {path}")
else:
    print(f"No path found from {start} to {goal}")
