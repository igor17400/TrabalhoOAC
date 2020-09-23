#path - /Users/igorlimarochaazevedo/Documents/UnB/OAC/arquivos-exemplo/example_saida.asm

from Registers import * 

class binary_machine:

    def __init__(self, command, line, opcode, rs, rt, address):
        self.command = command
        self.line = line
        self.opcode = opcode
        self.rs = rs
        self.rt = rt
        self.address = address

    def setRs(self, rs):
        self.rs = rs

    def setRt(self, rt):
        self.rt = rt
        
    def setOpcode(opcode):
        self.opcode = opcode

    def displayBinMachine(self):
        print('----------------------')
        print(self.command)
        print('line: {}'.format(self.line))
        print('Machine Instruction: {} {} {} {}'.format(self.opcode, self.rs, self.rt, self.address))
    
    def displayBinMachineHex(self):
        print('Hex: {}'.format(hex(int(self.opcode + self.rs + self.rt + self.address, 2))))


str_path = input('Insira o path para o arquivo .asm: ')

arr_bin_machine = []
line_pos = 0
with open(str_path, 'r') as reader:
    for line in reader:

        if line[0:2] == 'lw':
            #Separar entre a primeira e a segunda parte do comando
            arr_split = line[2:].split()
            print(arr_split)

            rt, rs = Registers.getRtRs_t(arr_split)

            # Separar a segunda parte utilizando o parenteses para conseguirmos
            #       obter o address mais facilmente
            split_add = arr_split[1].split('(')
            print(split_add)
            address = Registers.getBinaryAddress(int(split_add[0]), 16)

            # Criar o objeto e salva-lo em uma list para acesso posteriormente
            bm = binary_machine(line, str(line_pos), '100011', rs, rt, address)
            arr_bin_machine.append(bm)

        elif line[0:2] == 'sw':
            #Separar entre a primeira e a segunda parte do comando
            arr_split = line[2:].split()

            rt, rs = Registers.getRtRs_t(arr_split)

            # Separar a segunda parte utilizando o parenteses para conseguirmos
            #       obter o address mais facilmente
            split_add = arr_split[1].split('(')
            address = Registers.getBinaryAddress(int(split_add[0]), 16)

            # Criar o objeto e salva-lo em uma list para acesso posteriormente
            bm = binary_machine(line, str(line_pos), '101011', rs, rt, address)
            arr_bin_machine.append(bm)

        line_pos += 1

for bm in arr_bin_machine:
    bm.displayBinMachine()
    bm.displayBinMachineHex()