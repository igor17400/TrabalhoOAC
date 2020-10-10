from Registers import *
from bmI import *
from General import *

class TypeJ:

    def getAddress(instruction, current_line, labels_lines, instruction_name=''):

        if(instruction_name == 'jr'):
            address = Registers.getReg(instruction[1], 0)
            print(address)
            address = str(address) + '000000000000000001000'
        
        else:
            line_destiny = labels_lines[instruction[1]]
            temp = (line_destiny)*4
            binary = "{0:b}".format(temp)
            bin_hex = hex(int(binary, 2))
            if len(bin_hex) == 3:
                bin_hex = bin_hex[0:2] + '0' + bin_hex[-1]
            address = '0x004000' + bin_hex[-2:]

            ## Remover os 4 bits mais a esquerda, ou o primeiro hexa
            address = address[:2] + address[3:]

            ## Remover os 2 bits mais a direita
            address = "{0:028b}".format(int(address, 16))
            address = address[:-2]

            for i in range(26 - len(address)):
                address = '0' + address

        return address

    def getOpcode(operation):
        if operation=="j":
            return '000010'
        elif operation=="jal":
            return '000011'
        elif operation=="jr":
            return "000000"
        else:
            print("ERROR - OPCODE NOT FOUND")