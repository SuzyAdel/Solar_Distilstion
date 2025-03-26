import numpy as np
import matplotlib.pyplot as plt

# --- Constants and Physical Parameters ---
# Stefan-Boltzmann constant for radiation calculations (W/m²·K⁴)
sigma = 5.67e-8
# Latent heat of vaporization of water (J/kg)
latent_heat_vaporization = 2260e3
# Density of water (kg/m³)
density_water = 1000
# Specific heat capacity of water (J/kg·K)
heat_capacity_water = 4186
# Initial saline water volume (liters)
initial_water_volume = 10
# Initial salt concentration (g/L), typical seawater
initial_salt_concentration = 35
# Surface area of pyramid solar still cover (m²)
surface_area = 1.5
# Emissivity of the glass cover
glass_emissivity = 0.85

# --- Time Array (24 hours simulation) ---
time_hours = np.arange(0, 24, 1)

# --- Solar Radiation Simulation (W/m²) ---
# Using sinusoidal solar pattern + randomness for realism
np.random.seed(42)
solar_radiation = (
    500
    + 400 * np.maximum(np.sin(np.pi * time_hours / 24), 0)
    + np.random.normal(0, 30, size=len(time_hours))
)

# --- Water & Glass Temperature Simulation (°C) ---
water_temp = 20 + (solar_radiation / 100) + np.random.normal(0, 0.5, size=len(time_hours))
glass_temp = water_temp - 2 + np.random.normal(0, 0.3, size=len(time_hours))

# --- Condensation Efficiency Calculation ---
# Modeled using logistic function: increases with glass temp
cond_efficiency = 90 / (1 + np.exp(-(glass_temp - 25) / 2)) + np.random.normal(0, 2, size=len(time_hours))
cond_efficiency = np.clip(cond_efficiency, 70, 95)  # Realistic bounds

# --- Evaporation and Salt Concentration Tracking ---
salt_concentration = [initial_salt_concentration]
evaporation_rate = []
cumulative_fresh_water = [0]
remaining_saline_water = [initial_water_volume]

# --- Evaporation Calculation Per Hour ---
# Evaporation rate influenced by solar radiation, salt concentration, and condensation efficiency
for t in range(len(time_hours)):
    current_salt = salt_concentration[-1]
    evap_rate = (
        (0.0003 * solar_radiation[t])  # Proportional to solar input
        * (1 - (current_salt / 300))   # Salt reduces evaporation
        * cond_efficiency[t] / 100     # Condensation effectiveness
    )
    # Add slight random variation
    evap_rate += np.random.normal(0, evap_rate * 0.05)
    evap_rate = max(evap_rate, 0)  # Prevent negative rates
    evaporation_rate.append(evap_rate)

    # Update system state
    new_volume = remaining_saline_water[-1] - evap_rate
    new_volume = max(new_volume, 0)
    remaining_saline_water.append(new_volume)
    cumulative_fresh_water.append(cumulative_fresh_water[-1] + evap_rate)
    
    if new_volume > 0:
        salt_concentration.append((current_salt * remaining_saline_water[-2]) / new_volume)
    else:
        salt_concentration.append(current_salt)

instantaneous_fw = evaporation_rate  # Instantaneous fresh water each hour

# --- Energy Absorption & Loss Calculation ---
energy_absorbed = solar_radiation * surface_area * (1 - glass_emissivity)
energy_lost = energy_absorbed * (0.2 + np.random.normal(0, 0.02, size=len(time_hours)))

# =================== RESULTS OUTPUT =================== #
total_fresh_water = cumulative_fresh_water[-1]
peak_hour = np.argmax(instantaneous_fw)
peak_fw = instantaneous_fw[peak_hour]

print("===== Simulation Summary =====")
print(f"Total fresh water collected in 24 hours: {total_fresh_water:.2f} liters")
print(f"Maximum fresh water production occurs at hour: {peak_hour}h")
print(f"Fresh water produced during peak hour: {peak_fw:.3f} liters")
print("\nInterpretation:")
print(f"- Freshwater production peaks typically between midday and early afternoon (around hour {peak_hour}),")
print("  corresponding to maximum solar radiation and higher water/glass temperature difference.")
print(f"- The system efficiency is well correlated with solar intensity and condensation conditions.\n")

# ===================== PLOTS ===================== #
# (All your plots as you had them)

