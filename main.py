import datetime
from Lab1 import *

def main():
    arr_performance_obj = []

    start_time = datetime.datetime.now()
    arr_bin_machine, arr_performance_obj = startAnalysis()
    end_time = datetime.datetime.now()
    displayMachine(arr_bin_machine)

    print("\n------------------ Análise de Performance ------------------")
    print("Tempo para executar a conversão do código: ", end_time - start_time)
    print("------------------ ------------------ ------------------")

    # for performance in arr_performance_obj:
    #     performance.display()

    Performance.barChartPerInstruction(arr_performance_obj)
    Performance.barChartPerType(arr_performance_obj)

if __name__=="__main__": 
    main() 