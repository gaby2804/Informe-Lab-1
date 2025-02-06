# Report-Lab-1 Processing of an EMG signal contaminated by different noises

## Introduction

Gaussian noise is a statistical noise whose probability density function is a normal function or Gaussian bell, often used to model random variations that occur in real-life data. For its part, Artifact noise refers to interference or distortions that affect the typical shape of the signal studied (EMG in this case), it can manifest itself as peaks, oscillations or sudden changes in the amplitude of the signal, in some extreme cases, the artifact can be so strong that it completely hides the signal studied. In this context, impulse noise consists of abrupt and short-duration disturbances that are superimposed on the original signal, usually appearing randomly and without any specific pattern.

The signal to noise ratio (SNR) is a metric used in signal processing, it quantifies the proportion between the power or amplitude of the signal of interest and the power or amplitude of the noise that distorts it. 

A high SNR (between 10 and 20 dB) indicates that the useful signal is stronger than the noise, making it easier to analyze and process. While a low SNR (<0 dB) indicates that the noise is stronger than the useful signal, which makes it difficult to interpret.

Signal processing:

A biomedical signal is characterized by statistical measurements such as the mean of the signal, standard deviation, coefficient of variation, which allowed us to show what the average value of the electrical activity of the muscle looks like, as well as the dispersion of the signal with respect to its mean. From the histogram graph, we obtained the distribution of the amplitude of the signal in certain intervals and with the probability function the probability that the values ​​occurred again in the signal was indicated.

Instructions:

This algorithm was created to process, contaminate and analyze the EMG signal obtained on the page of the article on Gesture Recognition and Biometrics ElectroMyogram (GRABMyo), in which the electromyographic signal of the muscles of the forearm and wrist is acquired.

![](https://github.com/gaby2804/Informe-Lab-1/blob/main/se%C3%B1al%20emg.jpg)


The code begins by defining the file path through the wfdb library, to achieve the extraction and selection of the signal with its sampling frequency with:

```pitón
signal = record.p_signal  
fs = record.fs  

if signal.ndim > 1:
    signal = signal[:, 0]  
```

To carry out the descriptive statistical calculations of the signal, the following lines were programmed:

```pitón
n = len(signal)  
media_manual = sum(signal) / n  
varianza_manual = sum((x - media_manual) ** 2 for x in signal) / (n - 1)  
desviacion_manual = varianza_manual ** 0.5  
coef_variacion_manual = desviacion_manual / media_manual  
```
![](https://github.com/gaby2804/Informe-Lab-1/blob/main/histograma%20y%20funcion.jpg)

To display the histogram and probability function observed in the image, the following were used:

```pitón
hist, bins = np.histogram(signal, bins=30, densens=True)  
pdf = hist  
bin_centers = (bins[:-1] + bins[1:]) / 2
```
In which the probability function is the same histogram but normalized, thanks to the bins function the edges of each bin are given and with bin_centers the central calculations of each of them, with the positions on the x axis.

When contaminating the signal with the three types of noise (Gaussian, impulsive and artifact type), in the first case with Gaussian noise the signal is contaminated by adding a random noise with a normal distribution throughout the signal with noise = np.random.normal(loc=0, scale=np.std(signal) * 0.01, size=signal.shape) and signal_noise = signal + noise adds the noise to the signal base.

![](https://github.com/gaby2804/Informe-Lab-1/blob/main/ruidogaussiano.jpg)

With impulse noise, random peaks are generated in the same signal, to eventually simulate interference.

```pitón
proporcion_ruido = 0.05  
num_impulsos = int(len(signal) * proporcion_ruido)
amplitud_impulsos = np.max(signal) * 0.001
indices_impulsivos = np.random.choice(len(signal), num_impulsos, replace=False)
ruido_impulsivo = np.zeros_like(signal)
ruido_impulsivo[indices_impulsivos] = np.random.choice([-amplitud_impulsos, amplitud_impulsos], size=num_impulsos)
signal_ruido = signal + ruido_impulsivo
```
![](https://github.com/gaby2804/Informe-Lab-1/blob/main/ruidogaussiano.jpg)

There we define that 5% of the signal will be affected by this type of noise, in which it will randomly take specific positions where said impulses occurred, in this way negative and positive values ​​are assigned to each generated impulse added to the signal.

In artifact noise, what enters are two types of interference, the first is a 50 Hz interference where an electrical wave is simulated and the second is randomly selected artifacts with a very low amplitude.

```pitón
f_interferencia = 50  
t = np.arange(len(signal)) / fs 
interferencia = 0.000001 * np.max(signal) * np.sin(2 * np.pi * f_interferencia * t)
```

imagen

Finally, in each of the different noises, the SNR calculation was carried out to measure the impact that each noise had on the analyzed signal, this indicates how strong, intense and high the noise is compared to the signal, with the following corresponding formulas:

```pitón
potencia_signal = np.mean(signal**2)
potencia_ruido = np.mean(ruido**2)
SNR = 10 * np.log10(potencia_signal / potencia_ruido)

potencia_signal = np.mean(signal_ruido**2)
potencia_ruido = np.mean(ruido_impulsivo**2)
SNR = 10 * np.log10(potencia_signal / potencia_ruido)

potencia_signal = np.mean(signal_ruido**2)
potencia_ruido = (np.mean(ruido_artefacto**2)/2)
SNR = 10 * np.log10(potencia_signal / potencia_ruido)
```
In this way the following results were obtained:

imagen

Requirements:
- python 3.9
- matplotlib
- Wfdb Bookstore
