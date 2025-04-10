import numpy as np
import matplotlib.pyplot as plt
import wave
import struct
import pywt

# Cargar el archivo de audio (.wav)
def load_wav(filename):
    with wave.open(filename, 'rb') as wav_file:
        framerate = wav_file.getframerate()
        num_frames = wav_file.getnframes()
        audio_data = wav_file.readframes(num_frames)
        audio_data = np.array(struct.unpack('<' + 'h' * (num_frames), audio_data))
    return audio_data, framerate

# Aplicar la transformada wavelet discreta (DWT)
def apply_wavelet_transform(audio_data):
    # Realizar la DWT usando la wavelet 'db1' (Daubechies de orden 1)
    coeffs = pywt.wavedec(audio_data, 'db1', level=6)  # 6 niveles de descomposición
    return coeffs

# Visualizar los coeficientes de la DWT
def plot_wavelet_transform(coeffs):
    # El primer coeficiente es la aproximación (cA), los demás son detalles (cD)
    fig, axes = plt.subplots(len(coeffs), 1, figsize=(12, 8))
    
    for i, coeff in enumerate(coeffs):
        axes[i].plot(coeff)
        axes[i].set_title(f'Coeficientes de Nivel {i}')
        axes[i].set_ylabel('Amplitud')
        axes[i].set_xlabel('Muestras')

    plt.tight_layout()
    plt.show()

# Cargar el archivo de audio
audio_data, framerate = load_wav('grabacion.wav')

# Aplicar la transformada wavelet discreta
coeffs = apply_wavelet_transform(audio_data)

# Visualizar los coeficientes
plot_wavelet_transform(coeffs)
