import wfdb
import numpy as np
import matplotlib.pyplot as plt

filename = "C:/Users/diego/OneDrive/Documentos/LABORATORIO/LABORATORIO/session1_participant1_gesture10_trial1"
record = wfdb.rdrecord(filename)

wfdb.show_ann_classes()  
print(record.__dict__)  
signal = record.p_signal  
fs = record.fs  

if signal.ndim > 1:
    signal = signal[:, 0]  


time = [i / fs for i in range(len(signal))]  
time_2 = np.arange(len(signal)) / fs  

n = len(signal)  
media_manual = sum(signal) / n  
varianza_manual = sum((x - media_manual) ** 2 for x in signal) / (n - 1)  
desviacion_manual = varianza_manual ** 0.5  
coef_variacion_manual = desviacion_manual / media_manual  

media_np = np.mean(signal)
desviacion_np = np.std(signal, ddof=1)
coef_variacion_np = desviacion_np / media_np

print("\n=== ESTADÍSTICOS DESCRIPTIVOS ===")
print(f"Media (Manual): {media_manual:.5f} | (Numpy): {media_np:.5f}")
print(f"Desviación estándar (Manual): {desviacion_manual:.5f} | (Numpy): {desviacion_np:.5f}")
print(f"Coef. Variación (Manual): {coef_variacion_manual:.5f} | (Numpy): {coef_variacion_np:.5f}")

plt.figure(figsize=(10, 4))
plt.plot(time, signal, label="Señal EMG")
plt.xlabel("Tiempo [s]")
plt.ylabel("Voltaje [V]")
plt.title("Señal EMG Paciente Sano")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 4))
plt.hist(signal, bins=30, alpha=0.75, color='b', edgecolor='black', density=True)
plt.xlabel("Voltaje [V]")
plt.ylabel("Frecuencia")
plt.title("Histograma de la Señal EMG")
plt.grid()
plt.show()

hist, bins = np.histogram(signal, bins=30, density=True)
pdf = hist 
bin_centers = (bins[:-1] + bins[1:]) / 2

plt.figure(figsize=(10, 4))
plt.hist(signal, bins=30, alpha=0.75, color='b', edgecolor='black', density=True)
plt.plot(bin_centers, pdf, marker='o', linestyle='-', color='r', label="Función de Probabilidad")
plt.xlabel("Voltaje [V]")
plt.ylabel("Probabilidad")
plt.title("Función de Probabilidad de la Señal EMG")
plt.legend()
plt.grid()
plt.show()


if signal.ndim > 1:
    signal = signal[:, 0]  
# Generar ruido gaussiano
ruido1 = np.random.normal(loc=0, scale=np.std(signal) * 0.01, size=signal.shape)
ruido2 = np.random.normal(loc=0, scale=np.std(signal) * 0.001, size=signal.shape)
signal_ruido1 = signal + ruido1
signal_ruido2 = signal + ruido2
potencia_signal1 = np.mean(signal**2)
potencia_ruido1 = np.mean(ruido1**2)
potencia_signal = np.mean(signal**2)
potencia_ruido = np.mean(ruido2**2)

SNR1 = 10 * np.log10(potencia_signal1 / potencia_ruido1)

SNR2 = 10 * np.log10(potencia_signal / potencia_ruido)

print(f"\nSNR de la señal Gaussiana 1: {SNR1:.2f} dB")
print(f"\nSNR de la señal Gaussiana 2: {SNR2:.2f} dB")

time = np.arange(len(signal)) / fs  

plt.figure(figsize=(10, 4))
plt.plot(time, signal, label="Señal Original", alpha=0.8)
plt.plot(time, signal_ruido1, label="Señal con Ruido", alpha=0.6, linestyle="--")
plt.xlabel("Tiempo [s]")
plt.ylabel("Voltaje [V]")
plt.title("Señal EMG con Ruido Gaussiano")
plt.legend()
plt.grid()
plt.show()

if signal.ndim > 1:
    signal = signal[:, 0]  

