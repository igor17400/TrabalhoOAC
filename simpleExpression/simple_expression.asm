.data

.text
.globl main

main:
lw     $t0, 4($gp)       
mult   $t0, $t0   
lw     $t1, 4($gp)       
ori    $t2, $zero, 3     
mult   $t1, $t1     
add    $t2, $t0, $t1     
sw     $t2, 0($gp)       
