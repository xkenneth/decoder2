

import scipy
import math

#defining the 10 possible codes.
code0 = ['n','n','w','w','n']
code1 = ['w','n','n','n','w']
code2 = ['n','w','n','n','w']
code3 = ['w','w','n','n','n']
code4 = ['n','n','w','n','w']
code5 = ['w','n','w','n','n']
code6 = ['n','w','w','n','n']
code7 = ['n','n','n','w','w']
code8 = ['w','n','n','w','n']
code9 = ['n','w','n','w','n']
codes = [code0, code1, code2, code3, code4, code5, code6, code7, code8, code9 ]

def value_map( i, j ):
    # maps from code index to the corresponding value.
    # 0 <= i < 10
    # 0 <= j < 10
    
    return i*10+j


def pnorm( x, p=2 ):
    # computes the p-norm of x
    # http://en.wikipedia.org/wiki/Norm_%28mathematics%29
    # 
    sum = 0.0
    for k in range(len(x)):
        sum += abs(x[k])**p
    
    return sum**(1.0/p)

class I2of5_decode:
    # decode one code of interleaved 2 of 5,
    # http://en.wikipedia.org/wiki/Interleaved_2_of_5
    # 
    # 
    
    signal_group = []
    value_group = []
    
    def load_shapes( self, narrow_shape, wide_shape ):
        
        self.signal_group = []
        
        for i in range(10):
            for j in range(10):
                signal = scipy.array([])
                
                for k in range(5):
                    
                    if ( codes[i][k] == 'n' ):
                        signal = scipy.append( signal, narrow_shape )
                    else:
                        signal = scipy.append( signal, wide_shape )
                    
                    if ( codes[j][k] == 'n' ):
                        signal = scipy.append( signal, scipy.zeros(len(narrow_shape)) )
                    else:
                        signal = scipy.append( signal, scipy.zeros(len(wide_shape)) ) 
                
                signal /= pnorm(signal);
                
                self.signal_group.append( signal )
                self.value_group.append( value_map(i,j) )
    
    def decode( self, signal_in ):
        
        # return data
        certainty = 0
        value = 0
        
        # parameters
        p = 2
        
        # condition signal_in
        signal_in = scipy.array(signal_in)
        signal_in = signal_in[0:len(self.signal_group[0])]
        signal_in /= pnorm(signal_in,p)
        
        # compute signal distances
        distances = []
        
        for k in range(100):
            distances.append( pnorm(self.signal_group[k] - signal_in,p) )
        
        #check that there's only one minimum
        minimum = min(distances)
        min_count = 0
        
        for k in range(100):
            if (distances[k] == minimum ):
                min_count += 1
        
        if ( min_count > 1 ):
            raise Exception("Error: more than one minimum found.")
        
        #get value
        min_index = distances.index( min(distances) )
        value = self.value_group[ min_index ]
        
        # some output for debugging
        if (True):
            out = [ (self.value_group[i],distances[i]) for i in range(len(distances)) ]
        
            def compare(x,y):
                return cmp( x[1], y[1] )
        
            out.sort(compare)
        
            for i in range( len(out) ):
                print out[i]            
        
        #statistical wizardry
        
        distances.sort()        
        minimum = distances[0]
        distances = [ d - minimum for d in distances ]
        
        stdev = scipy.std(distances)
        
        print stdev
        
        
        
        return [value, certainty, distances ]
        
        
        
        
        
        
        

