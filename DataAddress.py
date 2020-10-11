class HexData:
    def get(line):
        arr_return = []
        for i in range(2,len(line)):
            #print(line[i])
            data = "{0:#0{1}x}".format(int(line[i]),10)
            arr_return.append(data)
        return arr_return