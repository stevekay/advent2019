#!/usr/bin/python3
import sys
array = sys.stdin.read().split(",")
array[1]='12'
array[2]='2'
cnt=0
while array[cnt] != '99':
    a,b,c = [ int(array[int(array[cnt+1])]),
              int(array[int(array[cnt+2])]),
              int(array[cnt+3]) ]
    opcode = int(array[cnt])
    if opcode == 1:
        array[c] = str(a+b)
    if opcode == 2:
        array[c] = str(a*b)
    cnt += 4
print(array[0])
