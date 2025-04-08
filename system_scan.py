import pyaudio

p = pyaudio.PyAudio()

# Listar dispositivos de entrada disponibles
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"Dispositivo {i}: {info['name']} - Canales: {info['maxInputChannels']}")

p.terminate()
