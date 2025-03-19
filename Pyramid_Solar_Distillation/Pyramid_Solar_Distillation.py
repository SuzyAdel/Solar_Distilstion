import numpy as np
import matplotlib.pyplot as plt
import math

# ---------------------- Constants & Parameters ----------------------
# Geometry (Square-based pyramid distiller)
base_length = 1.0  # meters
water_depth = 0.05  # meters
glass_incline_angle_deg = 30  # degrees
glass_incline_angle_rad = math.radians(glass_incline_angle_deg)

# Material and Environmental Properties
C_air = 1005  # J/kg.K (air specific heat)
sigma = 5.67e-8  # Stefan-Boltzmann constant
R = 8.314  # universal gas constant (J/mol·K)
M_water = 18.01528  # g/mol

# Antoine equation constants for water
A = 8.07131
B = 1730.63
C = 233.426

# Salt concentration influence factor (example reduction factor)
salt_concentration_factor = 0.98  # decreases vapor pressure by ~2%

# Condensation efficiency factor
condensation_efficiency = 0.85

# Water properties
water_density = 997  # kg/m³

# Solar parameters
I_max = 1000  # W/m² (peak irradiance)

# Time array for 24 hours (hourly steps)
time_hours = np.arange(0, 24, 1)

# ---------------------- Geometry Calculations ----------------------
# Slant height of the glass faces
slant_height = (base_length / 2) / math.cos(glass_incline_angle_rad)

# Glass area (4 triangular faces)
glass_area = 4 * (0.5 * base_length * slant_height)

# Base area
base_area = base_length ** 2

# Water surface area inside (approx equal to base area for shallow water)
water_surface_area = base_area

# ---------------------- Functions ----------------------
def solar_irradiance(hour):
    # Simulating irradiance using cosine shape (peak at noon, zero at night)
    solar_constant = I_max * max(np.cos((hour - 12) * (np.pi / 12)), 0)
    return solar_constant

def vapor_pressure_water(temp_c):
    # Antoine equation for water vapor pressure in mmHg
    vp_mmHg = 10 ** (A - (B / (temp_c + C)))
    # Convert mmHg to Pascal (1 mmHg = 133.322 Pa)
    vp_Pa = vp_mmHg * 133.322
    return vp_Pa

def evaporation_rate(irradiance, temp_water, salt_factor):
    # Basic empirical formula: Evaporation proportional to irradiance & vapor pressure difference
    vapor_pressure = vapor_pressure_water(temp_water) * salt_factor
    # Simplified form: rate (kg/s) = efficiency * irradiance * glass_area * factor
    # Reference factor chosen to scale results (~ realistic scale)
    factor = 1e-5
    return irradiance * glass_area * factor * (vapor_pressure / 1e5) * condensation_efficiency

# ---------------------- Simulation ----------------------
water_temp_c = 60  # assumed constant, can later vary with time
salt_concentration = 0.035  # 3.5% average seawater

results_irradiance = []
results_evaporation_kg_per_hour = []

for hour in time_hours:
    irr = solar_irradiance(hour)
    results_irradiance.append(irr)

    evap_rate_kg_s = evaporation_rate(irr, water_temp_c, salt_concentration_factor)
    evap_kg_hour = evap_rate_kg_s * 3600

    results_evaporation_kg_per_hour.append(evap_kg_hour)

# ---------------------- Results ----------------------

# Convert evaporated mass into liters (1L ~ 1kg for water)
fresh_water_liters_per_hour = results_evaporation_kg_per_hour

plt.figure(figsize=(12, 6))
plt.plot(time_hours, results_irradiance, label='Solar Irradiance (W/m²)', color='orange')
plt.ylabel('Solar Irradiance (W/m²)')
plt.xlabel('Time (hours)')
plt.title('Solar Irradiance over 24 Hours')
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(time_hours, fresh_water_liters_per_hour, label='Fresh Water Output (Liters/hour)', color='blue')
plt.ylabel('Fresh Water Output (L/h)')
plt.xlabel('Time (hours)')
plt.title('Distilled Fresh Water Production over 24 Hours')
plt.grid()
plt.show()

# Total daily output
print(f"Total fresh water produced in 24 hours: {sum(fresh_water_liters_per_hour):.2f} liters")

# ---------------------- Validation ----------------------
# Print sample values to validate understanding
for hour, irr, evap in zip(time_hours, results_irradiance, fresh_water_liters_per_hour):
    print(f"Hour {hour}: Irradiance = {irr:.2f} W/m², Fresh Water = {evap:.4f} L")

