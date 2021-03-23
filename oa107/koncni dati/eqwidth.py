from astropy.io import fits
from astropy import units as u
import numpy as np
from matplotlib import pyplot as plt
from astropy.visualization import quantity_support
quantity_support()  # for getting units on the axes below  

f = fits.open('https://dr14.sdss.org/optical/spectrum/view/data/format=fits/spec=lite?plateid=1323&mjd=52797&fiberid=12')  
# The spectrum is in the second HDU of this file.
specdata = f[1].data 
f.close() 

from specutils import Spectrum1D
lamb = 10**specdata['loglam'] * u.AA 
flux = specdata['flux'] * 10**-17 * u.Unit('erg cm-2 s-1 AA-1') 
spec = Spectrum1D(spectral_axis=lamb, flux=flux) 

f, ax = plt.subplots()  
ax.step(spec.spectral_axis, spec.flux) 

from specutils.fitting import fit_generic_continuum
cont_norm_spec = spec / fit_generic_continuum(spec)(spec.spectral_axis) 
f, ax = plt.subplots()  
ax.step(cont_norm_spec.wavelength, cont_norm_spec.flux)  
ax.set_xlim(654*u.nm, 660*u.nm)  

from specutils import SpectralRegion
from specutils.analysis import equivalent_width
equivalent_width(cont_norm_spec, regions=SpectralRegion(6562*u.AA, 6575*u.AA)) 