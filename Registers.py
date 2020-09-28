class Registers:

    def getBinaryAddress(num, num_bits):
        if num_bits == 5:
            return '{0:05b}'.format(num)
        elif num_bits == 6:
            return '{0:06b}'.format(num)
        elif num_bits == 16:
            return '{0:016b}'.format(num)

    def getRtRs_t(arr_split):
        if arr_split[0][1] == 'v':
            rt = Registers.getBinaryAddress(int(arr_split[0][-2] + 2), 5)
            rs = Registers.getBinaryAddress(int(arr_split[1][-2] + 2), 5)
            return (rt, rs)
        
        elif arr_split[0][1] == 'a':
            rt = Registers.getBinaryAddress(int(arr_split[0][-2] + 4), 5)
            rs = Registers.getBinaryAddress(int(arr_split[1][-2] + 4), 5)
            return (rt, rs)

        elif arr_split[0][1] == 't':
            if int(arr_split[0][-2]) < 8:
                rt = Registers.getBinaryAddress(int(arr_split[0][-2]) + 8, 5)
                rs = Registers.getBinaryAddress(int(arr_split[1][-2]) + 8, 5)
            else:
                rt = Registers.getBinaryAddress(int(arr_split[0][-2])%8 + 24, 5)
                rs = Registers.getBinaryAddress(int(arr_split[1][-2])%8 + 25, 5)
            return (rt, rs)

        elif arr_split[0][1] == 's':
            rt = Registers.getBinaryAddress(int(arr_split[0][-2]) + 16, 5)
            rs = Registers.getBinaryAddress(int(arr_split[1][-2]) + 16, 5)
            return (rt, rs)
        
        elif arr_split[0][1] == 'k':
            rt = Registers.getBinaryAddress(int(arr_split[0][-2]) + 26, 5)
            rs = Registers.getBinaryAddress(int(arr_split[1][-2]) + 26, 5)
            return (rt, rs)

        return (0,0)






    def getReg(type_reg,num):
        if type_reg == 'v':
            reg = Registers.getBinaryAddress(int(num) + 2, 5)
            return (reg)
        
        elif type_reg == 'a':
            reg = Registers.getBinaryAddress(int(num) + 4, 5)
            return (reg)

        elif type_reg == 't':
            if int(num) < 8:
                reg = Registers.getBinaryAddress(int(num) + 8, 5)
            else:
                reg = Registers.getBinaryAddress(int(num)%8 + 24, 5)
            return (reg)

        elif type_reg == 's':
            reg = Registers.getBinaryAddress(int(num) + 16, 5)
            return (reg)
        
        elif type_reg == 'k':
            reg = Registers.getBinaryAddress(int(num) + 26, 5)
            return (reg)

        return (0,0)