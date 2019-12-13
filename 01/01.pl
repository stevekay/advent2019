#!/usr/bin/perl
while(<>) {
  $a = int($_/3)-2;
  $s += $a;
  $b = $a;
  do {
    $b = int($b/3)-2;
    $t += $b>0 ? $b : 0;
  } while($b>0);
  $t += $a;
}
print "part1=$s, part2=$t\n";
