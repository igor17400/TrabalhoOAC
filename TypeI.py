from Registers import *
from bmI import *
from General import *

class TypeI:
    
    def getIRegisters(instruction):

        if instruction[0] == 'bne' or instruction[0] == 'beq':
            #Define os valores dos registradores em binário
            rs = Registers.getReg(instruction[1][0],instruction[1][1])
            rt = Registers.getReg(instruction[2][0],instruction[2][1])
            return rs, rt

        if instruction[0] == 'lui':
            rs = '00000'
            rt = Registers.getReg(instruction[1][0],instruction[1][1])
            
            return rs, rt
        else:
            #Define os valores dos registradores em binário
            rt = Registers.getReg(instruction[1][0],instruction[1][1])
            rs = Registers.getReg(instruction[3][0],instruction[3][1])
            return rs,rt

    def getAddress(instruction, current_line=0, labels_lines={}):

        if instruction[0] == 'bne' or instruction[0] == 'beq':
            line_destiny = labels_lines[instruction[3]]
            temp = (line_destiny) - (current_line+1)
            if temp < 0:
                address = format(temp if temp >= 0 else (1 << 16) + temp, '016b')
            else:
                address = Registers.getBinaryAddress(temp, 16)
            return address

        if instruction[0] == 'lui':
            print('CU')
            imidiate_int = int(instruction[2], 0)
            print(imidiate_int)
            address = Registers.getBinaryAddress(imidiate_int, 16)

            return address

        else:
            #Transforma o número do endereço de destino em binário de 16 bits
            address = Registers.getBinaryAddress(int(instruction), 16)
            return address

    def getOpcode(operation):
        if operation=="lw":
            return '100011'
        elif operation=="sw":
            return '101011'
        elif operation=="beq":
            return "000100"
        elif operation=="bne":
            return "000101"
        elif operation=="lui":
            return "001111"
        else:
            print("ERROR - OPCODE NOT FOUND")