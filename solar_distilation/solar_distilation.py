import numpy as np
import matplotlib.pyplot as plt

# Constants
initial_water = 10.0  # Liters of impure water
initial_salt = 0.3  # kg of salt (3% concentration)
solar_intensity_max = 1000  # W/m² (max sunlight at noon)
evaporation_coefficient = 0.0005  # Evaporation factor per unit sunlight (from evaporation theory)
brine_discharge_rate = 0.02  # Liters per hour discharged (rate of brine discharge)
max_salt_concentration = 0.12  # 12% salt, beyond which evaporation stops

# Time settings
hours = np.arange(0, 24, 1)  # 24 hours in a day

# Arrays for tracking variables
water_volume = np.zeros_like(hours, dtype=float)  # Array to store the water volume over time
salt_concentration = np.zeros_like(hours, dtype=float)  # Array to store salt concentration over time
evaporation_rate = np.zeros_like(hours, dtype=float)  # Array to store the evaporation rate over time
brine_discharge = np.zeros_like(hours, dtype=float)  # Array to store the brine discharge over time
temperature = np.zeros_like(hours, dtype=float)  # Array to store the temperature over time
solar_radiation = np.zeros_like(hours, dtype=float)  # Array to store solar radiation over time
fresh_water = np.zeros_like(hours, dtype=float)  # Array to store fresh water collected over time

# Initial conditions
water_volume[0] = initial_water  # Starting water volume in liters
salt_concentration[0] = initial_salt / initial_water  # Initial salt concentration

# Simulate hourly changes
for i in range(1, len(hours)):
    # Solar radiation follows a curve (low at night, high at noon)
    solar_radiation[i] = solar_intensity_max * np.sin(np.pi * i / 24) ** 2  # Solar intensity is sinusoidal

    # Temperature follows solar radiation (in a simple linear manner)
    temperature[i] = 20 + 15 * (solar_radiation[i] / solar_intensity_max)  # Approximate temperature increase with sunlight

    # Evaporation rate depends on sunlight and salt concentration
    if salt_concentration[i - 1] < max_salt_concentration:
        evaporation_rate[i] = evaporation_coefficient * solar_radiation[i] * (1 - salt_concentration[i - 1])  # Higher evaporation if salt concentration is low
    else:
        evaporation_rate[i] = 0  # Stop evaporation at max salt concentration

    # Water loss due to evaporation
    water_lost = evaporation_rate[i]  # Amount of water evaporated in this step

    # Brine discharge to control salt buildup
    brine_discharge[i] = min(brine_discharge_rate, water_volume[i - 1] * 0.1)  # Discharge 10% of current water volume as brine

    # Update water volume and salt concentration
    water_volume[i] = max(water_volume[i - 1] - water_lost - brine_discharge[i], 0)  # Ensure water volume doesn't go negative
    if water_volume[i] > 0:
        salt_concentration[i] = min((salt_concentration[i - 1] * water_volume[i - 1]) / water_volume[i], max_salt_concentration)  # Update salt concentration based on new water volume

    # Fresh water collected (evaporated water)
    fresh_water[i] = fresh_water[i - 1] + water_lost  # Accumulate fresh water from evaporation

# --- Plot 1: Water Volume & Salt Concentration ---
fig, ax1 = plt.subplots()
ax1.plot(hours, water_volume, 'g-', label="Water Volume (L)")
ax1.set_xlabel("Time (hours)")
ax1.set_ylabel("Water Volume (L)", color='g')
ax2 = ax1.twinx()
ax2.plot(hours, salt_concentration * 100, 'b-', label="Salt Concentration (%)")
ax2.set_ylabel("Salt Concentration (%)", color='b')
plt.title("Water Volume & Salt Concentration Over Time")
plt.grid()
plt.show()

# --- Plot 2: Temperature & Solar Radiation ---
fig, ax1 = plt.subplots()
ax1.plot(hours, temperature, 'r-', label="Temperature (°C)")
ax1.set_xlabel("Time (hours)")
ax1.set_ylabel("Temperature (°C)", color='r')
ax2 = ax1.twinx()
ax2.plot(hours, solar_radiation, 'y-', label="Solar Radiation (W/m²)")
ax2.set_ylabel("Solar Radiation (W/m²)", color='y')
plt.title("Temperature & Solar Radiation Over Time")
plt.grid()
plt.show()

# --- Plot 3: Evaporation Rate ---
fig, ax1 = plt.subplots()
ax1.bar(hours, evaporation_rate, color='orange', label="Evaporation Rate (L/hr)")
ax1.set_xlabel("Time (hours)")
ax1.set_ylabel("Evaporation Rate (L/hr)", color='orange')
plt.title("Evaporation Rate Over Time")
plt.grid()
plt.show()

# --- Combined Plot: Fresh Water Collected & Remaining Water ---
remaining_water = initial_water - fresh_water  # Calculate remaining water
plt.figure()
plt.plot(hours, fresh_water, 'c-', label="Fresh Water Collected (L)")
plt.plot(hours, remaining_water, 'b-', label=" Saline Water (L)")
plt.xlabel("Time (hours)")
plt.ylabel("Water (L)")
plt.title("Fresh Water Collected & Remaining Water Over Time")
plt.legend()
plt.grid()
plt.show()
