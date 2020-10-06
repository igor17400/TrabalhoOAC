from Registers import *
from bmR import *

class TypeR:

    def getRRegisters(instruction):
        #Define os valores dos registradores em binário
        rd = Registers.getReg(instruction[1][0],instruction[1][1])

        if instruction[0]!="sll" and instruction[0]!="srl":
            rs = Registers.getReg(instruction[2][0],instruction[2][1])
            rt = Registers.getReg(instruction[3][0],instruction[3][1])
        else:
            rs = '00000'
            rt = Registers.getReg(instruction[2][0],instruction[2][1])
        
        return rs, rt, rd
        
    def getFunct(operation):
        if operation=="add":
            return '100000'
        elif operation=="sub":
            return '100010'
        elif operation=="and":
            return '100100'
        elif operation=="or":
            return '100101'
        elif operation=="nor":
            return '100111'
        elif operation=="xor":
            return '100110'
        elif operation=="sll":
            return '000000'
        elif operation=="srl":
            return '000010'
        else:
            print("ERROR - FUNCT NOT FOUND")