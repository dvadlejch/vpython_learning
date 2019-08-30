import numpy as np
import matplotlib.pyplot as plt

w01 = 20e-3
d1 = 0   #mm
#f_input=input('large(1)(228,6mm)/small(2)(152,4)=' );
f_small = 152.4e-3
f_large = 228.6e-3
f = f_large
wavelength = 25e-6 # mm
z = np.arange(-f, f+10e-3, 0.1e-3)

# ----calculation
# notation has been adopted from prof. Liska's lessons on applied optics
z01 = np.pi* w01**2 / wavelength
denom = np.sqrt( 1 + (z01/f)**2 )
w02 = w01/denom

# beam profile behind the lens
z02 = np.pi * w02**2 / wavelength
w = w02 * np.sqrt( ( 1+ (z/z02)**2 ) )

plt.plot(z*1000, w*1000, z*1e3, -w*1e3, color='black')
# max wavelength
wavelength = 1e-3 # mm
#z = np.arange(-f, f+10e-3, 0.1e-3)

# ----calculation
# notation has been adopted from prof. Liska's lessons on applied optics
z01 = np.pi* w01**2 / wavelength
denom = np.sqrt( 1 + (z01/f)**2 )
w02 = w01/denom

# beam profile behind the lens
z02 = np.pi * w02**2 / wavelength
w = w02 * np.sqrt( ( 1+ (z/z02)**2 ) )

plt.plot(z*1000, w*1000, z*1e3, -w*1e3, color='red')
plt.show()




