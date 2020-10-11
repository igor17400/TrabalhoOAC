.data
.text
.globl main

main:
li $a1,10
jal show

li $a1,10
jal sort

li $a1,10
jal show

li $v0,10

swap:	
sll $t1,$a1,2
add $t1,$a0,$t1
lw $t0,0($t1)
lw $t2,4($t1)
sw $t2,0($t1)
sw $t0,4($t1)
jr $ra

show:	
add $t0,$a0,$zero
add $t1,$a1,$zero
add $t2,$zero,$zero

loop1: 	
beq $t2,$t1,fim1
li $v0,1
lw $a0,0($t0)
li $v0,4
addi $t0,$t0,4
addi $t2,$t2,1
j loop1

fim1:	
li $v0,4
jr $ra

sort:	
addi $sp,$sp,-20
sw $ra,16($sp)
sw $s3,12($sp)
sw $s2,8($sp)
sw $s1,4($sp)
sw $s0,0($sp)
add $s2,$a0,$zero
add $s3,$a1,$zero
add $s0,$zero,$zero

for1:	
slt $t0,$s0,$s3
beq $t0,$zero,exit1
addi $s1,$s0,-1

for2:	
bne $t0,$zero,exit2
sll $t1,$s1,2
add $t2,$s2,$t1
lw $t3,0($t2)
lw $t4,4($t2)
slt $t0,$t4,$t3
beq $t0,$zero,exit2
add $a0,$s2,$zero
add $a1,$s1,$zero
jal swap
addi $s1,$s1,-1
j for2

exit2:	
addi $s0,$s0,1
j for1

exit1: 	
lw $s0,0($sp)
lw $s1,4($sp)
lw $s2,8($sp)
lw $s3,12($sp)
lw $ra,16($sp)
addi $sp,$sp,20
jr $ra
