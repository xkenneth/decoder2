
#!/usr/bin/env python

import I2of5_decode
import matplotlib.pyplot as plt
import random
import scipy
import time
import random
import math
import cmath

random.seed(time.time()*50)

def rms( x ):
    
    sum = 0.0
    for k in range(len(x)):
        sum += abs(x[k])**2
    
    return math.sqrt(sum/len(x))
    

def add_noise_old (signal,amplitude=0.3):
    noise = [ random.uniform(-amplitude,amplitude) for i in range(len(signal)) ]
    signal += scipy.array(noise)


def add_noise ( signal, shape, amplitude, count ):
    
    n = len(signal)
    noise = scipy.zeros(n)
    
    for l in range(count):
        
        A = random.uniform( -1.0, 1.0 )*amplitude
        pos = random.uniform( 0, n )
        
        for k in range(len(shape)):
            noise [ (k+pos)%n ] += A*shape[k]
    
    for k in range(n):
        signal[k] = signal[k] + noise[k]
    
    

decoder = I2of5_decode.I2of5_decode()

wide = [ 0., 0., 0., 0., 0., 0., 0., 0.8, 1., 0.7, 0.3, 0., 0., 0., 0., 0., 0., 0. ]
narrow = [ 0., 0.8, 1., 0.7, 0.3, 0., ]
    
#    wide = [0., 1., 1.,0.]
#    narrow = [1.,1.]
    
#    plt.plot(narrow)
#    plt.plot(wide)
#    plt.show()
    
decoder.load_shapes( narrow, wide )


wave_a = [ 0.1, 0.2, 0.5, 1., 0.9, 0.8, 0.2, ]
wave_b = [ 0.1, 0.15, 0.25, 0.3, 0.25, 0.3, 0.75, 0.8, 0.9, 1., 1., 1.0, 0.8, 0.5, 0.3, 0.05 ]


#plt.plot(wave_b)
#plt.show()

plot_ = True

for blah in range(100):
    
    i = int((random.uniform( 0, 1000 )*1000)%99)
    
    test_signal = decoder.signal_group[ i ]
    test_value = decoder.value_group[ i ]
    
    if plot_ :
        plt.plot(test_signal)
    
    add_noise( test_signal, wave_a, .25, 50 )
    add_noise( test_signal, wave_b, .25, 1 )
    
    results = decoder.decode( test_signal )

    distances = results[2]
    
    print "certainty:  ", results[1], "\t",( results[0], test_value ), "delta: \t", results[0] - test_value
    
    if plot_ :
        plt.plot(test_signal)
        plt.show()
        
        raw_input('Press Enter...')
        
        plt.hist(results[2], bins=20)
        plt.show()
        
        raw_input('Press Enter...')






#plt.plot(wide)
#plt.show()







    

    
    
    
