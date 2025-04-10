import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter
import wave
import struct

# Cargar el archivo de audio (.wav)
def load_wav(filename):
    with wave.open(filename, 'rb') as wav_file:
        framerate = wav_file.getframerate()
        num_frames = wav_file.getnframes()
        audio_data = wav_file.readframes(num_frames)
        audio_data = np.array(struct.unpack('<' + 'h' * (num_frames), audio_data))
    return audio_data, framerate

# Guardar el archivo filtrado
def save_wav(filename, audio_data, framerate):
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit samples
        wav_file.setframerate(framerate)
        wav_file.writeframes(struct.pack('<' + 'h' * len(audio_data), *audio_data))

# Diseñar un filtro FIR pasa-bajo
def design_filter(cutoff, framerate, numtaps=101):
    # Diseñar el filtro FIR pasa-bajo
    fir_filter = firwin(numtaps, cutoff, fs=framerate)
    return fir_filter

# Filtrar la señal de audio
def apply_filter(audio_data, fir_filter):
    filtered_audio = lfilter(fir_filter, 1.0, audio_data)
    return filtered_audio

# Cargar el archivo de audio
audio_data, framerate = load_wav('grabacion.wav')

# Diseñar el filtro FIR pasa-bajo
cutoff = 1000  # Frecuencia de corte de 1000 Hz
fir_filter = design_filter(cutoff, framerate)

# Aplicar el filtro
filtered_audio = apply_filter(audio_data, fir_filter)

# Guardar el archivo filtrado
save_wav('audio_filtrado.wav', filtered_audio.astype(np.int16), framerate)

# Visualizar el audio original y el filtrado
plt.figure(figsize=(12, 6))

# Graficar audio original
plt.subplot(2, 1, 1)
plt.plot(audio_data[:1000])  # Mostrar solo los primeros 1000 puntos para no sobrecargar la gráfica
plt.title('Audio Original')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')

# Graficar audio filtrado
plt.subplot(2, 1, 2)
plt.plot(filtered_audio[:1000])  # Mostrar solo los primeros 1000 puntos
plt.title('Audio Filtrado (Pasa-Bajo 1000Hz)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')

plt.tight_layout()
plt.show()
