.data
a: .word 1, 2, 3

.text
.globl main
main: 
lw $t1, 0($t0)
add $t1, $t2, $t3
beq $t3,$t1,teste2
sll $t1, $t2, 2
mult $t1, $t2
div $t1, $t2
mfhi $t1
mflo $t2

teste1:
lw $t2, 0($t0)
lw $t3, 0($t0)
beq $t2,$t3,fim1

teste2:
lw $t2, 0($t0)
lw $t3, 4($t0)
beq $t2,$t1,teste1

fim1:
jr $ra