#!/usr/bin/python3
import sys
l = sys.stdin.read()
array=l.split(",")
array[1]='12'
array[2]='2'
cnt=0
while array[cnt] != '99':
    opcode = int(array[cnt])
    if opcode == 1:
        a,b,c = [ int(array[int(array[cnt+1])]),
                  int(array[int(array[cnt+2])]),
                  int(array[cnt+3]) ]
        array[c] = str(a+b)
        cnt += 4
    if opcode == 2:
        a,b,c = [ int(array[int(array[cnt+1])]),
                  int(array[int(array[cnt+2])]),
                  int(array[cnt+3]) ]
        array[c] = str(a*b)
        cnt += 4

print(array[0])
