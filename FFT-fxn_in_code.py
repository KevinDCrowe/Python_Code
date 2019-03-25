import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as sfft

#Functions#
def f(x):
    #The function(s)
    z = 4*np.sin(200.0*2.0*np.pi*x)
    return z
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

#Independant Variable#

x = np.linspace(0.0,N*T,N)

#Output
y = f(x)

#FFT Output
yf = sfft.fft(y)

#Frequency associated with a x = linspace(0,N*T,N)
xf = np.linspace(0.0,1.0/(2.0*T),N/2)

#Graphing Options
fig, ax = plt.subplots()
ax.plot(xf, 2.0/N*np.abs(yf[:int(N/2)]))
plt.xscale('log')
plt.title('FFT')
plt.grid(True)
plt.x
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power (V^2)')
plt.show()



