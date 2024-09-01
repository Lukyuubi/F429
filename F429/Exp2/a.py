import math

# Parâmetros do circuito
R = 330  # Ohms
L = 19e-3  # Henry (48.6 mH)
C = 1e-7  # Farad (0,1 microF)

w0 = 1 / math.sqrt(L * C)

gamma = R / (2 * L)
print("w0: ", w0)
freq0 = w0/(2*math.pi)
print("freq0:", freq0)
print("gamma", gamma)

wplus = (math.sqrt(w0**2 + gamma**2)) + gamma
wminus = (math.sqrt(w0**2 + gamma**2)) - gamma
freqplus = wplus/(2*math.pi)
freqminus = wminus/(2*math.pi)
print("w+: ", wplus)
print("freq+ :", freqplus)
print("---------------------")
print("w-: ", wminus)
print("freq- :", freqminus)