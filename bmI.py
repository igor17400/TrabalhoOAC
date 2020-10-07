class BinaryMachineI:

    def __init__(self, command, line, opcode, rs, rt, address):
        self.command = command
        self.line = line
        self.opcode = opcode
        self.rs = rs
        self.rt = rt
        self.address = address

    def setRs(self, rs):
        self.rs = rs

    def setRt(self, rt):
        self.rt = rt
        
    def setOpcode(opcode):
        self.opcode = opcode

    def displayBinMachineI(self):
        print('----------------------')
        print(self.command)
        print('line: {}'.format(self.line))
        print('Machine Instruction: {} {} {} {}'.format(self.opcode, self.rs, self.rt, self.address))
    
    def displayBinMachineHexI(self):
        print('Hex: {}'.format(hex(int(self.opcode + self.rs + self.rt + self.address, 2))))