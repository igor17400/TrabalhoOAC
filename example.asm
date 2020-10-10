.data
a: .word 1, 2, 3

.text
.globl main
main: 
lw    $t0, 1060($t0)      
lui   $t2, 0xffff         
sw    $t0, 1060($t2)
addi   $t1, $t1, -10 
andi  $t1, $t0, 10          
andi  $t1, $t0, -10
ori   $t5, $t6, -10
xori   $t2, $t2, -10