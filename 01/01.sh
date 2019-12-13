#!/bin/sh
while read A; do
  (( T+=$((A/3-2)) ))
done <input.txt
echo $T
