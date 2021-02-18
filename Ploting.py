########## PLOTING
#Spectrum of a person moving in the radar range
sum_item1s=np.array(item1s).sum(axis=0)/75
sum_item1s2=np.array(item1s2).sum(axis=0)/75
sum_item1s2a=np.array(item1s2a).sum(axis=0)/75
sum_item1s3=np.array(item1s3).sum(axis=0)/75

#sum_item2s=np.array(item2s).sum(axis=0)/37
#sum_item2s2=np.array(item2s2).sum(axis=0)/37
#sum_item2s3=np.array(item2s3).sum(axis=0)/37


fig, ((axe11, axe12), (axe21, axe22)) = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
#
#First row
axe11.plot(radar_range,sum_item1s, label="01 person moving");
axe11.axes.set_ylabel('Signal magnitude');
axe11.legend(loc="upper right", bbox_to_anchor=[1, 1],ncol=2);
axe11.grid(True)
#
axe12.plot(radar_range,sum_item1s2a, label="01 person standing")
axe12.legend(loc="upper right", bbox_to_anchor=[1, 1],ncol=2)
axe12.axes.set_ylim(0,1)
axe12.grid(True)
#
#Second row
axe21.plot(radar_range,sum_item1s3, label="03 persons standing")
axe21.vlines([1.2, 2.3, 3, 3.8], 0,1, colors='r', linestyles='dashed')
axe21.annotate('1st person', xy=(1.8, 0.5), xytext=(1.8, 0.65), arrowprops=dict(facecolor='black', shrink=0.1))
axe21.annotate('2nd person', xy=(2.7, 0.55), xytext=(2.7, 0.75), arrowprops=dict(facecolor='black', shrink=0.1))
axe21.annotate('3rd person', xy=(3.5, 0.25), xytext=(3.5, 0.4), arrowprops=dict(facecolor='black', shrink=0.1))
axe21.axes.set_ylabel('Signal magnitude')
axe21.axes.set_xlabel('Radar range (m)')
axe21.legend(loc="upper right", bbox_to_anchor=[1, 1],ncol=2)
axe21.axes.set_ylim(0,1)
axe21.grid(True)
#
axe22.plot(radar_range,sum_item1s2, label="02 persons standing")
axe22.vlines([0.8, 1.7, 2.7], 0,1, colors='r', linestyles='dashed')
axe22.annotate('1st person', xy=(1.2, 0.78), xytext=(1.19, 0.95), arrowprops=dict(facecolor='black', shrink=0.1))
axe22.annotate('2nd person', xy=(2.2, 0.4), xytext=(2.2, 0.6), arrowprops=dict(facecolor='black', shrink=0.1))
axe22.axes.set_xlabel('Radar range (m)')
axe22.legend(loc="upper right", bbox_to_anchor=[1, 1],ncol=2)
axe22.axes.set_ylim(0,1)
axe22.grid(True)
#
#
fig.show()
###################
#Spectrum of a moving person per range
fig, ((axe11, axe12, axe13), (axe21, axe22, axe23)) = plt.subplots(nrows=2, ncols=3)
#
#First row
axe11.plot(radar_range,item2s[0])
axe11.vlines([3.4, 5.05], 0,1, colors='r', linestyles='dashed')
axe11.text(2, 0.9, 'Captured at time $t_0$', style='italic', bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 2})
axe11.axes.set_ylabel('Magnitude')
axe11.axes.set_ylim(0,1)
axe11.grid(True)
#
axe12.plot(radar_range,item2s[1])
axe12.vlines([2.4, 3.4, 5.05], 0,1, colors='r', linestyles='dashed')
axe12.text(1.8, 0.9, 'Captured at time $t_1=t_0 + 2s$', style='italic', bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 2})
axe12.text(4.25, 0.65, '$t_0$', style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 2})
axe12.axes.set_ylim(0,1)
axe12.grid(True)
#
axe13.plot(radar_range,item2s[2])
axe13.vlines([1.95, 2.4, 3.4, 5.05], 0,1, colors='r', linestyles='dashed')
axe13.text(2.1, 0.9, 'Captured at time $t_2=t_1 + 2s$', style='italic', bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 2})
axe13.text(3.15, 0.65, '$t_1=t_0 + 2s$', style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 2})
axe13.axes.set_ylim(0,1)
axe13.grid(True)
#
#Second row
axe21.plot(radar_range,item2s[3])
axe21.vlines([1.25, 1.95, 2.4], 0,1, colors='r', linestyles='dashed')
axe21.text(0.75, 0.9, 'Captured at time $t_3=t_2 + 2s$', style='italic', bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 2})
axe21.text(2.25, 0.65, '$t_2=t_1 + 2s$', style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 2})
axe21.axes.set_ylabel('Magnitude')
axe21.axes.set_xlabel('Radar range (m)')
axe21.axes.set_ylim(0,1)
axe21.grid(True)
#
axe22.plot(radar_range,item2s[4])
axe22.vlines([0.55,1.25, 1.95], 0,1, colors='r', linestyles='dashed')
axe22.text(0.3, 0.9, 'Captured at time $t_4=t_3 + 2s$', style='italic', bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 2})
axe22.text(1.5, 0.65, '$t_3=t_2 + 2s$', style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 2})
axe22.axes.set_xlabel('Radar range (m)')
axe22.axes.set_ylim(0,1)
axe22.grid(True)
#
axe23.plot(radar_range,item2s[5])
axe23.vlines([0.14,0.55,1.25], 0,1, colors='r', linestyles='dashed')
axe23.text(0.0, 0.9, 'Captured at time $t_5=t_4 + 2s$', style='italic', bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 2})
axe23.text(1, 0.65, '$t_4=t_3 + 2s$', style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 2})
axe23.axes.set_xlabel('Radar range (m)')
axe23.axes.set_ylim(0,1)
axe23.grid(True)
#
fig.show()

