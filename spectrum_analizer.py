import numpy as np
import wave
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

# Abrir archivo WAV
file = wave.open('grabacion.wav', 'r')

# Obtener parámetros de audio
framerate = file.getframerate()
nframes = file.getnframes()
frames = file.readframes(nframes)
file.close()

# Convertir frames a numpy array
audio_data = np.frombuffer(frames, dtype=np.int16)

# Generar el espectrograma
f, t, Sxx = spectrogram(audio_data, framerate)

# Graficar el espectrograma
plt.figure(figsize=(10, 6))
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='auto')
plt.title('Espectrograma')
plt.xlabel('Tiempo [s]')
plt.ylabel('Frecuencia [Hz]')
plt.colorbar(label='Intensidad [dB]')
plt.show()
