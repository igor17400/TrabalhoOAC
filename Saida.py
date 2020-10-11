from bmI import *
from bmJ import *
from bmR import *

class Saida:

    def saveFileText(arr_bin_machine, name):
        open("{}.mif".format(name), 'w').close()
        f = open("{}.mif".format(name), 'r+')

        f.write("DEPTH = 4096;\n")
        f.write("WIDTH = 32;\n")
        f.write("ADDRESS_RADIX = HEX;\n")
        f.write("DATA_RADIX = HEX;\n")
        f.write("CONTENT\n")
        f.write("BEGIN\n")
        f.write("\n")

        count = 0
        line_str = ''
        for bm in arr_bin_machine:
            count_hex = "{0:#0{1}x} : ".format(count,4)
            line_str += "004000" + count_hex[2:]
            if isinstance(bm, BinaryMachineI) :
                line_str += bm.getBinMachineHexI() + ';  '

                command = bm.getCommand()
                if command[-1] == '\n':
                    command = command[:-1]
                line_add = '% ' + str(bm.getFakeLine()) + ': ' + command + ' %\n'
                if bm.getIsPseudo():
                    line_add = '\n'
                line_str += line_add

            elif isinstance(bm, BinaryMachineR) :
                line_str += bm.getBinMachineHexR() + ';  '

                command = bm.getCommand()
                if command[-1] == '\n':
                    command = command[:-1]
                line_add = '% ' + str(bm.getFakeLine()) + ': ' + command + ' %\n'
                if bm.getIsPseudo():
                    line_add = '\n'
                line_str += line_add

            elif isinstance(bm, BinaryMachineJ) :
                line_str += bm.getBinMachineHexJ() + ';  '

                command = bm.getCommand()
                if command[-1] == '\n':
                    command = command[:-1]
                line_add = '% ' + str(bm.getFakeLine()) + ': ' + command + ' %\n'
                if bm.getIsPseudo():
                    line_add = '\n'
                line_str += line_add

            else:
                line_str = "ERROR - bm type not found;\n"
            count += 4

        f.write(line_str)
        f.close()

    def saveFileData(arr_data, name):
        open("{}.mif".format(name), 'w').close()
        f = open("{}.mif".format(name), 'r+')

        f.write("DEPTH = 16384;\n")
        f.write("WIDTH = 32;\n")
        f.write("ADDRESS_RADIX = HEX;\n")
        f.write("DATA_RADIX = HEX;\n")
        f.write("CONTENT\n")
        f.write("BEGIN\n")
        f.write("\n")

        count = 0
        line_str = ''
        for data in arr_data:
            count_hex = "{0:#0{1}x} : ".format(count,10)
            line_str += count_hex + data +'\n'
            count += 4
            
        f.write(line_str)
        f.close()