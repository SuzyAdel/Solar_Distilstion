# 🌞 Pyramid Solar Distillation (PSD) System  

![Solar Desalination]([path/to/image1.png](https://github.com/SuzyAdel/Solar_Distilstion/blob/main/Pyramid_Solar_Distillation.sln))  

## 🔹 Overview  
The **Pyramid Solar Distillation (PSD)** system harnesses solar energy to evaporate and condense water, effectively purifying saline or contaminated water. This system is particularly beneficial in arid and remote regions where fresh water is scarce.  

This project simulates the desalination process using computational models that incorporate **solar radiation, salt concentration, evaporation rates, and thermodynamic principles** to optimize fresh water production.  

---

## 🔬 Key Features  
✅ **Simulates 24-hour solar desalination cycle**  
✅ **Accounts for real-world variations in solar radiation**  
✅ **Models evaporation, condensation, and salt concentration changes**  
✅ **Energy balance calculations for efficiency analysis**  
✅ **Comprehensive visualization with plots**  

---

## 📌 How It Works  

The simulation models:  
- **Solar Radiation** 🌞: Uses a sinusoidal model with randomness to mimic real-world fluctuations.  
- **Water & Glass Temperature** 💦🔲: Empirically determined based on solar input and thermal interactions.  
- **Evaporation Rate** 🌡️: Depends on solar intensity, salt concentration, and condensation efficiency.  
- **Salt Concentration** 🧂: Increases over time as water evaporates.  
- **Energy Absorbed & Lost** ⚡: Calculated using thermodynamic principles to determine system efficiency.  

### 📊 Key Equations  
#### 1️⃣ Solar Radiation Model  

 ![image](https://github.com/user-attachments/assets/cba726c7-4df2-4e03-a763-79e7a13d11be)
 where `ε(t) ~ N(0,30)` accounts for random fluctuations.  

#### 2️⃣ Evaporation Rate Model  
![image](https://github.com/user-attachments/assets/e0e857ab-21b5-4ead-874f-f437a7ca5f29)


where `G` is solar radiation, `Cs` is salt concentration, and `ηc` is condensation efficiency.  

More equations and references can be found in the **docs folder**.  

---

## 🚀 Installation & Usage  

### 📦 Requirements  
- Python 3.x  
- NumPy  
- Matplotlib
## Installation
To run the Pyramid Solar Distillation model, you need a Python environment with the following libraries:
- `numpy`
- `matplotlib` (for visualizations, if applicable)

  ###📈 Example Output
  
🔹 Solar Radiation & Water Temperature Over Time

![image](https://github.com/user-attachments/assets/e8f2721f-400c-47b4-95f5-3f20edf60b79)

🔹 Salt Concentration & Cumulative Fresh Water

![image](https://github.com/user-attachments/assets/f5a9002e-93eb-432b-a731-5eb7ea33d96b)

🔹 Energy Absorbed vs. Lost

![image](https://github.com/user-attachments/assets/5c0724a8-fe3c-4578-9839-306cddcfe1a2)

🔹 Evaporation Rate Over Time

![image](https://github.com/user-attachments/assets/4bb977e2-1f16-41d6-aa7f-637122723a74)
![image](https://github.com/user-attachments/assets/5bd5e5f9-18dd-489a-bad4-4d87cc61c277)

🔹 Water Volume Change Over Time

![image](https://github.com/user-attachments/assets/76505ffc-362f-47b7-84f2-9e857b08f5e1)
![image](https://github.com/user-attachments/assets/ce7f3f9b-7a31-49d8-bb69-a0b77a9bac24)

🔹 Glass & Water Temperature Relationship

![image](https://github.com/user-attachments/assets/c1683268-0882-495a-8375-f7a42b312904)

More results and analysis are provided in the generated plots.

📖 References

## 📖 References  
- Kabeel, A.E. (2009). *Performance of solar still with a concave wick evaporation surface.* Renewable Energy, 34(3), 493-498.  
- Dunkle, R. V. (1961). *Solar water distillation: The roof-type still and a multiple effect diffusion still.* International Developments in Heat Transfer, 895–902.  
- Tiwari, G. N., & Sahota, L. (2017). *Advanced Solar Distillation Systems.* Springer.  
- Malik, M. A. S., Tiwari, G. N., Kumar, A., & Sodha, M. S. (1982). *Solar Distillation.* Pergamon Press.  


### ▶️ Running the Simulation  
Clone the repository and run the script:  

```bash
git clone https://github.com/yourusername/solar_distillation.git
cd solar_distillation
python solar_distillation.py

## 🚀 Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/solar-distillation.git
   cd solar-distillation


