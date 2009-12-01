
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

def add_noise_old(signal,amplitude=0.3):
    noise = [ random.uniform(-amplitude,amplitude) for i in range(len(signal)) ]
    signal += scipy.array(noise)


def add_noise( signal, shape, amplitude, count ):
    
    n = len(signal)
    noise = scipy.zeros(n)
    
    for l in range(count):
        
        A = random.uniform( -1.0, 1.0 )*amplitude
        
        pos = random.uniform( 0, n )
        
        for k in range(len(shape)):
            noise [ (k+pos)%n ] += A*shape[k]
    
    for k in range(n):
        signal[k] = signal[k] + noise[k]





narrow_test = [0.3,1.0,0.8,0.2]
wide_test = [0.0, 0.0, 0.3,1.0,0.8,0.2, 0.0, 0.0 ]

narrow = [1.,1.,1.,1.]
wide = [0.0, 0.0, 1.,1.,1.,1., 0.0, 0.0 ]

    

decoder = I2of5_decode.I2of5_decode()
decoder.load_shapes( narrow, wide )

decoder_test = I2of5_decode.I2of5_decode()
decoder_test.load_shapes( narrow_test, wide_test  )


for i in range(100):
    
    i = int((random.uniform( 0, 1000 )*1000)%99)
    
    test_signal = decoder_test.signal_group[ i ]
    test_value = decoder_test.value_group[ i ]
    
    
    
    if False:
        X = [ (7.0*k)/len(decoder.signal_group[i]) for k in range(len(test_signal)) ]
        plt.plot(X, decoder.signal_group[i], X, test_signal )
        plt.show()
        raw_input("Press ENTER to continue...")
    
    if False:
        X = [ (7.0*k)/len(test_signal) for k in range(len(test_signal)) ]
        plt.plot(X, test_signal )
        plt.show()
        raw_input("Press ENTER to continue...")
    
    add_noise_old(test_signal,0.3)
    add_noise( test_signal, [ 0.3, 0.7, 1.0, 0.8, .6, 0.2, 0.1  ], 1.5, 10 )
    add_noise( test_signal, [ 0.3, 0.7, 1.0, 0.8, .6, 1.0, 0.8, .6, 1.0, 0.8, .6, 0.2, 0.1  ], 1.5, 10 )
    
    if True:
        X = [ (7.0*k)/len(decoder.signal_group[i]) for k in range(len(test_signal)) ]
        plt.plot(X, decoder.signal_group[i], X, test_signal )
        plt.show()
        raw_input("Press ENTER to continue...")
    
    
    
    results = decoder.decode( test_signal )
    
    print "test value: " , test_value, ", result: ", results[0], ", certainty: ", results[1]
    
    if False:
        plt.hist( results[3],  bins=100)
        plt.show()
        
        raw_input("Press ENTER to continue...")
    
    
