# Semiconductor Device Characterization Platform

ESP32-based I-V curve tracer that measures semiconductor device characteristics and fits the Shockley diode equation to extract junction parameters.

## What it does
- Sweeps voltage across semiconductor devices using an MCP4725 DAC
- Measures current at each step using an INA219 current sensor
- Streams data to Python over USB serial
- Fits the Shockley diode equation using SciPy to extract ideality factor (n) and saturation current (Is)
- Displays real-time I-V curves in a Streamlit web dashboard

## Devices characterized
| Device | Type | Is | n |
|--------|------|-----|---|
| 1N4001 | Silicon rectifier | 9.54e-10 A | 1.776 |
| 1N5817 | Schottky diode | 6.10e-6 A | 1.498 |
| 1N5404 | Silicon rectifier | 9.52e-9 A | 1.929 |

## Hardware
- ESP32 DevKit v1
- MCP4725 12-bit DAC (I2C)
- INA219 current sensor (I2C)
- 100Ω series resistor
- Assorted diodes

## Software
- Arduino C++ firmware
- Python: pyserial, pandas, numpy, scipy, matplotlib, streamlit, plotly

## How to run
1. Flash firmware to ESP32 via Arduino IDE
2. Activate virtual environment: `.venv\Scripts\Activate.ps1`
3. Collect data: `python collect.py`
4. Analyze: `python analyze.py`
5. Dashboard: `streamlit run app.py`

## concepts demonstrated
- Ohm's Law
- Shockley diode equation
- Semiconductor junction physics
- Band gap theory
- Kirchhoff's Voltage Law