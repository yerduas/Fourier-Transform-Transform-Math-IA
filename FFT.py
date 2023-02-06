
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, data = wavfile.read(r"FFT Mornning Bell")

#normalizing (this makes the y-axis mroe readable)
data = data / (2**15)

#fft
spectrum = np.fft.fft(data)
spectrum = np.abs(spectrum[:len(spectrum)//2])
frequencies = np.fft.fftfreq(len(data), 1/fs)
frequencies = frequencies[:len(frequencies)//2]

#plot
plt.plot(frequencies, spectrum)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title("Figure 12- Results of an FFT on the Morning Bell Audio")
plt.show()