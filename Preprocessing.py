import numpy as np
import scipy as sp
from scipy import signal
from scipy import io as sio
from matplotlib import pyplot as plt
import pywt

### Data extraction
dataset=np.load('github_data/standing_dataset.npz')
data=dataset['data']; labels=dataset['labels']

data0p=data[10]; data1p=data[50]; data2p=data[90]; data3p=data[130]
data4p=data[170]; data5p=data[210]; data6p=data[250]; data7p=data[290] 
data8p=data[330]; data9p=data[370]; data10p=data[410]; data11p=data[450] 
data12p=data[490]; data13p=data[530]; data14p=data[570]; data15p=data[610]

### Optional: Rescaling data
data0p=data0p/255.0; data1p=data1p/255.0; data2p=data2p/255.0; data3p=data3p/255.0 
data4p=data4p/255.0; data5p=data5p/255.0; data6p=data6p/255.0; data7p=data7p/255.0 
data8p=data8p/255.0; data9p=data9p/255.0; data10p=data10p/255.0; data11p=data11p/255.0 
data12p=data12p/255.0; data13p=data13p/255.0; data14p=data14p/255.0; data15p=data15p/255.0 

### Apply Discrete Wavelet Transform
data0p_wt=pywt.dwt2(data0p, 'bior1.3')
data3p_wt=pywt.dwt2(data3p, 'bior1.3')
data6p_wt=pywt.dwt2(data6p, 'bior1.3')
data9p_wt=pywt.dwt2(data9p, 'bior1.3')

### Save Wavelet Coefficients
data3p_wtH=data3p_wt[-1][0]
data3p_wtV=data3p_wt[-1][1]
data3p_wtD=data3p_wt[-1][-1]

### Save Wavelets Coefficients as image
plt.imsave('data3p_wtH.png', data3p_wtH, cmap='RdBu')
plt.imsave('data3p_wtV.png', data3p_wtV, cmap='RdBu')
plt.imsave('data3p_wtD.png', data3p_wtD, cmap='RdBu')


### Clutter removal

m,n=raw_data.shape
LowPass_Clutter = np.zeros((m,n))
Signal_WithOut_Clutter = np.zeros((m,n))
counter = 0; Alpha = 0.7

LowPass_Clutter = Alpha*LowPass_Clutter + (1-Alpha)*Signal_With_Clutter
Signal_WithOut_Clutter= raw_data - LowPass_Clutter;
