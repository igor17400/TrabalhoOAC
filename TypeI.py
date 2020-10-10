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

        elif instruction[0] == 'lui':
            rs = '00000'
            # Checar se temos uma letra ou numero no reg.
            if instruction[1][0].isdigit(): 
                rt = Registers.getBinaryAddress(int(instruction[1][0]), 5)
            else:
                rt = Registers.getReg(instruction[1][0],instruction[1][1])
            return rs, rt

        elif instruction[0] == 'addi' or instruction[0] == 'andi' or\
                instruction[0] == 'ori' or instruction[0] == 'xori':
            # Checar se temos uma letra ou numero no reg.
            if instruction[1].isdigit(): 
                rt = Registers.getBinaryAddress(int(instruction[1]), 5)
            else:
                rt = Registers.getReg(instruction[1][0],instruction[1][1])

            if instruction[2].isdigit(): 
                rs = Registers.getBinaryAddress(int(instruction[2]), 5)
            else:
                rs = Registers.getReg(instruction[2][0],instruction[2][1])

            return rs, rt

        elif instruction[0] == 'addiu':
            #Define os valores dos registradores em binário
            rt = Registers.getReg(instruction[1][0],instruction[1][1])
            rs = Registers.getBinaryAddress(int(instruction[2]), 5)
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

        elif instruction[0] == 'lui':
            imidiate_int = int(instruction[2], 0)
            address = Registers.getBinaryAddress(imidiate_int, 16)

            return address

        elif instruction[0] == 'addi' or instruction[0] == 'andi' or\
                instruction[0] == 'ori' or instruction[0] == 'xori':
            imidiate_int = int(instruction[3], 0)
            if imidiate_int < 0:
                address = format(imidiate_int if imidiate_int >= 0 else (1 << 16) + \
                    imidiate_int, '016b')
            else:
                address = Registers.getBinaryAddress(imidiate_int, 16)            

            return address

        elif instruction[0] == 'addiu':
            imidiate_int = int(instruction[3], 0)
            if imidiate_int < 0:
                address = format(imidiate_int if imidiate_int >= 0 else (1 << 16) + \
                    imidiate_int, '016b')
            else:
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
        elif operation=="addi":
            return "001000"
        elif operation=="andi":
            return "001100"
        elif operation=="ori":
            return "001101"
        elif operation=="xori":
            return "001110"
        elif operation=="addiu":
            return "001001"
        else:
            print("ERROR - OPCODE NOT FOUND")