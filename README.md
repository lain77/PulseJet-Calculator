![Pulsejet Diagram]([https://pulsejet-sim.com/static/images/5.%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE-Photoroom.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgUGWX2FH_c8_OHwNmCmaVVbq9iKeoqycmZe9LfVm0NTZ8JQNM2WVIY4_Sh2Ux0FBV8UWPvGGgWg_i18R_o7sNxBeHepVqXUL3k9Rv_RMOZVFqZ26-9cQd-m9A93LwYbRC4Hl6-MH5EZW5ne7vMSAHNliEdSZDODAttss78kX7gJAAiMEUpoPr2HilTkXmq/s550/GIF%2012%EC%9B%94%2018%EC%9D%BC%20%EC%9B%94%EC%9A%94%EC%9D%BC%20%EC%98%A4%ED%9B%84%209-20-23.gif))

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