#### Plotting the velocity
velocity=[0.205,0.205, 0.35,0.35, 0.35,0.35, 0.225,0.225, 0.5,0.5, 0.8,0.8]
v_range=[0.14,0.5501, 0.55,1.2501, 1.25,1.9501, 1.95,2.401, 2.4,3.401,3.4,5.0]
_vline=[0.14,0.55,1.95, 2.4,3.4,5.0] 

plt.step(v_range,velocity)
plt.vlines(_vline, 0,1, colors='r', linestyles='dashed')
plt.text(1.5, 0.85, 'Person moving towards the radar', style='italic', bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 3})
plt.annotate('.', xy=(0.86, 0.86), xytext=(1.5, 0.85), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('$V_0$', xy=(3.8, 0.8), xytext=(3.8, 0.9), arrowprops=dict(facecolor='black', shrink=0.1))
plt.annotate('$V_1$', xy=(2.8, 0.5), xytext=(2.8, 0.6), arrowprops=dict(facecolor='black', shrink=0.1))
plt.annotate('$V_2$', xy=(2.2, 0.225), xytext=(2.2, 0.3), arrowprops=dict(facecolor='black', shrink=0.1))
plt.annotate('$V_3$', xy=(1.3, 0.35), xytext=(1.3, 0.45), arrowprops=dict(facecolor='black', shrink=0.1))
plt.annotate('$V_4$', xy=(0.3, 0.205), xytext=(0.3, 0.3), arrowprops=dict(facecolor='black', shrink=0.1))
plt.ylabel("Velocity (m/s)")
plt.xlabel('Radar range (m)')
plt.ylim(0,1)
plt.xlim(0,5)
plt.grid(True)
plt.show()

text(4, 0.7, 'Captured at time $t_0$', style='italic', bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 10})

plt.plot(radar_range, item1s[0], radar_range, item1s[1], radar_range, item1s[2], radar_range, item1s[3], radar_range, item1s[4], radar_range, item1s[5], radar_range, item1s[6], radar_range, item1s[7], radar_range, item1s[8], radar_range, item1s[9]);plt.show()

plt.plot(radar_range, item5s[0], radar_range, item5s[1]);plt.show()

