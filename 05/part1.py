#!/usr/bin/python3
import sys
array = sys.stdin.read().split(",")
#array[1]='12'
#array[2]='2'
input = 1
cnt=0
while array[cnt] != '99':
    instruction = array[cnt]
    if len(instruction) == 1:
        instruction = '000' + instruction
    if len(instruction) == 2:
        instruction = '00' + instruction
    if len(instruction) == 3:
        instruction = '000' + instruction
    opcode=int(instruction[-2:])
    if opcode == 9:
        break
    modefirst=instruction[-3]
    modesecond=instruction[-4]
    if len(instruction) < 5:
        modethird='0'
    else:
        modethird=instruction[-5]
    if opcode == 1:
        if modefirst == '0':
            a = int(array[int(array[cnt+1])])
        else:
            a = int(array[cnt+1])

        if modesecond == '0':
            b = int(array[int(array[cnt+2])])
        else:
            b = int(array[cnt+2])

        answer = a + b
        c = int(array[cnt+3])
        array[c] = str(answer)
        cnt += 4
    if opcode == 2:
        if modefirst == '0':
            a = int(array[int(array[cnt+1])])
        else:
            a = int(array[cnt+1])

        if modesecond == '0':
            b = int(array[int(array[cnt+2])])
        else:
            b = int(array[cnt+2])

        answer = a * b

        c = array[cnt+3]

        array[int(c)] = str(answer)
        cnt += 4
    if opcode == 3:
        a = int(array[cnt+1])
        array[a] = str(input)
        cnt += 2
    if opcode == 4:
        a = int(array[cnt+1])
        cnt += 2

print(array[0])
