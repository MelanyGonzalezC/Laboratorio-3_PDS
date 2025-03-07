import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.fftpack import fft
from scipy.signal import welch, correlate
from sklearn.decomposition import FastICA
import os  # Para abrir el archivo de audio después de guardarlo

# Función para calcular el SNR
def calculate_snr(signal, noise):
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)
    return 10 * np.log10(signal_power / noise_power)

# Lista de archivos de audio en formato WAV
files = ["audio-santi.wav", "audio-melany.wav", "audio-majo.wav"]
signals = []
sr = None


for file in files:
    signal, sr = librosa.load(file, sr=16000)  
    signals.append(signal)

# Convertir a misma longitud
max_length = max(len(sig) for sig in signals)
signals = np.array([np.pad(sig, (0, max_length - len(sig))) for sig in signals])

# Extraer el ruido de los primeros 5 segundos de cada señal
ruido = np.array([sig[:5 * sr] for sig in signals])

# Calcular SNR para cada señal original
snr_values = {}
for i in range(3):
    snr_values[files[i]] = calculate_snr(signals[i], ruido[i])
    print(f"SNR de {files[i]}: {snr_values[files[i]]:.2f} dB")

# Crear una única figura para todas las gráficas
fig, axes = plt.subplots(3, 3, figsize=(12, 10))

for i, signal in enumerate(signals):
    # Forma de onda
    librosa.display.waveshow(signal, sr=sr, ax=axes[i, 0])
    axes[i, 0].set_title(f"Onda de {files[i]}")
    axes[i, 0].set_xlabel("Tiempo (s)")
    axes[i, 0].set_ylabel("Amplitud (v)")
    
    # FFT de la señal
    N = len(signal)
    T = 1.0 / sr
    freqs = np.fft.fftfreq(N, T)[:N // 2]
    fft_vals = np.abs(fft(signal))[:N // 2]
    axes[i, 1].plot(freqs, fft_vals)
    axes[i, 1].set_title(f"FFT de {files[i]}")
    axes[i, 1].set_xlabel("Frecuencia (Hz)")
    axes[i, 1].set_ylabel(" Voltaje (V) FFT")
    
    # PSD de la señal
    freqs, psd = welch(signal, fs=sr, nperseg=1024)
    axes[i, 2].semilogx(freqs, psd)
    axes[i, 2].set_title(f"Densidad espectral de {files[i]}")
    axes[i, 2].set_xlabel("Frecuencia (Hz)")
    axes[i, 2].set_ylabel("Densidad de potencia(V^2/Hz)")
    axes[i, 2].grid()

plt.tight_layout()
plt.savefig("interfaz_graficas.png")  
plt.show()

# Normalizar señales antes de FastICA
signals -= np.mean(signals, axis=1, keepdims=True)  
signals /= np.std(signals, axis=1, keepdims=True)   

# Aplicar FastICA para separar la voz
ica = FastICA(n_components=3, max_iter=1000, tol=0.001)
sources = ica.fit_transform(signals.T).T  # Matriz de fuentes separadas

# Seleccionar la fuente con mayor energía, asumiendo que la voz tiene más energía
powers = [np.mean(s ** 2) for s in sources]
voz_maj = sources[np.argmax(powers)]  # Fuente con mayor energía

# *Calcular la potencia de la voz separada*
P_voz_maj = np.mean(voz_maj ** 2)
print(f"Potencia de la voz separada: {P_voz_maj:.6f}")

# *Calcular la potencia del ruido (usando los primeros 5 segundos de la señal original)*
P_ruido = np.mean(ruido[0] ** 2)
print(f"Potencia del ruido: {P_ruido:.6f}")

# *Calcular el SNR de la voz separada*
SNR_voz_maj = 10 * np.log10(P_voz_maj / P_ruido)
print(f"SNR de la voz separada: {SNR_voz_maj:.2f} dB")

# Graficar la señal aislada en el dominio del tiempo
plt.figure(figsize=(10, 4))
librosa.display.waveshow(voz_maj, sr=sr)
plt.title("Voz aislada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (v)")
plt.savefig("voz_aislada.png")  # Guardar la señal como imagen
plt.show()

# Guardar el audio separado en formato WAV
sf.write("voz_aislada.wav", voz_maj, sr)

# Reproducir el audio separado usando una alternativa
if os.name == "nt":  # Windows
    os.system("start voz_aislada.wav")
elif os.name == "posix":  # Linux/macOS
    os.system("afplay voz_aislada.wav")  # Mac
    os.system("aplay voz_aislada.wav")   # Linux
