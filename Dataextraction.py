import os
import numpy as np
import scipy as sp
import matplotlib
import seaborn as sns
import csv
from scipy import io as sio
from matplotlib import image as mpimg
from matplotlib import pyplot as plt

### Input the path to your data
dirpath= '/.../data/'
fname1= os.path.join(dirpath,'filename')
fname2= os.path.join(dirpath,'filename2')
fname3= os.path.join(dirpath,'filename3')

## Load the file content
file1= sio.loadmat(fname1, mat_dtype=True)
file2= sio.loadmat(fname2, mat_dtype=True)
file3= sio.loadmat(fname3, mat_dtype=True)
data1= file1['CAM_CFAR_detection_result']
data2= file2['CAM_CFAR_detection_result']
data3= file3['CAM_CFAR_detection_result']

## Display data as image
plt.imshow(data1)
plt.ylabel('Slow time index ($1s= 20$ samples)')
plt.xlabel('Fast time index ($1m= 156$ samples)')
plt.grid(True)
plt.show()

#### Remove the other person from data2
_data2a=[]
for item in data2:
	temp= np.zeros(len(item[301:]))
	item[301:]= temp
	_data2a.append(item)

_data2b=[]
for item in data2:
	temp1= np.zeros(len(item[0:300]))
	temp2= np.zeros(len(item[450:]))
	item[0:300]= temp1
	item[450:]= temp2
	_data2b.append(item)

#### Remove the two other persons from data3
_data3a=[]
for item in data3:
	temp= np.zeros(len(item[359:]))
	item[359:]= temp
	_data3a.append(item)

_data3b=[]	
for item in data3:
	temp1= np.zeros(len(item[0:358]))
	temp2= np.zeros(len(item[515:]))
	item[0:358]= temp1
	item[515:]= temp2
	_data3b.append(item)

_data3c=[]	
for item in data3:
	temp= np.zeros(len(item[0:516]))
	item[0:516]= temp
	_data3c.append(item)

