.data
a: .word 1, 2, 3

.text
.globl main
main: 
lw    $t0, 1060($t0)      
lui   $t2, 0xffff         
sw    $t0, 1060($t2)      