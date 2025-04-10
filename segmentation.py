import os
import wave
import struct
import numpy as np

# Cargar el archivo de audio .wav
def load_wav(filename):
    with wave.open(filename, 'rb') as wav_file:
        framerate = wav_file.getframerate()
        num_frames = wav_file.getnframes()
        audio_data = wav_file.readframes(num_frames)
        audio_data = np.array(struct.unpack('<' + 'h' * (num_frames), audio_data))
    return audio_data, framerate, num_frames

# Guardar un segmento de audio en un archivo .wav
def save_wav(filename, audio_data, framerate):
    num_samples = len(audio_data)
    num_channels = 1  # Mono
    sampwidth = 2  # 16-bit audio
    num_frames = num_samples
    comptype = 'NONE'
    compname = 'not compressed'
    
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(framerate)
        wav_file.setnframes(num_frames)
        wav_file.setcomptype(comptype, compname)
        wav_file.writeframes(audio_data.tobytes())

# Segmentación del audio
def segment_audio(audio_data, framerate, segment_duration, output_folder):
    segment_samples = int(segment_duration * framerate)
    total_samples = len(audio_data)
    
    # Asegurarse de que la carpeta exista
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    segment_count = total_samples // segment_samples
    for i in range(segment_count):
        start_idx = i * segment_samples
        end_idx = (i + 1) * segment_samples
        segment = audio_data[start_idx:end_idx]

        # Guardar el segmento como un archivo .wav
        segment_filename = os.path.join(output_folder, f'segment_{i+1}.wav')
        save_wav(segment_filename, segment, framerate)
        print(f"Segmento {i+1} guardado como {segment_filename}")

    # Si hay sobrante, guardar el último segmento
    if total_samples % segment_samples != 0:
        segment = audio_data[segment_count * segment_samples:]
        segment_filename = os.path.join(output_folder, f'segment_{segment_count + 1}.wav')
        save_wav(segment_filename, segment, framerate)
        print(f"Segmento {segment_count + 1} guardado como {segment_filename}")

# Parámetros
input_file = 'grabacion.wav'  # Archivo de entrada
segment_duration = 1  # Duración de cada segmento en segundos
output_folder = 'segments'  # Carpeta donde se guardarán los segmentos

# Cargar el archivo de audio
audio_data, framerate, num_frames = load_wav(input_file)

# Segmentar el audio y guardar los archivos
segment_audio(audio_data, framerate, segment_duration, output_folder)
