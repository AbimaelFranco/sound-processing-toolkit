import numpy as np
import matplotlib.pyplot as plt
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

# Calcular la FFT y obtener las frecuencias
def calculate_fft(audio_data, framerate):
    N = len(audio_data)
    # Realizar la FFT sobre la señal de audio
    fft_result = np.fft.fft(audio_data)
    # Obtener la magnitud de la FFT
    fft_magnitude = np.abs(fft_result)[:N // 2]
    # Calcular las frecuencias correspondientes a los puntos de la FFT
    frequencies = np.fft.fftfreq(N, 1 / framerate)[:N // 2]
    return fft_magnitude, frequencies

# Determinar la frecuencia fundamental (la más baja con mayor amplitud)
def find_fundamental_frequency(fft_magnitude, frequencies):
    # Encontrar el índice de la frecuencia fundamental (el pico más alto en el espectro)
    peak_index = np.argmax(fft_magnitude)
    fundamental_frequency = frequencies[peak_index]
    return fundamental_frequency

# Cargar el archivo de audio
audio_data, framerate = load_wav('grabacion.wav')

# Calcular la FFT
fft_magnitude, frequencies = calculate_fft(audio_data, framerate)

# Encontrar la frecuencia fundamental
fundamental_frequency = find_fundamental_frequency(fft_magnitude, frequencies)

# Imprimir la frecuencia fundamental
print(f"La frecuencia fundamental es: {fundamental_frequency} Hz")

# Visualizar el espectro de frecuencias
plt.figure(figsize=(12, 6))

# Graficar la magnitud de la FFT
plt.plot(frequencies, fft_magnitude)
plt.title('Espectro de Frecuencias')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.xlim(0, 5000)  # Limitar el rango de frecuencias para mejor visualización

# Resaltar la frecuencia fundamental
plt.axvline(fundamental_frequency, color='r', linestyle='--', label=f'Frecuencia Fundamental: {fundamental_frequency:.2f} Hz')
plt.legend()

plt.tight_layout()
plt.show()
