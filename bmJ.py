class BinaryMachineJ:

    def __init__(self, command, line, opcode, address):
        self.command = command
        self.line = line
        self.opcode = opcode
        self.address = address
        
    def setOpcode(opcode):
        self.opcode = opcode

    def displayBinMachineJ(self):
        print('----------------------')
        print(self.command)
        print('line: {}'.format(self.line))
        print('Machine Instruction: {} {}'.format(self.opcode, self.address))
    
    def displayBinMachineHexJ(self):
        aux = int(self.opcode + self.address, 2)
        print("Hex: {0:#0{1}x}".format(aux,10)) #hexa 8 bits (+0x)