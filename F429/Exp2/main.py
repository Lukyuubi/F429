import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('R1K_dados.csv')

frequencia = df['frequency (Hz)']
fase = df['phase (Ch2-Ch1) (degrees)']
Tdb = df['T_dB']

# Criação do gráfico do Diagrama de Bode - Transmissão em dB
plt.figure(figsize=(10, 6))
plt.semilogx(frequencia, Tdb, marker='o', linestyle='', label='Transmissão (Tdb)')
plt.title('Diagrama de Bode - Transmissão em função da frequência')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Transmissão (dB)')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.savefig('grafico_transmissao.png')

# Criação do gráfico de Fase
plt.figure(figsize=(10, 6))
plt.semilogx(frequencia, fase, marker='o', linestyle='', color='orange', label='Fase (degrees)')
plt.title('Diagrama de Bode - Fase em função da frequência')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (graus)')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.savefig('grafico_fase.png')