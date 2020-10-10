.data
a: .word 1, 2, 3

.text
.globl main

__start:
la $a0,vetor
li $a1,10
jal show

la $a0,vetor
li $a1,10
jal sort

la $a0,vetor
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
sw $t2,0($t1)

loop1: 	
beq $t2,$t1,fim1
li $v0,1
lw $a0,0($t0)
li $v0,4
la $a0,tab

addi $t0,$t0,4
addi $t2,$t2,1
j loop1

fim1:	
li $v0,4
la $a0,newl

jr $ra

sort:	
addi $t0,$t0,-20
sw $t0,16($t0)
sw $s3,12($t0)
sw $s2,8($t0)
sw $s1,4($t0)
sw $s0,0($t0)

for1:	
slt $t0,$s0,$s3
beq $t0,$t0,exit1
addi $s1,$s0,-1

for2:	
slti $t0,$s1,0
bne $t0,$t0,exit2
sll $t1,$s1,2
add $t2,$s2,$t1
lw $t3,0($t2)
lw $t4,4($t2)
slt $t0,$t4,$t3
beq $t0,$t0,exit2
jal swap
addi $s1,$s1,-1
j for2

exit2:	
addi $s0,$s0,1
j for1

exit1: 	
lw $s0,0($t0)
lw $s1,4($t0)
lw $s2,8($t0)
lw $s3,12($t0)
lw $t0,16($t0)
addi $t0,$t0,20
jr $ra