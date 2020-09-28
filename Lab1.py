#path - /Users/igorlimarochaazevedo/Documents/UnB/OAC/arquivos-exemplo/example_saida.asm

import re
from Registers import *
from bm import *
from TypeI import *


str_path = input('Insira o path para o arquivo .asm: ')

arr_bin_machine = []
line_pos = 0
with open(str_path, 'r') as reader:
    for line in reader:
        line_regex = (re.sub("[$,() ]"," ", line))
        line_regex = re.sub("  "," ",line_regex)
        print (f"Line Regex:{line_regex}")

        if line_regex[0:2] == 'lw':
            rs, rt, address = TypeI.getLwSwInstruction(line_regex)

            # Criar o objeto e salva-lo em uma list para acesso posteriormente
            bm = BinaryMachine(line, str(line_pos), '100011', rs, rt, address)
            arr_bin_machine.append(bm)

        elif line[0:2] == 'sw':
            rs, rt, address = TypeI.getLwSwInstruction(line_regex)
            # Criar o objeto e salva-lo em uma list para acesso posteriormente
            bm = BinaryMachine(line, str(line_pos), '101011', rs, rt, address)
            arr_bin_machine.append(bm)

        line_pos += 1

for bm in arr_bin_machine:
    bm.displayBinMachine()
    bm.displayBinMachineHex()