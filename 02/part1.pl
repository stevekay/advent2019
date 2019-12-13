#!/usr/bin/perl
@l=split(/,/,<>);
$l[1]=12;
$l[2]=2;
for($z=0;$z<=$#l;$z+=4) {
  $opcode = $l[$z];
  $a = $l[$l[$z+1]];
  $b = $l[$l[$z+2]];
  $c = $l[$z+3];
  if($opcode == 1) {
    $v = $a + $b;
    $l[$c]=$v;
  } elsif($opcode == 2) {
    $v = $a * $b;
    $l[$c] = $v;
  } elsif($opcode == 99) {
    print $l[0],"\n";
    exit;
 }
}
