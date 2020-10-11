import datetime
import psutil

from Lab1 import *
from data import *

def main():
    arr_performance_obj = []

    start_time = datetime.datetime.now()
    arr_bin_machine, arr_performance_obj = startAnalysis()
    end_time = datetime.datetime.now()
    #displayMachine(arr_bin_machine) ~~~~> mostra as intruções no terminal

    # gives a single float value
    cpu_percent = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    dict(psutil.virtual_memory()._asdict())
    # you can have the percentage of used RAM
    ram_percentage = psutil.virtual_memory().percent
    percentage_of_available_memory = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total

    print("\n------------------ Análise de Performance na conversão do código ------------------")
    print("Tempo para executar: ", end_time - start_time)
    print("Percentagem de CPU necessária: ", cpu_percent)
    print("Memória virtual utilizada: ", virtual_memory)
    print("Percentagem de memoria disponível: ", percentage_of_available_memory)
    print("------------------ ------------------ ------------------")
    print("Arquivos de saída disponíveis em saida_data.mif e saida_text.mif")

if __name__=="__main__": 
    data()
    main() 