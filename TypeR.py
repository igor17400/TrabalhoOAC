from Registers import *
from bmR import *

class TypeR:

    def getRRegisters(instruction):
        #Define os valores dos registradores em binário
        rd = Registers.getReg(instruction[1][0],instruction[1][1])
        rs = Registers.getReg(instruction[2][0],instruction[2][1])
        rt = Registers.getReg(instruction[3][0],instruction[3][1])
        return rs,rt,rd

    def getFunct(operation):
        if operation=="add":
            return '100000'
        elif operation=="sub":
            return '100010'
        else:
            print("ERROR - FUNCT NOT FOUND")