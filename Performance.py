import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time

class Performance:
    def __init__(self, command, typeCommand, time1, time2=''):
        self.command = command
        self.typeCommand = typeCommand
        self.time1 = time1
    
    def getCommand(self):
        return self.command
    
    def getTypeCommand(self):
        return self.typeCommand

    def setTime2(self, time2):
        self.time2 = time2

    def calculateTime(self):
        totalTime = self.time2 - self.time1
        return totalTime

    def display(self):
        print("---- Resutado ----")
        print(self.command)
        print(self.typeCommand)
        print(self.calculateTime())
        print("---- ------- ----")

    def barChartPerInstruction(array_performance):
        arr_commands = []
        arr_calculatedTime = []
        
        for performance in array_performance:
            arr_calculatedTime.append(performance.calculateTime().total_seconds())
            arr_commands.append(performance.getCommand())
        

        fig, ax = plt.subplots()

        ax.barh(arr_commands, arr_calculatedTime, align='center')
        ax.invert_yaxis()  

        ax.set_xlabel('Tempo de processamento')
        ax.set_title('Tempo de processamento para cada instrução')

        plt.show()

    def barChartPerType(array_performance):
        arr_type_commands = []
        dict_calculatedTime = {"type R": 0, "type I": 0, "type J": 0}
        
        for performance in array_performance:
            arr_type_commands.append(performance.getTypeCommand())
        
        for performance in array_performance:
            if(performance.getTypeCommand() == 'type R'):
                dict_calculatedTime[performance.getTypeCommand()] += performance.calculateTime().total_seconds()
            elif(performance.getTypeCommand() == 'type I'):
                dict_calculatedTime[performance.getTypeCommand()] += performance.calculateTime().total_seconds()
            elif(performance.getTypeCommand() == 'type J'):
                dict_calculatedTime[performance.getTypeCommand()] += performance.calculateTime().total_seconds()

        fig, ax = plt.subplots()

        objects = ("type R", "type I", "type J")
        y_pos = np.arange(len(objects))
        performance = dict_calculatedTime.values()

        plt.barh(y_pos, performance, align='center', alpha=0.5)
        plt.yticks(y_pos, objects)
        plt.xlabel('Tempo de processamento')
        plt.title('Tempo de processamento para cada tipo de instrução')

        plt.show()

