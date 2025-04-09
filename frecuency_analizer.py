import numpy as np
import wave
import matplotlib.pyplot as plt

# Abrir el archivo WAV
file = wave.open('grabacion.wav', 'r')

# Obtener parámetros de audio
framerate = file.getframerate()  # Frecuencia de muestreo
nframes = file.getnframes()      # Número de frames
frames = file.readframes(nframes)
file.close()

# Convertir frames a numpy array (int16)
audio_data = np.frombuffer(frames, dtype=np.int16)

# Calcular la FFT
fft_data = np.fft.fft(audio_data)
frequencies = np.fft.fftfreq(len(fft_data), 1 / framerate)

# Tomar solo las frecuencias positivas
positive_frequencies = frequencies[:len(frequencies) // 2]
positive_fft = np.abs(fft_data[:len(fft_data) // 2])

# Graficar el espectrograma
plt.figure(figsize=(10, 6))
plt.plot(positive_frequencies, positive_fft)
plt.title('Espectro de Frecuencia')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')
plt.show()
