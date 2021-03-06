import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as sfft

#Functions#
def numinput():
    j=0
    while (j<1):
        A= int(input('Enter a number: '))
        #
        # Conditions
        #
        if (A != 0):
            j=j+1
        else:
            print('Enter a different number')
            continue
    return A


#Inputs
print('Please enter the sampling frequency')
F = numinput()
T = 1/F
print('Please enter the number of samples')
N = numinput()
y = #array in question#

#Independant Variable#

x = np.linspace(0.0,N*T,N)



#FFT Output
yf = sfft.fft(y)

#Frequency associated with a x = linspace(0,N*T,N)
xf = np.linspace(0.0,1.0/(2.0*T),N/2)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N*np.abs(yf[:int(N/2)]))
plt.xscale('linear')
plt.title('FFT')
plt.grid(True)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power (V^2)')
plt.show()



