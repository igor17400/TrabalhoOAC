import re
from data import *
from Saida import *
from DataAddress import *

def data(str_name):
    f = open(str_name, "r")
    f = f.read().splitlines()

    k = 0
    arr_data = []
    for line in f:
        k = k+1

        if line.isspace():
            continue
        
        if line == ".data":
            continue

        aux = line.split()
        if not aux:
            continue
        elif aux[0] == ".text":
            break

        line_regex = re.sub("[:., ]"," ", line)
        line_regex = re.sub("  "," ", line_regex)
        line_data = line_regex.split()

        aux = HexData.get(line_data)
        arr_data.extend(aux)

    Saida.saveFileData(arr_data, 'saida_data')
