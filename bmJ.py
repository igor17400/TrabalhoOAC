class BinaryMachineJ:

    def __init__(self, command, line, opcode, 
            address, fake_line, isPseudo=False):
        self.command = command
        self.line = line
        self.opcode = opcode
        self.address = address
        self.fake_line = fake_line
        self.isPseudo = isPseudo
        
    def setIsPseudo(self, isPseudo):
        self.isPseudo = isPseudo

    def setOpcode(opcode):
        self.opcode = opcode

    def getIsPseudo(self):
        return self.isPseudo
    
    def getLine(self):
        return self.line
    
    def getFakeLine(self):
        return self.fake_line

    def getCommand(self):
        return self.command

    def displayBinMachineJ(self):
        print('----------------------')
        print(self.command)
        print('line: {}'.format(self.line))
        print('Machine Instruction: {} {}'.format(self.opcode, self.address))
    
    def displayBinMachineHexJ(self):
        aux = int(self.opcode + self.address, 2)
        print("Hex: {0:#0{1}x}".format(aux,10)) #hexa 8 bits (+0x)

    def getBinMachineHexJ(self):
        aux = int(self.opcode + self.address, 2)
        return ("{0:#0{1}x}".format(aux,10)) #hexa 8 bits (+0x)