# Ruido impulsivo
proporcion_ruido = 0.05  
num_impulsos = int(len(signal) * proporcion_ruido)
amplitud_impulsos1 = np.max(signal) * 0.001
amplitud_impulsos2 = np.max(signal) * 0.00001
# Generar posiciones aleatorias para los impulsos
indices_impulsivos1 = np.random.choice(len(signal), num_impulsos, replace=False)
indices_impulsivos2 = np.random.choice(len(signal), num_impulsos, replace=False)
# Crear el ruido impulsivo 
ruido_impulsivo1 = np.zeros_like(signal)
ruido_impulsivo1[indices_impulsivos1] = np.random.choice([-amplitud_impulsos1, amplitud_impulsos1], size=num_impulsos)
ruido_impulsivo2 = np.zeros_like(signal)
ruido_impulsivo2[indices_impulsivos2] = np.random.choice([-amplitud_impulsos2, amplitud_impulsos2], size=num_impulsos)


signal_ruidox = signal + ruido_impulsivo1
signal_ruido2 = signal + ruido_impulsivo2


potencia_signal1 = np.mean(signal_ruidox**2)
potencia_ruido1 = np.mean(ruido_impulsivo1**2)
potencia_signal = np.mean(signal_ruido2**2)
potencia_ruido = np.mean(ruido_impulsivo2**2)

SNR1 = 10 * np.log10(potencia_signal1 / potencia_ruido1)
SNR2 = 10 * np.log10(potencia_signal / potencia_ruido)

print(f"\nSNR de la señal con ruido impulsivo 1: {SNR1:.2f} dB")
print(f"\nSNR de la señal con ruido impulsivo 2: {SNR2:.2f} dB")
time = np.arange(len(signal)) / fs  

plt.figure(figsize=(10, 4))
plt.plot(time, signal, label="Señal Original", alpha=0.8)
plt.plot(time, signal_ruidox, label="Señal con Ruido Impulsivo", alpha=0.6, linestyle="--")
plt.xlabel("Tiempo [s]")
plt.ylabel("Voltaje [V]")
plt.title("Señal EMG con Ruido Impulsivo")
plt.legend()
plt.grid()
plt.show()


if signal.ndim > 1:
    signal = signal[:, 0]  


f_interferencia =50  # Frecuencia en Hz
t = np.arange(len(signal)) / fs 
interferencia1 = 0.000001 * np.max(signal) * np.sin(2 * np.pi * f_interferencia * t)
interferencia2 = 0.001 * np.max(signal) * np.sin(2 * np.pi * f_interferencia * t)

num_artefactos = 2 
duracion_artefacto = int(0.1 * fs)  
artefacto_amp = np.max(signal) * 0.01


artefactos = np.zeros_like(signal)
artefacto_indices = np.random.randint(0, len(signal) - duracion_artefacto, num_artefactos)

for idx in artefacto_indices:
    artefactos[idx:idx + duracion_artefacto] = artefacto_amp * np.sign(np.random.randn(duracion_artefacto))


ruido_artefacto1 = interferencia1 + artefactos
ruido_artefacto2 = interferencia2 + artefactos
signal_ruidoy = signal + ruido_artefacto1
signal_ruido2 = signal + ruido_artefacto2

potencia_signal1 = np.mean(signal_ruidoy**2)
potencia_ruido1 = (np.mean(ruido_artefacto1**2)/2)
SNR1 = 10 * np.log10(potencia_signal1 / potencia_ruido1)
potencia_signal = np.mean(signal_ruido2**2)
potencia_ruido = (np.mean(ruido_artefacto2**2)/2)
SNR2 = 10 * np.log10(potencia_signal / potencia_ruido)
print(f"\nSNR de la señal con ruido tipo artefacto 1: {SNR1:.2f} dB")
print(f"\nSNR de la señal con ruido tipo artefacto 2: {SNR2:.2f} dB")

plt.figure(figsize=(10, 4))
plt.plot(t, signal, label="Señal Original", alpha=0.8)
plt.plot(t, signal_ruidoy, label="Señal con Ruido Tipo Artefacto", alpha=0.6, linestyle="--")
plt.xlabel("Tiempo [s]")
plt.ylabel("Voltaje [V]")
plt.title("Señal EMG con Ruido tipo Artefacto")
plt.legend()
plt.grid()
plt.show()