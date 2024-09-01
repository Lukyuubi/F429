import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Carregar os dados dos três CSVs
df_resistor470 = pd.read_csv('R470_dados.csv')
df_resistor2 = pd.read_csv('R1K_dados.csv')
df_resistor3 = pd.read_csv('R2.2K_dados.csv')
df_resistor4 = pd.read_csv('R4.7K_dados.csv')

# Frequência (Hz)
frequency_resistor = df_resistor470['frequency (Hz)'].values
frequency_resistor2 = df_resistor2['frequency (Hz)'].values
frequency_resistor3 = df_resistor3['frequency (Hz)'].values
frequency_resistor4 = df_resistor4['frequency (Hz)'].values

# Tensão medida nos canais (Vpp1 e Vpp2)
Vpp1_resistor = df_resistor470['Vpp1 (V)'].values  
Vpp2_resistor = df_resistor470['Vpp2 (V)'].values

Vpp1_resistor2 = df_resistor2['Vpp1 (V)'].values  
Vpp2_resistor2 = df_resistor2['Vpp2 (V)'].values  

Vpp1_resistor3 = df_resistor3['Vpp1 (V)'].values  
Vpp2_resistor3 = df_resistor3['Vpp2 (V)'].values  

Vpp2_resistor4 = df_resistor4['Vpp2 (V)'].values  
Vpp1_resistor4 = df_resistor4['Vpp1 (V)'].values  # Tensão de entrada no capacitor

# Cálculo da resposta espectral para cada componente
# Configuração a) Queda de tensão no resistor
T_R1 = Vpp2_resistor / Vpp1_resistor  # Transmissão
T_R_dB = 20 * np.log10(np.abs(T_R1))

# Configuração b) Queda de tensão no resistor config2
T_R2 = Vpp2_resistor2 / Vpp1_resistor2  # Transmissão
T_R2_db = 20 * np.log10(np.abs(T_R2))

# Configuração c) Queda de tensão no resist config3
T_R3 = Vpp2_resistor3 / Vpp1_resistor3  # Transmissão
T_R3_db = 20 * np.log10(np.abs(T_R3))

# Configuração d) Queda de tensão no resistor config4
T_R4 = Vpp2_resistor4 / Vpp1_resistor4  # Transmissão
T_R4_db = 20 * np.log10(np.abs(T_R4))

# Plotar a resposta espectral para as três configurações
plt.figure(figsize=(10, 6))

plt.plot(frequency_resistor, T_R_dB, 'bo', label='Queda de tensão no Resistor (R) config 470')
plt.plot(frequency_resistor2, T_R2_db, 'yo', label='Queda de tensão no Resistor (R) config2')
plt.plot(frequency_resistor3, T_R3_db, 'ro', label='Queda de tensão no Resistor (R) config3')
plt.plot(frequency_resistor4, T_R4_db, 'go', label='Queda de tensão no Resistor (R) config4')

plt.xscale('log')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Transmissão (dB)')
plt.title('Resposta Espectral do Circuito RLC em Diferentes Configurações')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig("parte2.1.png")
