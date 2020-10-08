#path - /Users/igorlimarochaazevedo/Documents/UnB/OAC/arquivos-exemplo/example_saida.asm

import re
from Registers import *
from bmI import *
from TypeI import *
from TypeR import *

str_path = input('Insira o path para o arquivo .asm: ')

arr_bin_machine = []
line_pos = 0
with open(str_path, 'r') as reader:
    for line in reader:
        #simplifica a instrução removendo partes inutilizadas segundo nossa lógica
        line_regex = re.sub("[$,() ]"," ", line)
        line_regex = re.sub("   "," ",line_regex) #debug
        line_regex = re.sub("  "," ",line_regex) #debug
        instruction = line_regex.split()
        print (f"Instruction:{instruction}")

        if instruction[0] == 'lw' or instruction[0] == 'sw':
            opcode = TypeI.getOpcode(instruction[0])
            rs, rt = TypeI.getIRegisters(instruction)
            address = TypeI.getAddress(instruction[2])

            # Criar o objeto e salva-lo em uma list para acesso posteriormente
            bm = BinaryMachineI(line, str(line_pos), opcode, rs, rt, address)
            arr_bin_machine.append(bm)

        elif instruction[0] in ('add','sub','and','or','nor','xor'):
            rs, rt, rd = TypeR.getRRegisters(instruction)
            funct = TypeR.getFunct(instruction[0])

            # Criar o objeto e salva-lo em uma list para acesso posteriormente
            bm = BinaryMachineR(line, str(line_pos), '000000', rs, rt, rd, '00000', funct)
            arr_bin_machine.append(bm)

        elif instruction[0] == 'sll' or instruction[0] == 'srl':
            rs, rt, rd = TypeR.getRRegisters(instruction)
            funct = TypeR.getFunct(instruction[0])
            shamt = '{0:05b}'.format(int(instruction[3]))

            # Criar o objeto e salva-lo em uma list para acesso posteriormente
            bm = BinaryMachineR(line, str(line_pos), '000000', rs, rt, rd, shamt, funct)
            arr_bin_machine.append(bm)
        
        elif instruction[0] == 'mult' or instruction[0] == 'div':
            rs, rt, rd = TypeR.getRRegisters(instruction)
            funct = TypeR.getFunct(instruction[0])

            # Criar o objeto e salva-lo em uma list para acesso posteriormente
            bm = BinaryMachineR(line, str(line_pos), '000000', rs, rt, rd, '00000', funct)
            arr_bin_machine.append(bm)

        elif instruction[0] == 'mfhi' or instruction[0] == 'mflo':
            rs = '00000'
            rt = '00000'
            rd = Registers.getReg(instruction[1][0],instruction[1][1])
            funct = TypeR.getFunct(instruction[0])

            # Criar o objeto e salva-lo em uma list para acesso posteriormente
            bm = BinaryMachineR(line, str(line_pos), '000000', rs, rt, rd, '00000', funct)
            arr_bin_machine.append(bm)
        
        else:
            print("ERROR - INSTRUCTION NOT RECOGNIZED")

        line_pos += 1

for bm in arr_bin_machine:
    if isinstance(bm, BinaryMachineI) :
        bm.displayBinMachineI()
        bm.displayBinMachineHexI()
    elif isinstance(bm, BinaryMachineR) :
        bm.displayBinMachineR()
        bm.displayBinMachineHexR()
    else:
        print("ERROR - bm type not found")