import math

def position(a,b):
    '''
    a: distance of object from sensor 1
    b: distance of object from sensor 2
    c: distance between sensor 1 & 2
    '''

    i =(a**2-b**2+(0.52**2))/(2*0.52)
    j=math.sqrt(a**2-i**2)
    x1,y1=2,3
    x=x1+i
    y=y1+j
    print(i,j)

position(3,4)