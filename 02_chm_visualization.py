import numpy as np
import matplotlib.pyplot as plt

data = np.load("data/chm.npy")

plt.imshow(data, cmap='viridis', aspect='equal', vmin=0, vmax=60)
plt.colorbar(label="Height (m)")
plt.xlabel("EAST/WEST(m)")
plt.ylabel("NORTH/SOUTH(m)")
plt.title(f"Canopy Height Model - Bonang State Forest\nMax: {np.max(data):.1f}m | Mean: {np.mean(data):.1f}m | Plot: 25 hectares")

plt.savefig("chm.png", dpi=300, bbox_inches="tight")
plt.show()


