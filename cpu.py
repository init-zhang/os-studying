# Instruction set
# 00000000 00000000 00000000
# opcode   r1       r2/immediate
#
# Categories
# 0X control
# 1X registers and memory
# 2X ALU
#
# Control
# 00 nop
# 01 halt
# 02 jump:     addr
# 03 jump =0:  addr, reg
# 04 jump !=0: addr, reg
#
# registers and memory
# 10 write reg:   reg1 = reg2
# 11 write reg i: reg = immediate
# 12 read mem:    reg = mem
# 13 write mem:   mem = reg
# 14 write mem i: mem = immediate
#
# ALU, all results are stored in ALU
# 30 add:   reg1 + reg2
# 31 add i: reg1 + immediate
# 32 mul:   reg1 * reg2
# 33 mul i: reg1 * immediate
# 34 and: reg1 & reg2
# 35 or:  reg1 | reg2
# 36 not: !reg
# 37 xor: reg1 ^ reg2
# 38 shift left:    reg1 << reg2
# 39 shift left i:  reg << immediate
# 3a shift right:   reg1 >> reg2
# 3b shift right i: reg >> immediate
# 3c div: reg1 / reg2
# 3d mod: reg1 % reg2

# CPU registers
C_PC = 0
C_IR = 1
C_MAR = 2
C_MDR = 3
C_ACC = 4
C_R0 = 5
C_R1 = 6
C_R2 = 7
registers = [0] * 8

def read_memory():
    # Implement virtual memory checks
    reg[C_MDR] = mem[reg[C_MAR]]

def write_memory():
    # Implement virtual memory checks
    mem[reg[C_MAR]] = reg[C_MDR]

def decode(reg, mem):
    instruct = reg[C_IR]
    opcode = instruct >> 16
    operand1 = (instruct & 0xFF00) >> 8
    operand2 = instruct & 0xFF

    # Begin the if chain
    if opcode == 0x00:
        pass
    elif opcode == 0x01:
        pass
    elif opcode == 0x02:
        # Get virtual memory offset
        reg[C_PC] = operand1
    elif opcode == 0x03:
        if reg[operand2] == 0:
            reg[C_PC] = operand1
    elif opcode == 0x04:
        if reg[operand2] != 0:
            reg[C_PC] = operand1
