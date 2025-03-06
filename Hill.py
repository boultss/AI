import random

def hill_climbing(func, x_start, step_size=0.1, max_iterations=1000):
    """
    Implements the Hill Climbing algorithm to maximize a function.
    
    Parameters:
    - func: The function to optimize.
    - x_start: The initial random starting point.
    - step_size: The step size for moving towards a better solution.
    - max_iterations: The maximum number of iterations allowed.
    
    Returns:
    - best_x: The x value that gives the maximum function output.
    - best_value: The maximum function value.
    """
    x = x_start  # Start at a random point
    for _ in range(max_iterations):
        neighbors = [x - step_size, x + step_size]  # Generate neighbors
        best_neighbor = max(neighbors, key=func)  # Choose the best neighbor
        
        if func(best_neighbor) <= func(x):  # Stop if no improvement
            break
        
        x = best_neighbor  # Move to the best neighbor
    return x, func(x)

# Define the objective function f(x) = -x² + 4x
def objective_function(x):
    return -x**2 + 4*x

# Generate a random starting point between 0 and 5
x_start = random.uniform(0, 5)

# Run Hill Climbing
best_x, best_value = hill_climbing(objective_function, x_start)

# Print the results
print("===== Hill Climbing Optimization =====")
print(f"Starting Point: {x_start:.4f}")
print(f"Best x Found: {best_x:.4f}")
print(f"Maximum Value of f(x): {best_value:.4f}")
print("=====================================")
