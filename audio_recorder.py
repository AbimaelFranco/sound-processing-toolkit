import pyaudio
import wave

# Configuración de parámetros de grabación
FORMAT = pyaudio.paInt16  # Formato de audio
CHANNELS = 1              # Número de canales (estéreo)
RATE = 44100              # Frecuencia de muestreo (samples per second)
CHUNK = 1024              # Tamaño del buffer
SECONDS = 5              # Duración de la grabación en segundos
FILENAME = "grabacion.wav"  # Nombre del archivo de salida

# Inicializar pyaudio
p = pyaudio.PyAudio()

# Abrir flujo de grabación
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Grabando...")

frames = []

# Grabar durante 15 segundos
for i in range(0, int(RATE / CHUNK * SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# Detener la grabación
print("Grabación terminada.")
stream.stop_stream()
stream.close()
p.terminate()

# Guardar el archivo WAV
with wave.open(FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Archivo guardado como {FILENAME}")
