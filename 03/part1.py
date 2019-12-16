#!/usr/bin/python3
import numpy as np
import sys

s = 11000

def AtoXY( ax,ay ):
    return(ay-s,ax-s)

def XYtoA(ax,ay):
    return(s+ay,s+ax)

g = np.zeros ( [s*2,s*2], dtype=np.int)
g[XYtoA(0,0)]=1
wire=1
col=99999
for a in sys.stdin:
    x,y=[0,0]
    for ele in a.split(','):
        dir,dist=[ ele[0], int(ele[1:]) ]
        if dir=="U":
            yd,xd=[1,0]
        if dir=="D":
            yd,xd=[-1,0]
        if dir=="L":
            yd,xd=[0,-1]
        if dir=="R":
            yd,xd=[0,1]
        while(dist):
            x+=xd
            y-=yd
            if wire==1:
                g[XYtoA(x,y)]=1
            if wire==2 and g[XYtoA(x,y)]==1 and x+y*-1 < col:
                col=x+y*-1
            dist-=1
    wire+=1
            
print(col)
