#!/usr/bin/python3
import sys
l = sys.stdin.read()
origarray=l.split(",")
for noun in range(0,100):
    for verb in range(0,100):
        array = origarray.copy()
        array[1]=str(noun)
        array[2]=str(verb)
        cnt=0
        while array[cnt] != '99':
            opcode = int(array[cnt])
            a,b,c = [ int(array[int(array[cnt+1])]),
                      int(array[int(array[cnt+2])]),
                      int(array[cnt+3]) ]
            if opcode == 1:
                array[c] = str(a+b)
            if opcode == 2:
                array[c] = str(a*b)
            cnt += 4
        if array[0] == '19690720':
            print(str(100*noun+verb))
