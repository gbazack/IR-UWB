### Split data per time sample (1s = 20 samples)
tsample1s=np.array([20*i for i in range(0,76)])
tsample2s=np.array([40*i for i in range(0,38)])
tsample3s=np.array([60*i for i in range(0,25)])
tsample4s=np.array([80*i for i in range(0,19)])
tsample5s=np.array([100*i for i in range(0,15)])

## Create empty array to store the split data
tsample1s_data= []
tsample2s_data= []
tsample3s_data= []
tsample4s_data= []
tsample5s_data= []


for index in range(len(tsample1s)-1):
	tsample1s_data.append(data1[tsample1s[index]:tsample1s[index+1]])
for index in range(len(tsample2s)-1):
	tsample2s_data.append(data1[tsample2s[index]:tsample2s[index+1]])
for index in range(len(tsample3s)-1):
	tsample3s_data.append(data1[tsample3s[index]:tsample3s[index+1]])
for index in range(len(tsample4s)-1):
	tsample4s_data.append(data1[tsample4s[index]:tsample4s[index+1]])
for index in range(len(tsample5s)-1):
	tsample5s_data.append(data1[tsample5s[index]:tsample5s[index+1]])


##### Save images to local repositories
imdirpath= '/.../results/moving/'
item1s=[]
for index in range(len(tsample1s_data)):
	impath= os.path.join(imdirpath, '1s/p1s'+str(index)+'.png')
	plt.imsave(impath, tsample1s_data[index])
	item1s.append(tsample1s_data[index].sum(axis=0)/20)

item2s=[]	
for index in range(len(tsample2s_data)):
	impath= os.path.join(imdirpath, '2s/p2s'+str(index)+'.png')
	plt.imsave(impath, tsample2s_data[index])
	item2s.append(tsample2s_data[index].sum(axis=0)/40)

item3s=[]
for index in range(len(tsample3s_data)):
	impath= os.path.join(imdirpath, '3s/p3s'+str(index)+'.png')
	plt.imsave(impath, tsample3s_data[index])
	item3s.append(tsample3s_data[index].sum(axis=0)/60)

item4s=[]
for index in range(len(tsample4s_data)):
	impath= os.path.join(imdirpath, '4s/p4s'+str(index)+'.png')
	plt.imsave(impath, tsample4s_data[index])
	item4s.append(tsample4s_data[index].sum(axis=0)/80)

item5s=[]
for index in range(len(tsample5s_data)):
	impath= os.path.join(imdirpath, '5s/p5s'+str(index)+'.png')
	plt.imsave(impath, tsample5s_data[index])
	item5s.append(tsample5s_data[index].sum(axis=0)/100)

##### Save data as CSV files
radar_range=np.arange(782)/156
csvdirpath= '/.../results/moving/data/'

with open(csvdirpath+'1s/pm1s.csv', 'w', newline='') as pm1scsv:
		fieldnames= ['Radar_range']
		for index in range(len(item1s)):
			fieldnames.append('Time.slot'+str(index))
		f= csv.DictWriter(pm1scsv, fieldnames=fieldnames)
		f.writeheader()
		
		for i in range(len(radar_range)):
				temp1= [('Radar_range', radar_range[i])]
				temp2= [('Time.slot'+str(index),item1s[index][i]) for index in range(len(item1s))]
				dico= dict(temp1+temp2)
				f.writerow(dico)

