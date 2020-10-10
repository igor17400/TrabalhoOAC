.data
a: .word 1, 2, 3

.text
.globl main
main:  
lw    $t0, 1060($t0)
li $a1,10
clo $t0, $t1   
clo $t3, $t7
clo $t8, $t9   
bgez  $t0, loop1
bgezal  $t0, loop1
lui   $t2, 0xffff         
sw    $t0, 1060($t2)
addi   $t1, $t1, -10 
andi  $t1, $t0, 10          
andi  $t1, $t0, -10
ori   $t5, $t6, -10

loop1: 
xori   $t2, $t2, -10
li	$t1, 5
li	$t1, 0xfffff
li	$t1, 0xbbbbbb
li  $t1, 12303291

loop2: 
beq  $t0, $t1, loop1
bne  $t0, $t1, main

