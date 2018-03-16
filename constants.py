import numpy as np

# Note: This program follows the MKS system (meters, kg, and seconds are defined as 1)

meters = 1
centimeters = 1e-2 * meters
millimeters = 1e-3 * meters
micrometers = 1e-6 * meters
feet = 2.54 * centimeters

seconds = 1

hertz = 1 / seconds
kilohertz = 1e3 * hertz
megahertz = 1e6 * hertz
gigahertz = 1e9 * hertz

# Constants
c0 = 299792458 * meters / seconds  # Speed of light in free space
u0 = 4 * np.pi * 1e-7 * 1 / meters  # Permeability of free space
e0 = 1 / (c0 ** 2 * u0) * 1 / meters  # Permittivity of free space

# Relative Permittivities (room temp, under 1 kHz
er_Silicon = 11.68
er_SiliconDioxide = 3.9
er_Air = 1.00059