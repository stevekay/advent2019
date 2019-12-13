#!/usr/bin/awk -f
{ a = int($1/3)-2
  b = a
  do {
    b = int(b/3)-2
    t += b>0 ? b : 0
  } while(b > 0)
  t += a
} END {
  print t
}
