

import csv

def read_csv(file_string):
    file = open(file_string)
    R = csv.reader( file )
    
    lines = []
    
    while True:
        try:
            lines.append( R.next() )
        except:
            break
        else:
            continue
            
    start = 0
    for i in range(len(lines)):
        try:
            [ float(x) for x in lines[i] ]
        except:
            continue
        else:
            start = i
            break
    
    return lines[start:]

if __name__ == '__main__':
    for i in read_csv(open(sys.argv[1])):
        print i








