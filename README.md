# 🔥 Pulsejet Calculator

**Pulsejet Calculator** is a lightweight desktop tool that helps you estimate the key dimensions and performance parameters of a pulsejet engine.  
It’s designed for experimenters, hobbyists, and aviation enthusiasts who want to explore how design variables — like exhaust radius — affect thrust, resonance, and geometry.

---

## ✈️ Overview

This calculator applies the empirical relationships described by **Fredrik Westberg (Inside the Pulsejet Engine, 2000)** and **Paul Schmidt**, the pioneer of pulsejet theory.

By entering the exhaust pipe radius, the program automatically computes:

- **Exhaust Pipe Area (EPA)**
- **Valve Flow Area (VFA)**
- **Recommended Tube Length**
- **Estimated Thrust Output**
- **Predicted Resonance Frequency**

These formulas are based on real-world experimental data and are intended for **educational and conceptual use**.

---

## 🧮 Example Calculation

If you enter a radius of `25 mm`, the calculator will output:

| Parameter | Result | Units |
|-----------|--------|-------|
| Exhaust Pipe Area | 1963.50 | mm² |
| Valve Flow Area | 966.10 | mm² |
| Tube Length | 768.4 | mm |
| Estimated Thrust | 5.78 | kgf |
| Resonance Frequency | 195.3 | Hz |

---

## 💻 Features

- Built with **Python + Tkinter**
- Modern dark interface with hover effects
- Real-time validation and formatted results
- Based entirely on classic **pulsejet theory equations**
- Modular structure for future expansion (fuel type, temperature, pressure, etc.)

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/lain77/pulsejet-calculator.git
cd pulsejet-calculator
```

---

## 🧠 Theory References

- Fredrik Westberg — *Inside the Pulsejet Engine* (2000)  
- Paul Schmidt — German pulsejet theory and Argus As-014 development  
- Dave Brill — empirical relations and design validation

---

## 🚀 Future Plans

- Add graph-based visualizations (tube geometry preview)  
- Support for temperature-based speed of sound adjustment  
- Thrust vs. frequency plotting  
- Save/Export feature for test data  

---

## 🧑‍💻 Author

**Victor Samuel**  
Aviation enthusiast • Software developer • Pulsejet experimenter  
📍 Brazil  

💬 “If it breathes, explodes, and roars — I want to understand it.”

---

## ⚠️ Disclaimer

This software is for theoretical and educational purposes only.  
Do not use these calculations for real-world construction without proper safety knowledge, testing environment, and engineering supervision.

© 2025 Pulsejet Tools — All rights reserved.
