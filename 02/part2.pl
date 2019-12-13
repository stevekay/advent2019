#!/usr/bin/perl
@l=split(/,/,<>);
for($noun=0;$noun<100;$noun++) {
  for($verb=0;$verb<100;$verb++) {
    @m = @l;
    $m[1]=$noun;
    $m[2]=$verb;
    for($z=0;$z<=$#m;$z+=4) {
      $opcode = $m[$z];
      $a = $m[$m[$z+1]];
      $b = $m[$m[$z+2]];
      $c = $m[$z+3];
      if($opcode == 1) {
        $v = $a + $b;
        $m[$c]=$v;
      } elsif($opcode == 2) {
        $v = $a * $b;
        $m[$c] = $v;
      } elsif($opcode == 99) {
	if($m[0] == 19690720) {
	  print 100*$noun+$verb,"\n";
	  exit;
        }
      }
    }
  }
}
