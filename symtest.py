
#!/usr/bin/env python

import I2of5_decode
import matplotlib.pyplot as plt
import random
import scipy
import time

random.seed(time.time()*50)

def add_noise(signal,amplitude=0.3):
    noise = [ random.uniform(-amplitude,amplitude) for i in range(len(signal)) ]
    signal += scipy.array(noise)

decoder = I2of5_decode.I2of5_decode()

wide = [0., 0.2, 0.6, 0.9, 1., 1., 1., 0.9, 0.6, 0.2, 0. ]
narrow = [0.,0.5,1.,0.5,0.]

#wide = [1.,1.]
#narrow = [1.]

decoder.load_shapes( narrow, wide )



test_signal = decoder.signal_group[ 25 ]
test_value = decoder.value_group[ 25 ]

add_noise( test_signal, 0.3 )

results = decoder.decode( test_signal )

#distances = results[2]
#for i in range( len(distances) ):
#    print distances[i]


print 

print results[0]
print test_value


plt.hist(results[2], bins=100)
plt.show()







#plt.plot(wide)
#plt.show()







    

    
    
    
    
