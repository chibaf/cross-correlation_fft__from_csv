import numpy as np
import sys
import matplotlib.pyplot as plt

def find_index(c):  # find index of maximum value
  mc=np.amax(c)
  for i in range(len(c)):
    if c[i]==mc:
      im=i
      break
  return im

# read data from csv file
m=np.loadtxt(sys.argv[1],delimiter=',')  # convert a csv file to a matrix from file sys.argv[1]
mt=m.T #transpose matrix

times=np.empty(0) # array for storing result
i=0
while (i+99)<len(mt[1]):
#computing cross-correlation by fft
  v1=mt[1][i:i+99];v2=mt[2][i:i+99]
  c=1.0/(np.linalg.norm(v1)*np.linalg.norm(v2)) 
  f1=np.fft.fft(v1)
  f2=np.conjugate(np.fft.fft(v2))
  ff=f1*f2
  corrf=np.real(np.fft.ifft(ff))*c
#find maximum and calculate time interval
  ix=find_index(corrf) #find maximum
  dt=mt[0][i+ix]-mt[0][i] # calculate interval time 
  times=np.append(times,dt)
  i=i+50
# save result
f = open(sys.argv[2], 'w')
for i in range(len(times)):
  if i<len(times)-1:
    f.write(str(times[i])+",")
  else:
    f.write(str(times[i])+"\n")
f.close()
# plot result
x=range(len(times))
plt.plot(x,times)
plt.show()
exit()
