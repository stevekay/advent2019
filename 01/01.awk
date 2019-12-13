#!/usr/bin/awk -f 
{ t += int($1/3)-2 } END { print t }
