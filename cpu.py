# Instruction set
# 00000000 00000000 00000000
# opcode   r1       r2/immediate
#
# Valid registers: $ac, $r0, $r1, $r2
#
# Categories
# 0X control
# 1X registers and memory
# 2X ALU
#
# Control
# 00 nop
# 01 die
# 02 j:   addr
# 03 je:  addr, reg = 0?
# 04 jne: addr, reg != 0?
#
# registers and memory
# 10 wg:  reg1 = reg2
# 11 wgi: reg = immediate
# 12 rm:  reg = mem
# 13 wm:  mem = reg
# 14 wmi: mem = immediate
#
# ALU, all results are stored in ALU
# 30 add:  reg1 + reg2
# 31 addi: reg1 + immediate
# 32 mul:  reg1 * reg2
# 33 muli: reg1 * immediate
# 34 and:  reg1 & reg2
# 35 or:   reg1 | reg2
# 36 not:  !reg
# 37 xor:  reg1 ^ reg2
# 38 sl:   reg1 << reg2
# 39 sli:  reg << immediate
# 3a sr:   reg1 >> reg2
# 3b sri:  reg >> immediate
# 3c div:  reg1 / reg2
# 3d mod:  reg1 % reg2

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
    if reg[C_MAR] < 0 or reg[C_MAR] > 7:
        raise Exception("Out of bounds")
    reg[C_MDR] = mem[reg[C_MAR]]

def write_memory():
    # Implement virtual memory checks
    if reg[C_MAR] < 0 or reg[C_MAR] > 7:
        raise Exception("Out of bounds")
    mem[reg[C_MAR]] = reg[C_MDR]

def decode(reg, mem):
    instruct = reg[C_IR]
    opcode = instruct >> 16
    operand1 = (instruct & 0xFF00) >> 8
    operand2 = instruct & 0xFF

    print(opcode, operand1, operand2)

    # Begin the if chain
    if opcode == 0x00:  # nop
        pass
    elif opcode == 0x01:  # die
        pass
    elif opcode == 0x02:  # j adrr
        # Get virtual memory offset
        reg[C_PC] = operand1
    elif opcode == 0x03:  # je addr, reg
        if reg[operand2] == 0:
            reg[C_PC] = operand1
    elif opcode == 0x04:  # jne addr, reg
        if reg[operand2] != 0:
            reg[C_PC] = operand1

    # Registers and memory
    elif opcode == 0x10:  # wg reg1 = reg2
        reg[operand1] = reg[operand2]

    elif opcode == 0x11:  # wgi reg = immediate
        reg[operand1] = operand2

    elif opcode == 0x12:  # rm reg = mem
        reg[C_MAR] = reg[operand2]
        read_memory()
        reg[operand1] = reg[C_MDR]

    elif opcode == 0x13:  # wm mem = reg
        reg[C_MAR] = reg[operand1]
        reg[C_MDR] = reg[operand2]
        write_memory()

    elif opcode == 0x14:  # wmi mem = immediate
        reg[C_MAR] = reg[operand1]
        reg[C_MDR] = operand2
        write_memory()

    # ALU operations (results go to ALU register)
    elif opcode == 0x30:  # add
        reg[C_ACC] = reg[operand1] + reg[operand2]

    elif opcode == 0x31:  # addi
        reg[C_ACC] = reg[operand1] + operand2

    elif opcode == 0x32:  # mul
        reg[C_ACC] = reg[operand1] * reg[operand2]

    elif opcode == 0x33:  # muli
        reg[C_ACC] = reg[operand1] * operand2

    elif opcode == 0x34:  # and
        reg[C_ACC] = reg[operand1] & reg[operand2]

    elif opcode == 0x35:  # or
        reg[C_ACC] = reg[operand1] | reg[operand2]

    elif opcode == 0x36:  # not
        reg[C_ACC] = ~reg[operand1]

    elif opcode == 0x37:  # xor
        reg[C_ACC] = reg[operand1] ^ reg[operand2]

    elif opcode == 0x38:  # sl
        reg[C_ACC] = reg[operand1] << reg[operand2]

    elif opcode == 0x39:  # sli
        reg[C_ACC] = reg[operand1] << operand2

    elif opcode == 0x3A:  # sr
        reg[C_ACC] = reg[operand1] >> reg[operand2]

    elif opcode == 0x3B:  # sri
        reg[C_ACC] = reg[operand1] >> operand2

    elif opcode == 0x3C:  # div
        reg[C_ACC] = reg[operand1] // reg[operand2] if reg[operand2] != 0 else 0

    elif opcode == 0x3D:  # mod
        reg[C_ACC] = reg[operand1] % reg[operand2] if reg[operand2] != 0 else 0

    else:
        raise ValueError(f"Unknown opcode: {opcode:02X}")
