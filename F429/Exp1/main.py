import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar o arquivo CSV
df = pd.read_csv('R1K_C100n_dados.csv')

# Supondo que o arquivo CSV tenha as colunas 'frequencia', 'V1pp', 'V2pp', 'fase'
frequencia = df['frequency (Hz)']
V1pp = df['Vpp1 (V)']
V2pp = df['Vpp2 (V)']
fase = df['phase (Ch2-Ch1) (degrees)']
# Cálculo da razão V2/V1
razao_V2_V1 = V2pp / V1pp

# Corrigir a fase para garantir que ela comece em 90 graus e decaia
fase_corrigida = np.where(fase <-90, fase + 360, fase)  # Adiciona 360 graus para valores negativos

# Opcionalmente, podemos fixar o valor máximo em 90 graus
fase_corrigida = np.clip(fase_corrigida, None, 90)

# Gráfico log-log da razão V2/V1 em função da frequência
plt.figure(figsize=(10, 6))
plt.loglog(frequencia, razao_V2_V1, label='V2/V1')
plt.title('Razão V2/V1 em função da frequência')
plt.xlabel('Frequência (Hz)')
plt.ylabel('V2/V1')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.savefig('grafico1.png')

# Gráfico semi-log da fase em função da frequência
plt.figure(figsize=(10, 6))
plt.semilogx(frequencia, fase_corrigida, label='Fase')
plt.title('Fase em função da frequência')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (graus)')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.savefig('grafico2.png')
