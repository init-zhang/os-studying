REGS = {
    "$ac": 4,
    "$r0": 5,
    "$r1": 6,
    "$r2": 7,
}

OPCODES = {
    "nop":  0x00,
    "die":  0x01,
    "j":    0x02,
    "je":   0x03,
    "jne":  0x04,

    "wr":   0x10,
    "wri":  0x11,
    "rm":   0x12,
    "wm":   0x13,
    "wmi":  0x14,

    "add":  0x30,
    "addi": 0x31,
    "mul":  0x32,
    "muli": 0x33,
    "and":  0x34,
    "or":   0x35,
    "not":  0x36,
    "xor":  0x37,
    "sl":   0x38,
    "sli":  0x39,
    "sr":   0x3A,
    "sri":  0x3B,
    "div":  0x3C,
    "mod":  0x3D,
}

def parse_operand(x):
    x = x.strip()
    if x in REGS:
        return REGS[x]
    if x.startswith("0x"):
        return int(x, 16)
    return int(x)

def assemble_line(line):
    line = line.strip()
    if not line:
        return None

    parts = line.replace(",", " ").split()
    mnemonic = parts[0].lower()

    if mnemonic not in OPCODES:
        raise ValueError(f"Unknown instruction '{mnemonic}'")

    opcode = OPCODES[mnemonic]
    operands = parts[1:]

    op1 = 0
    op2 = 0

    if len(operands) == 1:
        op1 = parse_operand(operands[0])
    elif len(operands) == 2:
        op1 = parse_operand(operands[0])
        op2 = parse_operand(operands[1])

    return (opcode << 16) | (op1 << 8) | op2

def assemble(program_text):
    instructions = []
    for n, line in enumerate(program_text.splitlines()):
        if (inst := assemble_line(line)) is not None:
            instructions.append(inst)
    return instructions


# Example usage
if __name__ == "__main__":
    program = """
    wri $r1, 5
    addi $r1, 2
    wr $ac, $r1
    """
    assembled = assemble(program)
    for i, word in enumerate(assembled):
        print(f"{i:02d}: {word:06X}")
