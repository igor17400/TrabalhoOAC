#path - /Users/igorlimarochaazevedo/Documents/UnB/OAC/arquivos-exemplo/example_saida.asm

import re
from Registers import *
from bmI import *
from bmJ import *
from TypeI import *
from TypeR import *
from TypeJ import *
from General import *

# str_path = input('Insira o path para o arquivo .asm: ')
str_path = "./example.asm"

labels_dict, total_execution_lines = getLabelsDict(str_path)
total_text_lines = getTotalTextLine(str_path)
arr_bin_machine = []
line_pos = 0

print('--------------')
print(labels_dict)
print('--------------')
for i in range(total_text_lines):

    line = progamCounter(str_path, i)

    ## Pular os espaços em brancos e labels
    # if line.isspace() or re.sub(r"[\n\t\s]*", "", line)[-1] == ':'\
    #         or re.sub(r"[\n\t\s]*", "", line)[0] == '.':
    #     continue
    if line.isspace():
        continue

    #simplifica a instrução removendo partes inutilizadas segundo nossa lógica
    line_regex = re.sub("[$,() ]"," ", line)
    line_regex = re.sub("   "," ",line_regex) #debug
    line_regex = re.sub("  "," ",line_regex) #debug
    instruction = line_regex.split()

    if instruction[0][-1] == ':' or instruction[0][0] == '.':
        continue

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

    elif instruction[0] == 'beq' or instruction[0] == 'bne':
        opcode = TypeI.getOpcode(instruction[0])
        rs, rt = TypeI.getIRegisters(instruction)
        address = TypeI.getAddress(instruction, line_pos, labels_dict)

        # Criar o objeto e salva-lo em uma list para acesso posteriormente
        bm = BinaryMachineI(line, str(line_pos), opcode, rs, rt, address)
        arr_bin_machine.append(bm)

    elif instruction[0] == 'j' or instruction[0] == 'jal':
        opcode = TypeJ.getOpcode(instruction[0])
        address = TypeJ.getAddress(instruction, line_pos, labels_dict)

        # Criar o objeto e salva-lo em uma list para acesso posteriormente
        bm = BinaryMachineJ(line, str(line_pos), opcode, address)
        arr_bin_machine.append(bm)

    elif instruction[0] == 'jr':
        opcode = TypeJ.getOpcode(instruction[0])
        address = TypeJ.getAddress(instruction, line_pos, labels_dict, instruction[0])

        # Criar o objeto e salva-lo em uma list para acesso posteriormente
        bm = BinaryMachineJ(line, str(line_pos), opcode, address)
        arr_bin_machine.append(bm)

    elif instruction[0] == 'jalr':
        rs, rt, rd = TypeR.getRRegisters(instruction)
        funct = TypeR.getFunct(instruction[0])

        # Criar o objeto e salva-lo em uma list para acesso posteriormente
        bm = BinaryMachineR(line, str(line_pos), '000000', rs, rt, rd, '00000', funct)
        arr_bin_machine.append(bm)

    elif instruction[0] == 'lui':
        opcode = TypeI.getOpcode(instruction[0])
        rs, rt = TypeI.getIRegisters(instruction)
        address = TypeI.getAddress(instruction)

        # Criar o objeto e salva-lo em uma list para acesso posteriormente
        bm = BinaryMachineI(line, str(line_pos), opcode, rs, rt, address)
        arr_bin_machine.append(bm)

    elif instruction[0] == 'addi' or instruction[0] == 'andi' or\
            instruction[0] == 'ori' or instruction[0] == 'xori':
        imidiate_int = int(instruction[3], 0)
        if imidiate_int < 0 and (instruction[0] == 'andi' or\
             instruction[0] == 'ori' or instruction[0] == 'xori'):
            first_pseudo_inst = ['lui', '1', '0xffff']
            opcode = TypeI.getOpcode(first_pseudo_inst[0])
            rs, rt = TypeI.getIRegisters(first_pseudo_inst)
            address = TypeI.getAddress(first_pseudo_inst)

            # Criar o objeto e salva-lo em uma list para acesso posteriormente
            bm = BinaryMachineI(line, str(line_pos), opcode, rs, rt, address)
            arr_bin_machine.append(bm)

            ### Como temos uma pseudo intrução, será necessário salvar mais objetos
            second_pseudo_inst = ['ori', '1', '1', instruction[3]]
            opcode = TypeI.getOpcode(second_pseudo_inst[0])
            rs, rt = TypeI.getIRegisters(second_pseudo_inst)
            address = TypeI.getAddress(second_pseudo_inst)

            # Criar o objeto e salva-lo em uma list para acesso posteriormente
            bm = BinaryMachineI(line, str(line_pos), opcode, rs, rt, address)
            arr_bin_machine.append(bm)

            if(instruction[0] == 'andi'):
                third_pseudo_inst = ['and', instruction[1], instruction[2], '1']
                rs, rt, rd = TypeR.getRRegisters(third_pseudo_inst)
                funct = TypeR.getFunct(third_pseudo_inst[0])
            elif(instruction[0] == 'ori'):
                third_pseudo_inst = ['or', instruction[1], instruction[2], '1']
                rs, rt, rd = TypeR.getRRegisters(third_pseudo_inst)
                funct = TypeR.getFunct(third_pseudo_inst[0])
            elif(instruction[0] == 'xori'):
                third_pseudo_inst = ['xor', instruction[1], instruction[2], '1']
                rs, rt, rd = TypeR.getRRegisters(third_pseudo_inst)
                funct = TypeR.getFunct(third_pseudo_inst[0])

            # Criar o objeto e salva-lo em uma list para acesso posteriormente
            bm = BinaryMachineR(line, str(line_pos), '000000', rs, rt, rd, '00000', funct)
            arr_bin_machine.append(bm)

        else:
            opcode = TypeI.getOpcode(instruction[0])
            rs, rt = TypeI.getIRegisters(instruction)
            address = TypeI.getAddress(instruction)

            # Criar o objeto e salva-lo em uma list para acesso posteriormente
            bm = BinaryMachineI(line, str(line_pos), opcode, rs, rt, address)
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
    elif isinstance(bm, BinaryMachineJ) :
        bm.displayBinMachineJ()
        bm.displayBinMachineHexJ()
    else:
        print("ERROR - bm type not found")

