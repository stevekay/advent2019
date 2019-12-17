#!/usr/bin/python3
import sys
start,end=sys.argv[1].split("-")
cnt=0
for a in range(int(start),int(end)):
    if a < 100000 or a > 999999:
        continue
    last='z'
    repeater=0
    highest=-1
    decreaser=0
    for digit in str(a):
        if digit == last:
            repeater=1
        last=digit
        if int(digit) < highest:
            decreaser=1
        if int(digit) > highest:
            highest=int(digit)
    if decreaser==1:
        continue
    if repeater==0:
        continue
    cnt+=1
print(cnt)
