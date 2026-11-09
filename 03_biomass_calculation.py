# Application of an allometric equation to convert every pixel in the CHM from height in meters to biomass in kg per square meter.
# Biomass (kg/m²) = a * (Height)^b

# a and b are species specific constants

# generalized eucalypt model yielding per-pixel weight

import numpy as np

chm = np.load("data/chm.npy")

# allometric constants
# modify a and b based on target species or study area
a = 0.05
b = 2.1

# replace negatives with 0
chm_clean = np.maximum(chm, 0)

# apply allometric equation across every pixel
biomass_pixels = a * (chm_clean ** b)

# calculate total biomass in kg
total_biomass_kg = np.sum(biomass_pixels)

# convert kg to tonnes
total_biomass_tonnes = total_biomass_kg / 1000.0

# calculate biomass density in tonnes per hectare
plot_area_ha = 25.0
biomass_density_per_ha = total_biomass_tonnes / plot_area_ha

print(f"Total Plot Biomass: {total_biomass_tonnes:,.2f} tonnes")
print(f"Biomass Density:    {biomass_density_per_ha:,.2f} tonnes/ha")

np.save("data/biomass.npy", biomass_pixels)

""" Important info 
When using remote sensing (like airborne LiDAR) over south-eastern Australian eucalypt forests, 
researchers often fit a power-law equation (AGB = a * H^b) where H is the pixel canopy 
height or mean canopy height, and the output is Above-Ground Biomass (AGB)
"""
