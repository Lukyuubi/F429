import pandas as pd
import numpy as np

# Carregar o arquivo CSV
df = pd.read_csv('R1K_C100n_dados.csv')

# Verificar as primeiras linhas do DataFrame
print(df.head())

# Definir o valor de Tdb para o qual queremos encontrar a frequência
Tdb_target = -3

# Interpolar a frequência
frequencias = df['frequency (Hz)']
Tdb_values = df['T_dB']

# Encontrar a frequência correspondente ao Tdb_target
frequencia_interpolada = np.interp(Tdb_target, Tdb_values, frequencias)

print(f'A frequência correspondente a Tdb = {Tdb_target} dB é {frequencia_interpolada:.2f} Hz')
