from Registers import *
from bmR import *

class TypeR:

    def getRRegisters(instruction):
        #Define os valores dos registradores em binário
        if instruction[0]!="mult" and instruction[0]!="div" and instruction[0]!="madd" and instruction[0]!="msubu":
            rd = Registers.getReg(instruction[1][0],instruction[1][1])            
        else:
            rd = '00000'

        if instruction[0]=="sll" or instruction[0]=="srl" or instruction[0]=="sra":
            rs = '00000'
            rt = Registers.getReg(instruction[2][0],instruction[2][1])
        elif instruction[0]=="mult" or instruction[0]=="div" or instruction[0]=="madd" or instruction[0]=="msubu":
            rs = Registers.getReg(instruction[1][0],instruction[1][1])
            rt = Registers.getReg(instruction[2][0],instruction[2][1])
        elif instruction[0] == "jalr":
            rs = Registers.getReg(instruction[2][0],instruction[2][1])
            rt = '00000'
        elif instruction[0] == "clo":
            rs = Registers.getReg(instruction[2][0],instruction[2][1])
            rt = '00000'
        elif instruction[0] == "and" and instruction[3].isdigit() or\
                instruction[0] == "or" and instruction[3].isdigit() or\
                instruction[0] == "xor" and instruction[3].isdigit():
            rs = Registers.getReg(instruction[2][0],instruction[2][1])
            rt = Registers.getBinaryAddress(int(instruction[3]), 5)
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
        elif operation=="sra":
            return '000011'
        elif operation=="srav":
            return '000111'
        elif operation=="mult":
            return '011000'
        elif operation=="div":
            return '011010'
        elif operation=="mfhi":
            return '010000'
        elif operation=="mflo":
            return '010010'
        elif operation=="madd":
            return '000000'
        elif operation=="msubu":
            return '000101'
        elif operation=="jalr":
            return "001001"
        elif operation=="clo":
            return "100001"
        else:
            print("ERROR - FUNCT NOT FOUND")