import librosa
import numpy as np
import os
import soundfile as sf

# Ruta del archivo de audio
input_file = "grabacion.wav"
output_dir = "output_folder"
os.makedirs(output_dir, exist_ok=True)

# Cargar el audio
y, sr = librosa.load(input_file, sr=None)

# Extraer características
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
zero_crossings = librosa.feature.zero_crossing_rate(y)
rms = librosa.feature.rms(y=y)

# Imprimir dimensiones (puedes usar estos vectores para ML)
print("MFCCs shape:", mfccs.shape)
print("Chroma shape:", chroma.shape)
print("Spectral Contrast shape:", spectral_contrast.shape)
print("Zero Crossings shape:", zero_crossings.shape)
print("RMS shape:", rms.shape)

# Si quieres guardar las características en un archivo numpy
np.savez(os.path.join(output_dir, 'audio_features.npz'),
         mfccs=mfccs,
         chroma=chroma,
         spectral_contrast=spectral_contrast,
         zero_crossings=zero_crossings,
         rms=rms)