import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def shockley(V, Is, n):
    Vt = 0.02585
    return Is * (np.exp(V / (n * Vt)) - 1)

df = pd.read_csv('data/1n5404.csv')
v = df['voltage'].values
i = df['current'].values

print(f'Voltage range: {v.min():.3f} to {v.max():.3f}')
print(f'Current range: {i.min():.3f} to {i.max():.3f}')

mask = (v > 0.3) & (v < 0.8) & (i > 0.5)

popt, _ = curve_fit(shockley, v[mask], i[mask]/1000,
                    p0=[1e-6, 1.5],
                    bounds=([1e-12, 1.0], [1e-3, 2.0]),
                    maxfev=10000)

print(f'Is = {popt[0]:.3e} A')
print(f'n  = {popt[1]:.3f}')

v_fit = np.linspace(0, max(v), 300)
i_fit = shockley(v_fit, popt[0], popt[1]) * 1000

plt.figure(figsize=(8,5))
plt.plot(v, i, 'o', ms=3, label='Measured', color='steelblue')
plt.plot(v_fit, i_fit, '-', label=f'Shockley fit (n={popt[1]:.2f})', color='orange')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('1N5404 Diode I-V Characteristic')
plt.ylim(-1, 15)
plt.xlim(0, 1.5)
plt.grid(alpha=0.3)
plt.legend()
plt.show()