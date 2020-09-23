#entrada: registrador em formato assembly MIPS
#saída: valor hexadecimal correspondente
def registrador(self):
    if self == "$zero":
        return "00000"
    elif self == "$at":
        return "00001"
    elif self == "$v0":
        return "00010"
    elif self == "$v1":
        return "00011"
    elif self == "$a0":
        return "00100"
    elif self == "$a1":
        return "00101"
    elif self == "$a2":
        return "00110"
    elif self == "$a3":
        return "00111"
    elif self == "$t0":
        return "01000"
    elif self == "$t1":
        return "01001"
    elif self == "$t2":
        return "01010"
    elif self == "$t3":
        return "01011"
    elif self == "$t4":
        return "01100"
    elif self == "$t5":
        return "01101"
    elif self == "$t6":
        return "01110"
    elif self == "$t7":
        return "01111"
    elif self == "$s0":
        return "10000"
    elif self == "$s1":
        return "10001"
    elif self == "$s2":
        return "10010"
    elif self == "$s3":
        return "10011"
    elif self == "$s4":
        return "10100"
    elif self == "$s5":
        return "10101"
    elif self == "$s6":
        return "10110"
    elif self == "$s7":
        return "10111"
    elif self == "$t8":
        return "11000"
    elif self == "$t9":
        return "11001"
    elif self == "$k0":
        return "11010"
    elif self == "$k1":
        return "11011"
    elif self == "$gp":
        return "11100"
    elif self == "$sp":
        return "11101"
    elif self == "$fp":
        return "11110"
    elif self == "$ra":
        return "11111"
    else:
        print(f'ERRO - registrador não encontrado: {self}')


#entrada: valor binário (4 bits)
#saída: símbolo hexadecimal correspondente
def bin2hex_4b(self):
    if self == "0000":
        return "0"
    elif self == "0001":
        return "1"
    elif self == "0010":
        return "2"
    elif self == "0011":
        return "3"
    elif self == "0100":
        return "4"
    elif self == "0101":
        return "5"
    elif self == "0110":
        return "6"
    elif self == "0111":
        return "7"
    elif self == "1000":
        return "8"
    elif self == "1001":
        return "9"
    elif self == "1010":
        return "a"
    elif self == "1011":
        return "b"
    elif self == "1100":
        return "c"
    elif self == "1101":
        return "d"
    elif self == "1110":
        return "e"
    elif self == "1111":
        return "f"
    else:
        print(f'ERRO - registrador não encontrado: {self}')


instrucao_entrada = input('Instrução: ')

#separa a operação em operacao[0] e o resto da instrução fica em operacao[1]
operacao = instrucao_entrada.split(" ", 1)

if operacao[0] == "add":
    opcode = "000000"
    shamt = "00000"
    funct = "100000"
    tipo = "R"
else:
    print(f'ERRO - operação não é adição: {operacao[0]}')
    pass

if tipo == "R":
    aux = operacao[1].split(", ", 2) #separa os registradores em aux[0], aux[1] e aux[2]
    rs = aux[1]
    rt = aux[2]
    rd = aux[0]
    r1 = registrador(rs)
    r2 = registrador(rt)
    r3 = registrador(rd)
else:
    pass

instrucao_saida = []
instrucao_saida = opcode + r1 + r2 + r3 + shamt + funct #concatena todas as partes da instrução

linha_hex = ""
for i in range(0,8):
    linha_hex += bin2hex_4b(instrucao_saida[(4*i):(4*i+4)]) #transforma os bits em hexadecimal de 4 em 4

print(linha_hex) #saída: instrução em hexadecimal
