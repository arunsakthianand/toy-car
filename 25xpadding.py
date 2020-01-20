import numpy as np
import soundfile as sf
import os

new_data = np.empty([25000,]) #creating an empty array for new file to be generated from original file
y1 = np.empty([25000,])

#lic={"back","forward","left","right","stop"}
#for loc in lic:
#os.mkdir("Final/"+loc)
loc = "forward"
ind = 1
for j in range(1,81):
	b= loc+str(j)+".wav"
	data, samplerate = sf.read(b) #reading audio file using soundfile library
	print(len(data), samplerate,j)
	x= len(data)
	p = 25000-x
	d = int(p/25)
	if(20000>x>12000):
		for y in range(1 ,p, d):   
			for i in range(0,y-1):
		 # ~ #adding empty elements in the array in the start
				new_data[i] =y1[i]
			for i in range(y,x+y-1):
				new_data[i] =data[i-y]
			for i in range(x+y ,24999 ):    #adding empty elements in the array in the end 
				new_data[i] = y1[i]	
			a = loc+"/"+loc+str(ind)+".wav"    #total length becomes 25000
			ind += 1
			sf.write(a, new_data, samplerate)  #audio files are written back to harddisk
			print(len(new_data))
