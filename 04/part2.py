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
            if str(a).count(str(digit)*3) == 0:
                repeater=1
        last=digit
        if int(digit) < highest:
            decreaser=1
        if int(digit) > highest:
            highest=int(digit)
    if decreaser==0 and repeater==1:
        cnt+=1
print(cnt)
