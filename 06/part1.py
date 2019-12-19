#!/usr/bin/python3
import sys

def walkp(p):
    global c
    if p != 'COM':
        c += 1
    if p in parents:
        walkp(parents[p])

c=0
parents={}

for l in sys.stdin:
    # chomp
    if l.endswith("\n"):
        l=l[:-1]
    a,b = l.split(")")
    parents[b] = a

for o in parents:
    walkp(o)

print(c)
