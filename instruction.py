def limit(x, bits):
    return x & (2**bits-1)

def instruction(opcode, operand1, operand2):
    instruct = 0
    instruct |= limit(opcode, 4) << 16
    instruct |= limit(operand1, 8) << 8
    instruct |= limit(operand2, 8)
    return instruct

def print_instruction(instruct):
    print(instruct >> 16 & 0b1111)
    print(instruct >> 8 & 0b11111111)
    print(instruct & 0b11111111)

instruct = instruction(1,3,5)
print(bin(instruct))
print_instruction(instruct)
