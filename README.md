# Semiconductor Device Characterization Platform

ESP32-based I-V curve tracer that measures semiconductor device characteristics and fits the Shockley diode equation to extract junction parameters.

## What it does
- Sweeps voltage across semiconductor devices using an MCP4725 DAC
- Measures current at each step using an INA219 current sensor
- Streams data to Python over USB serial
- Fits the Shockley diode equation using SciPy to extract ideality factor (n) and saturation current (Is)
- Displays measured I-V curves in an interactive Streamlit dashboard

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

- Main firmware:firmware/semiconductor_iv_tracer/semiconductor_iv_tracer.ino
- I2C scanner: firmware/tools/i2c_scanner/i2c_scanner.ino


## How to run
1. Install dependencies: pip install -r requirements.txt
2. Flash firmware to ESP32 via Arduino IDE
3. Collect data: `python collect.py`
4. Analyze: `python analyze.py`
5. Dashboard: `streamlit run app.py`

## concepts demonstrated
- Embedded firmware development
- Hardware-software integration
- I2C and UART communication
- Sensor interfacing
- Ohm’s law
- Kirchhoff’s voltage law
- Shockley diode equation
- Semiconductor junction physics
- Nonlinear curve fitting
- Engineering data visualization

## Hardware
![Circuit](images/circuit.jpg)

## Dashboard
![Dashboard](images/dashboard.png)
