import matplotlib.pyplot as plt
import numpy as np

# Heatmap showing biomass distribution across the forest. Color represents tonnes of biomass per sq metre

biomass_data = np.load("data/biomass.npy") # biomass in kg/m2

# metrics calculation
total_biomass_tonnes = np.nansum(biomass_data) / 1000.0
mean_density_t_ha = total_biomass_tonnes / 25.0

print(f"Total biomass: {total_biomass_tonnes:,.1f} tonnes")
print(f"Mean density: {mean_density_t_ha:,.1f} tonnes/ha")

# convert for visualization (tonnes/ha per pixel)
biomass_t_ha = biomass_data * 10

# adjust vmin and vmax to lock color scale to actual range
vmin = float(np.nanmin(biomass_t_ha))
vmax = float(np.nanmax(biomass_t_ha))

plt.figure(figsize=(10, 8))

# colormap
cmap = 'Greens'

im = plt.imshow(biomass_t_ha, cmap=cmap, vmin=vmin, vmax=vmax)

cbar = plt.colorbar(im)
cbar.set_label("Biomass (tonnes/ha)", fontsize=12)

plt.title(f"Vegetation Biomass Map - Bonang State Forest\nTotal: {total_biomass_tonnes:.0f} tonnes | Mean Density: {mean_density_t_ha:.0f} tonnes/ha", fontsize=14)
plt.xlabel("EAST/WEST (m)")
plt.ylabel("NORTH/SOUTH (m)")

plt.tight_layout()
plt.savefig("biomass_map.png", dpi=300, bbox_inches="tight")
plt.show()
