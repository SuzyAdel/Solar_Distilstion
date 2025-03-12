# Solar_Distilstion
# Pyramid Solar Distillation Model

## Overview
This project models a **Pyramid Solar Distillation system** that simulates the evaporation of water using solar energy. The system takes into account **solar radiation**, **salt concentration**, and the **evaporation rate** to simulate the distillation process. The goal is to model how water evaporates, leaving salt behind, and how the distillation process can be optimized through the control of salt concentration.

## Key Features
- **Dual Energy Source**: The model uses **solar radiation** to drive the evaporation process. Solar intensity directly influences the rate of evaporation, and **salt concentration** impacts evaporation efficiency.
  
- **Single-Basin Solar Still**: The system simulates a **single-basin solar still**, where water is evaporated from an open basin, leaving salt behind. The model includes **brine discharge** to control salt concentration and maintain optimal evaporation rates.

- **Evaporation-Controlled Process**: The rate of evaporation follows an equation based on **solar intensity** and **salt concentration**. As the water evaporates, **freshwater** is collected through condensation, while salt is left behind.

- **Brine Discharge**: The model incorporates a mechanism to periodically remove brine to keep salt concentrations in check and optimize the efficiency of the system.

- **Freshwater Collection**: As evaporated water condenses, it is collected as pure **freshwater**, free of salt and impurities.

## Features in Detail
1. **Solar Radiation as the Primary Energy Source**: Solar radiation is the driving factor for evaporation. The model calculates the energy available based on the time of day, weather, and location, determining the rate of evaporation.

2. **Salt Concentration Impact**: The evaporation rate is adjusted based on the salt concentration in the basin. As salt concentration increases, the system slows the evaporation rate to account for the difficulty of evaporating water with high salt content.

3. **Brine Discharge**: To prevent salt buildup in the basin, the system includes a **brine discharge mechanism** that periodically removes saltwater, maintaining the ideal salt concentration for efficient evaporation.

4. **Evaporation-Controlled Process**: The evaporation rate is controlled by an equation that factors in both **solar intensity** and **salt concentration**. This dynamic system ensures that the distillation process adjusts based on varying environmental and operational conditions.

5. **Condensation and Freshwater Collection**: The evaporated water vapor is collected after condensation on a cooler surface, resulting in purified water that is free from salt and impurities.
