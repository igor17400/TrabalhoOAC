.data
a: .word 1, 2, 3

.text
.globl main
main:  
lw     $t0, 0($gp)      
srl    $t0, $t0, 1      
addi   $t1, $gp, 28     
sll    $t0, $t0, 2      
add    $t1, $t1, $t0    
lw     $t1, 0($t1)      
addi   $t1, $t1, 1      
lw     $t0, 0($gp)      
sll    $t0, $t0, 2      
addi   $t2, $gp, 28     
add    $t2, $t2, $t0    
sw     $t1, 0($t2)      

lw     $t0, 0($gp)      
addi   $t0, $t0, 1      
sll    $t0, $t0, 2      
addi   $t1, $gp, 28     
add    $t1, $t1, $t0    
addi   $t2, $zero, -1   
sw     $t2, 0($t1)      