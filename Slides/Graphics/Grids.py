import matplotlib.pyplot as plt
import numpy as np

# Set up the figure
fig, ax = plt.subplots(figsize=(6,6))

# Define the range for the grid
grid_min, grid_max, step = -5, 5, 1
x_range = np.arange(grid_min, grid_max+step, step)
y_range = np.arange(grid_min, grid_max+step, step)

# Plot the base grid (aligned with the axes)
for x in x_range:
    ax.plot([x, x], [grid_min, grid_max], color='gray', lw=1)
for y in y_range:
    ax.plot([grid_min, grid_max], [y, y], color='gray', lw=1)

# Define rotation parameters
angle_deg = 5  # rotation angle in degrees
angle_rad = np.deg2rad(angle_deg)
rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
                            [np.sin(angle_rad),  np.cos(angle_rad)]])

# Plot the rotated grid
# Vertical lines for rotated grid:
for x in x_range:
    # Create points along a vertical line at x (original grid)
    ys = np.linspace(grid_min, grid_max, 100)
    pts = np.column_stack((np.full_like(ys, x), ys))
    # Rotate these points
    pts_rot = pts @ rotation_matrix.T
    ax.plot(pts_rot[:,0], pts_rot[:,1], color='blue', lw=1)

# Horizontal lines for rotated grid:
for y in y_range:
    xs = np.linspace(grid_min, grid_max, 100)
    pts = np.column_stack((xs, np.full_like(xs, y)))
    pts_rot = pts @ rotation_matrix.T
    ax.plot(pts_rot[:,0], pts_rot[:,1], color='blue', lw=1)

# Set equal aspect and limits
ax.set_aspect('equal')
ax.set_xlim(grid_min-1, grid_max+1)
ax.set_ylim(grid_min-1, grid_max+1)
ax.axis('off')
plt.tight_layout()
plt.show()
