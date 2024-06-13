import random

# Define the number of points to generate
num_points = 100000

# Initialize the starting value
current_value = 5

# Calculate the incremental step size
step_size = (15 - 5) / num_points

# Generate random points incrementally
data = []
for _ in range(num_points):
    current_value += random.uniform(0, step_size)
    data.append(current_value)

# Print the first 10 points as an example
print(data[:10])
