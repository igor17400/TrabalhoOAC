from Registers import *
from bmR import *

class TypeR:

    def getRRegisters(instruction):
        #Define os valores dos registradores em binário
        if instruction[0]!="mult" and instruction[0]!="div":
            rd = Registers.getReg(instruction[1][0],instruction[1][1])            
        else:
            rd = '00000'

        if instruction[0]=="sll" or instruction[0]=="srl":
            rs = '00000'
            rt = Registers.getReg(instruction[2][0],instruction[2][1])
        elif instruction[0]=="mult" or instruction[0]=="div":
            rs = Registers.getReg(instruction[1][0],instruction[1][1])
            rt = Registers.getReg(instruction[2][0],instruction[2][1])
        else:
            rs = Registers.getReg(instruction[2][0],instruction[2][1])
            rt = Registers.getReg(instruction[3][0],instruction[3][1])    
        
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
        elif operation=="mult":
            return '011000'
        elif operation=="div":
            return '011010'
        elif operation=="mfhi":
            return '010000'
        elif operation=="mflo":
            return '010010'
        else:
            print("ERROR - FUNCT NOT FOUND")