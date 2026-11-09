import numpy as np
from scipy.stats import binned_statistic_2d

points = np.load("data/veg_normalized.npy")

x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

# 1 metre pixel resolution
pixel_res = 1.0

# spatial boundaries 
x_min, x_max = np.min(x), np.max(x)
y_min, y_max = np.min(y), np.max(y)

# calculate exact bin edges spaced by resolution
# adding resolution to upperlimit ensures the furthest points are caught
x_edges = np.arange(x_min, x_max + pixel_res, pixel_res)
y_edges = np.arange(y_min, y_max + pixel_res, pixel_res)

# compute 2d grid statistic (Max z value per 1m x 1m cell)
# statistic='max' to retrieve the peak vegetation height per grid
grid_z, x_edges, y_edges, binnumber = binned_statistic_2d(
    x=x,
    y=y,
    values=z,
    statistic='max',
    bins=[x_edges, y_edges] # type: ignore
)

# binned_statistic_2d returns a matrix where rows correspond to X bins 
# and columns correspond to Y bins. Transpose it for standard matrix rendering (Y=rows, X=cols)
grid_z = grid_z.T

# Handle empty cells (gaps with no vegetation points)
# By default, cells with no points will contain np.nan when computing 'max'.
# We can find these NaN values and assign them a baseline ground height (e.g., 0.0)
empty_mask = np.isnan(grid_z)
grid_z_cleaned = np.nan_to_num(grid_z, nan=0.0)

print(f"Generated Grid Shape: {grid_z_cleaned.shape}")
print(f"Total Grid Cells: {grid_z_cleaned.size}")
print(f"Handled/Filled Gaps: {np.sum(empty_mask)} empty pixels set to 0.0m")
print(f"Max Height in CHM: {np.max(grid_z_cleaned):.2f} m")
print(f"Mean Height in CHM: {np.mean(grid_z_cleaned):.2f} m")

np.save("data/chm.npy", grid_z_cleaned)
