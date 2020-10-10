import datetime
from Lab1 import *

def main():
    start_time = datetime.datetime.now()
    arr_bin_machine = startAnalysis()
    end_time = datetime.datetime.now()
    displayMachine(arr_bin_machine)
    
    print("\n------------------ Análise de Performance ------------------")
    print("Tempo para executar a conversão do código: ", end_time - start_time)
    print("------------------ ------------------ ------------------")

if __name__=="__main__": 
    main() 