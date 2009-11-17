#!/usr/bin/env python

import pdb
import math
import pylab
import random

#half time
narrow = 1.0
wide = 2.0

#defining the integer symbols
symbol0 = ['n','n','w','w','n']
symbol1 = ['w','n','n','n','w']
symbol2 = ['n','w','n','n','w']
symbol3 = ['w','w','n','n','n']
symbol4 = ['n','n','w','n','w']
symbol5 = ['w','n','w','n','n']
symbol6 = ['n','w','w','n','n']
symbol7 = ['n','n','n','w','w']
symbol8 = ['w','n','n','w','n']
symbol9 = ['n','w','n','w','n']

#appending the integer symbols
symbols = [symbol0,symbol1,symbol2,symbol3,symbol4,symbol5,symbol6,symbol7,symbol8,symbol9]

signals = []

def translate_char(char,height=0.0):
    if char == 'n':
        return [1.0*height]
    if char == 'w':
        return [1.0*height,1.0*height]
    else:
        raise Exception("you fucked up.")
        
        
def compute_signal(symbol_a,symbol_b):
    signal = []

    for i in range(len(symbol_a)):
        signal.extend(translate_char(symbol_a[i],1.0))
        signal.extend(translate_char(symbol_b[i],0.0))

    return signal

#calculate all of the symbols
all_symbols = []

for i in range(10):
    for y in range(10):
        all_symbols.append(compute_signal(symbols[i],symbols[y]))

symbol_00 = compute_signal(symbols[0],symbols[0])

def diff_signal(symbol_a,symbol_b):
    signal_diff = []
    for i in range(len(symbol_a)):
        signal_diff.append(symbol_a[i] - symbol_b[i])

    return signal_diff

def signal_error(signal,p=2.0):
    return [ abs(char)**p for char in signal ]

def mean(numberList):
    floatNums = [float(x) for x in numberList]
    return sum(floatNums) / len(numberList)

def add_noise(signal,amplitude=0.3):
    return [ mod + random.uniform(-amplitude,amplitude) for mod in signal ]
    
    
noisy_signal = add_noise(symbol_00,0.5)
perfect_signal = compute_signal(symbols[0],symbols[0])

data = [ sum(signal_error(diff_signal(noisy_signal,sym))) for sym in all_symbols]

print "Min:", min(data)
print "Max:", max(data)
print "Mean:", mean(data)
print "STD:", pylab.std(data)
print "Noisy Signal:",noisy_signal
print "Correct Pattern:", perfect_signal
print "Correct Difference:", diff_signal(noisy_signal,perfect_signal)
print "Correct Error:", signal_error(diff_signal(noisy_signal,perfect_signal))
print "Correct Sum:", sum(signal_error(diff_signal(noisy_signal,perfect_signal)))

data.sort()
print "Sort:"
print data
#opylab.hist(data,bins=30)



for i in range(100):
    stds = []
    noisy_signal = add_noise(symbol_00,1.0/(float(i)+1.0))
    data = [ sum(signal_error(diff_signal(noisy_signal,sym))) for sym in all_symbols]
    stds.append(pylab.std(data))

pylab.hist(stds,bins=30)

pylab.show()
    
    
