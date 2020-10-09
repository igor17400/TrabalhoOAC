import re

def progamCounter(str_path, line_number):
    '''Recebe como parâmetro o path do arquivo e a linha 
    a qual deve ser lida. Retorna a linha desejada'''

    file_variable = open(str_path)
    all_lines_variable = file_variable.readlines()
    return all_lines_variable[line_number]

def getLabelsDict(str_path):
    '''Retorna a quantidade de linhas totais executaveis no arquivo .asm 
    e um dicionário que nos da o nome do label e a 
    linha que o mesmo ocorre'''

    labels_lines = dict()
    line_pos = 0

    with open(str_path, 'r') as reader:
        for line in reader:

            if line.isspace():
                continue

            #simplifica a instrução removendo partes inutilizadas segundo nossa lógica
            line_regex = re.sub("[$,() ]"," ", line)
            line_regex = re.sub("   "," ",line_regex) #debug
            line_regex = re.sub("  "," ",line_regex) #debug
            instruction = line_regex.split()

            if instruction[0][0] == '.':
                continue

            if instruction[0][-1] == ':':
                flag = -1
                if instruction[0][:-1] not in labels_lines:
                    labels_lines[instruction[0][:-1]] = line_pos
                continue
            
            line_pos += 1 ## Contador de linhas

    return labels_lines, line_pos

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val  

def getTotalTextLine(path):
    with open(path) as f:
        return sum(1 for _ in f)