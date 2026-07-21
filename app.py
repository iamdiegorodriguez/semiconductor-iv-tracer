import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit

def shockley(V, Is, n):
    Vt = 0.02585
    return Is * (np.exp(V / (n * Vt)) - 1)

# Device list
DEVICES = ['1n4001', '1n5817', '1n5404']

# Streamlit title
st.title('Semiconductor I-V Curve Tracer')

# Device dropdown
device = st.sidebar.selectbox('Select Device', DEVICES)

# Extract v and i from CSVs
df = pd.read_csv(f'data/{device}.csv')
v = df['voltage'].values
i = df['current'].values

if device == '1n5817':
    mask = (v > 0.1) & (v < 0.5) & (i > 0.5)
else:
    mask = (v > 0.3) & (v < 0.75) & (i > 0.5)
    
popt, _ = curve_fit(
    shockley,
    v[mask],
    i[mask] / 1000,
    p0=[1e-9, 1.8],
    bounds=([1e-12, 1.0], [1e-6, 2.0]),
    maxfev=10000,
)

v_fit = np.linspace(0, max(v), 300)
i_fit = shockley(v_fit, popt[0], popt[1]) * 1000

fig = go.Figure()
fig.add_trace(go.Scatter(x=v,y=i, mode='markers', name='Measured'))
fig.add_trace(go.Scatter(x=v_fit, y=i_fit, mode='lines', name='Shockley fit'))
fig.update_layout(xaxis_title='Voltage (V)', yaxis_title='Current (mA)')
st.plotly_chart(fig)

col1, col2, col3 = st.columns(3)
col1.metric('Ideality factor n', f'{popt[1]:.3f}')
col2.metric('Saturation current Is', f'{popt[0]:.2e} A')
vf = v[np.argmax(i > 1.0)] if any(i > 1.0) else 0
col3.metric('Forward voltage Vf', f'{vf:.2f} V')