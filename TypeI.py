from Registers import *
from bmI import *

class TypeI:
    
    def getIRegisters(instruction):

        #Define os valores dos registradores em binário
        rt = Registers.getReg(instruction[1][0],instruction[1][1])
        rs = Registers.getReg(instruction[3][0],instruction[3][1])
        return rs,rt

    def getAddress(instruction):
        #Transforma o número do endereço de destino em binário de 16 bits
        address = Registers.getBinaryAddress(int(instruction), 16)
        return address

    def getOpcode(operation):
        if operation=="lw":
            return '100011'
        elif operation=="sw":
            return '101011'
        else:
            print("ERROR - OPCODE NOT FOUND")