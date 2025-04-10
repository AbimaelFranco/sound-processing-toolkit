import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import os

# Leer el archivo de audio
audio_rate, audio_data = read("grabacion.wav")

# Si es estéreo, tomamos un solo canal
if len(audio_data.shape) == 2:
    audio_data = audio_data[:, 0]

# Normalizar a rango [-1, 1]
audio_data = audio_data / np.max(np.abs(audio_data))

# Tomar un fragmento pequeño para visualización (por ejemplo, 0.01 segundos)
duration = 0.001  # segundos
num_samples = int(audio_rate * duration)
segment = audio_data[:num_samples]
time = np.linspace(0, duration, num_samples)

# Parámetros de cuantización
bits = 5  # Cambia este valor para más o menos resolución
levels = 2 ** bits

# Cuantización uniforme
min_val, max_val = -1, 1
step = (max_val - min_val) / levels
quantized = np.round((segment - min_val) / step) * step + min_val

# Codificación binaria
quantized_indices = np.clip(np.round((segment - min_val) / step), 0, levels - 1).astype(int)
binary_codes = [format(val, f'0{bits}b') for val in quantized_indices]

# Gráfica
plt.figure(figsize=(12, 6))
plt.plot(time, segment, label='Original (analógica)', color='blue', linewidth=1.5)
plt.stem(time, quantized, linefmt='r-', markerfmt='ro', basefmt=' ', label='Cuantizada (digital)')
plt.title(f'Proceso PCM - {bits} bits ({levels} niveles)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

# Mostrar los valores binarios en el gráfico
for i, (t, b) in enumerate(zip(time, binary_codes)):
    if i % int(len(binary_codes) / 10 + 1) == 0:  # Mostrar solo algunos para evitar saturar
        plt.text(t, quantized[i] + 0.05, b, fontsize=8, rotation=90, ha='center')

plt.tight_layout()
plt.show()
