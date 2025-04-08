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

# Convertir frames a numpy array (int16) para poder manipularlo
audio_data = np.frombuffer(frames, dtype=np.int16)

# Crear un tiempo para el eje x (en segundos)
time = np.linspace(0, nframes / framerate, num=nframes)

# Graficar la onda de sonido
plt.figure(figsize=(10, 6))
plt.plot(time, audio_data)
plt.title('Onda de sonido en el dominio del tiempo')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.show()
