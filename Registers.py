class Registers:

    #traduz um número decimal(num) para um binário com N bits, tal que N=num_bits
    def getBinaryAddress(num, num_bits):
        if num_bits == 5:
            return '{0:05b}'.format(num)
        elif num_bits == 6:
            return '{0:06b}'.format(num)
        elif num_bits == 16:
            return '{0:016b}'.format(num)
        elif num_bits == 26:
            return '{0:026b}'.format(num)

    #recebe um registrador da ISA MIPS com a divisão e retorna o número binário correspondente àquele registrador
    def getReg(type_reg,num):

        if type_reg == 'z':
            reg = Registers.getBinaryAddress(0, 5)
            return (reg)

        elif type_reg == 'a' and num == 't':
            reg = Registers.getBinaryAddress(1, 5)
            return (reg)

        elif type_reg == 'v':
            reg = Registers.getBinaryAddress(int(num) + 2, 5)
            return (reg)
        
        elif type_reg == 'a' and num.isdigit():
            reg = Registers.getBinaryAddress(int(num) + 4, 5)
            return (reg)

        elif type_reg == 't':
            if int(num) < 8:
                reg = Registers.getBinaryAddress(int(num) + 8, 5)
            else:
                reg = Registers.getBinaryAddress(int(num)%8 + 24, 5)
            return (reg)

        elif type_reg == 's' and num.isdigit():
            reg = Registers.getBinaryAddress(int(num) + 16, 5)
            return (reg)
        
        elif type_reg == 'k':
            reg = Registers.getBinaryAddress(int(num) + 26, 5)
            return (reg)

        elif type_reg == 'g' and num == 'p':
            reg = Registers.getBinaryAddress(28, 5)
            return (reg)

        elif type_reg == 's' and num == 'p':
            reg = Registers.getBinaryAddress(29, 5)
            return (reg)

        elif type_reg == 'r':
            reg = Registers.getBinaryAddress(31, 5)
            return (reg)
        

        return (0,0)

    def getRegLetter(num):
        num = int(num)
        if num == 0:
            return 'zero'
        elif num == 1:
            return 'at'
        elif num == 2:
            return 'v0'
        elif num == 3:
            return 'v1'