# 1) Solar Radiation & Water Temperature
plt.figure(figsize=(10, 5))
plt.title('Solar Radiation & Water Temperature Over Time')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(time_hours, solar_radiation, label='Solar Radiation (W/m²)', color='orange')
ax2.plot(time_hours, water_temp, label='Water Temp (°C)', color='blue')
ax1.set_ylabel('Solar Radiation (W/m²)')
ax2.set_ylabel('Water Temperature (°C)')
ax1.set_xlabel('Time (hours)')
ax1.grid()
plt.xticks(time_hours)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()

# 2) Salt concentration & cumulative fresh water
fig, ax1 = plt.subplots(figsize=(10, 5))
plt.title('Salt Concentration & Cumulative Fresh Water Over Time')
ax2 = ax1.twinx()
ax1.plot(time_hours, salt_concentration[:-1], color='brown', label='Salt Concentration (g/L)')
ax2.plot(time_hours, cumulative_fresh_water[:-1], color='green', label='Cumulative Fresh Water (L)')
ax1.set_xlabel('Time (hours)')
ax1.set_ylabel('Salt Concentration (g/L)', color='brown')
ax2.set_ylabel('Cumulative Fresh Water (L)', color='green')
ax1.grid()
plt.xticks(time_hours)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()

# 3) Cumulative FW, remaining saline water, initial water + instantaneous FW
plt.figure(figsize=(10, 5))
plt.title('Water Collection and Volumes Over Time')
plt.plot(time_hours, cumulative_fresh_water[:-1], label='Cumulative FW (L)', color='green')
plt.plot(time_hours, remaining_saline_water[:-1], label='Remaining Saline Water (L)', color='red')
plt.plot(time_hours, [initial_water_volume]*len(time_hours), '--', color='black', label='Initial Water Volume (L)')
plt.bar(time_hours, instantaneous_fw, label='Instantaneous FW (L/h)', color='purple', alpha=0.5)
plt.xlabel('Time (hours)')
plt.grid()
plt.xticks(time_hours)
plt.legend()
plt.show()

# 4) Instantaneous fresh water collected per hour
plt.figure(figsize=(10, 5))
plt.title('Instantaneous Fresh Water Collected Per Hour')
plt.bar(time_hours, instantaneous_fw, color='skyblue')
plt.xlabel('Time (hours)')
plt.ylabel('Liters per Hour')
plt.grid()
plt.xticks(time_hours)
plt.show()

# 5) Evaporation rate & salt concentration
fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.set_xlabel('Time (hours)')
ax1.set_ylabel('Evaporation Rate (L/h)', color='blue')
ax1.plot(time_hours, evaporation_rate, color='blue', label='Evaporation Rate (L/h)')
ax2 = ax1.twinx()
ax2.set_ylabel('Salt Concentration (g/L)', color='brown')
ax2.plot(time_hours, salt_concentration[:-1], color='brown', linestyle='dashed', label='Salt Concentration (g/L)')
plt.title('Evaporation Rate & Salt Concentration Over Time')
ax1.grid()
plt.xticks(time_hours)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()

# 6) Evaporation rate & solar radiation
fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.set_xlabel('Time (hours)')
ax1.set_ylabel('Evaporation Rate (L/h)', color='blue')
ax1.plot(time_hours, evaporation_rate, color='blue', label='Evaporation Rate (L/h)')
ax2 = ax1.twinx()
ax2.set_ylabel('Solar Radiation (W/m²)', color='orange')
ax2.plot(time_hours, solar_radiation, color='orange', linestyle='dashed', label='Solar Radiation (W/m²)')
plt.title('Evaporation Rate & Solar Radiation Over Time')
ax1.grid()
plt.xticks(time_hours)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()

# 7) Energy absorbed & lost
fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.set_xlabel('Time (hours)')
ax1.set_ylabel('Energy Absorbed (J)', color='green')
ax1.plot(time_hours, energy_absorbed, color='green', label='Energy Absorbed')
ax2 = ax1.twinx()
ax2.set_ylabel('Energy Lost (J)', color='red')
ax2.plot(time_hours, energy_lost, color='red', linestyle='dashed', label='Energy Lost')
plt.title('Energy Absorbed & Lost Over Time')
ax1.grid()
plt.xticks(time_hours)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()

# 8) Glass temperature & water temperature
plt.figure(figsize=(10, 5))
plt.title('Glass & Water Temperature Over Time')
plt.plot(time_hours, water_temp, color='blue', label='Water Temperature (°C)', linestyle='solid')
plt.plot(time_hours, glass_temp, color='purple', label='Glass Temperature (°C)', linestyle='dotted')
plt.xlabel('Time (hours)')
plt.grid()
plt.xticks(time_hours)
plt.legend()
plt.show()
