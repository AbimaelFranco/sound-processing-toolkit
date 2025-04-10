import numpy as np
from scipy.io.wavfile import read, write
from scipy.signal import convolve
import scipy.signal as signal
import os


def apply_reverb(input_audio, reverb_impulse_response):
    # Aplicamos la convolución para simular la reverberación
    return convolve(input_audio, reverb_impulse_response, mode='same')

def apply_distortion(audio_data, gain=10, threshold=0.5):
    # Aumenta el volumen (ganancia)
    audio_data = audio_data * gain
    
    # Clipping: Recorta las amplitudes que exceden un umbral
    audio_data = np.clip(audio_data, -threshold, threshold)
    return audio_data

def apply_pitch_shift(audio_data, shift_factor):
    # Cambia el tono desplazando las frecuencias de manera proporcional
    sample_rate = 44100  # Tasa de muestreo del archivo
    n = len(audio_data)
    x = np.arange(n)
    
    # Cambio de tono mediante re-muestreo
    resampled_audio = signal.resample(audio_data, int(n * shift_factor))
    return resampled_audio

# Cargar el archivo de audio y la respuesta al impulso (IR) de reverb
input_file = 'grabacion.wav'
output_folder = 'effects'  # Carpeta donde se guardarán los efectos
os.makedirs(output_folder, exist_ok=True)
audio_rate, audio_data = read(input_file)

# ----------- REVERB -----------
# Crear o cargar una respuesta al impulso (IR) para la reverberación
impulse_response = np.random.randn(1000)  # Respuesta al impulso simulada (debe ser un archivo de IR real)

# Aplicar reverb
audio_with_reverb = apply_reverb(audio_data, impulse_response)
audio_with_reverb = audio_with_reverb / np.max(np.abs(audio_with_reverb))  # Normaliza
audio_with_reverb = (audio_with_reverb * 32767).astype(np.int16)  # Convierte a int16
# Guardar el archivo de audio con reverb
output_path = os.path.join(output_folder, 'grabacion_con_reverb.wav')
write(output_path, audio_rate, audio_with_reverb)

# ----------- DISTORSIÓN -----------
# Aplicar distorsión al audio
audio_with_distortion = apply_distortion(audio_data)
audio_with_distortion = audio_with_distortion / np.max(np.abs(audio_with_distortion))
audio_with_distortion = (audio_with_distortion * 32767).astype(np.int16)
# Guardar el archivo de audio con distorsión
output_path = os.path.join(output_folder, 'grabacion_con_distorsion.wav')
write(output_path, audio_rate, audio_with_distortion)

# ----------- PITCH SHIFT -----------
# Aplicar cambio de tono (shift_factor > 1 aumenta el tono, < 1 lo disminuye)
shift_factor = 1.2  # Aumenta el tono en un 20%
audio_with_pitch_shift = apply_pitch_shift(audio_data, shift_factor)
audio_with_pitch_shift = audio_with_pitch_shift / np.max(np.abs(audio_with_pitch_shift))
audio_with_pitch_shift = (audio_with_pitch_shift * 32767).astype(np.int16)
# Guardar el archivo de audio con cambio de tono
output_path = os.path.join(output_folder, 'grabacion_con_pitch_shift.wav')
write(output_path, audio_rate, audio_with_distortion)