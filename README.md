# Report-Lab-1 Processing of an EMG signal contaminated by different noises

## Introduction

Gaussian noise is a statistical noise whose probability density function is a normal function or Gaussian bell, often used to model random variations that occur in real-life data. For its part, Artifact noise refers to interference or distortions that affect the typical shape of the signal studied (EMG in this case), it can manifest itself as peaks, oscillations or sudden changes in the amplitude of the signal, in some extreme cases, the artifact can be so strong that it completely hides the signal studied. In this context, impulse noise consists of abrupt and short-duration disturbances that are superimposed on the original signal, usually appearing randomly and without any specific pattern.

The signal to noise ratio (SNR) is a metric used in signal processing, it quantifies the proportion between the power or amplitude of the signal of interest and the power or amplitude of the noise that distorts it. It is usually expressed in decibels (dB) and the formula with which it is calculated is:

SNR(dB) =10 *log10(PsignallPnoise) 

In terms of amplitude it is calculated like this:

SNR(dB) =20 *log10(NoiseSignal)

A high SNR (between 10 and 20 dB) indicates that the useful signal is stronger than the noise, making it easier to analyze and process. While a low SNR (<0 dB) indicates that the noise is stronger than the useful signal, which makes it difficult to interpret.

