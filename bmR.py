class BinaryMachineR:

    def __init__(self, command, line, opcode, rs, rt, rd, shamt, funct):
        self.command = command
        self.line = line
        self.opcode = opcode
        self.rs = rs
        self.rt = rt
        self.rd = rd
        self.shamt = shamt
        self.funct = funct

    def setRs(self, rs):
        self.rs = rs

    def setRt(self, rt):
        self.rt = rt
    
    def setRd(self, rd):
        self.rd = rd
        
    def setOpcode(opcode):
        self.opcode = opcode
    
    def setShamt(shamt):
        self.shamt = shamt
    
    def setFunct(funct):
        self.funct = funct

    def displayBinMachineR(self):
        print('----------------------')
        print(self.command)
        print('line: {}'.format(self.line))
        print('Machine Instruction: {} {} {} {} {} {}'.format(self.opcode, self.rs, self.rt, self.rd, self.shamt, self.funct))
    
    def displayBinMachineHexR(self):
        aux = int(self.opcode + self.rs + self.rt + self.rd + self.shamt + self.funct, 2)
        print("Hex: {0:#0{1}x}".format(aux,10)) #hexa 8 bits (+0x)