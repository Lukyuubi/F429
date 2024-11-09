import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def calcular_transmitancia(csv_file):
    # Ler o CSV
    df = pd.read_csv(csv_file)
    
    # Assumindo que as colunas sejam 'Frequência', 'Tensão_Entrada' e 'Tensão_Saída'
    frequencia = df['frequency (Hz)']
    tensao_entrada = df['Vpp1 (V)']
    tensao_saida = df['Vpp2 (V)']
    
    # Calcular a transmitância em dB
    transmitancia_dB = 20 * np.log10(tensao_saida / tensao_entrada)
    
    return frequencia, transmitancia_dB

# Lista de arquivos CSV
arquivos_csv = ['C220n_R1k_dados.csv', 'C220n_R4.7K_dados.csv', 'C220n_R470_dados.csv', 'C220n_R2200_dados.csv']

plt.figure(figsize=(10, 6))

#Obtém dados das colunas de cada csv
for csv_file in arquivos_csv:
    frequencia, transmitancia_dB = calcular_transmitancia(csv_file)
    plt.scatter(frequencia, transmitancia_dB, label=f'Transmitância ({csv_file})')

# Configurações do gráfico
plt.xscale('log')  # Escala logarítmica no eixo x (frequência)
plt.xlabel('Frequência (Hz)')
plt.ylabel('Transmitância (dB)')
plt.title('Gráfico de Transmitância em dB para Capacitância 200 nF e variação de Resistores')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.savefig('grafico_capacitor_cte.png')

