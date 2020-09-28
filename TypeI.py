from Registers import *
from bm import *

class TypeI:
    
    def getLwSwInstruction(instruction):
        #Separar entre a primeira e a segunda parte do comando
        arr_split = instruction[2:].split()

        #Define os valores dos registradores em binário
        rt = Registers.getReg(arr_split[0][0],arr_split[0][1])
        rs = Registers.getReg(arr_split[2][0],arr_split[2][1])

        #Transforma o número do endereço de destino em binário de 16 bits
        address = Registers.getBinaryAddress(int(arr_split[1]), 16)

        return rt,rs,address