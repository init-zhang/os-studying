# Memory
# 0-22 OS and scheduler
# 23 Current PID
# 24 Queue tail
# 25 Queue head
# 26-31 Process queue
# 32 Next free PID
# 33-63 Process list
# 64-1023 Processes
M_CURRENT_PID = 23
M_QUEUE_TAIL = 24
M_QUEUE_HEAD = 25
M_QUEUE_BASE = 26
M_QUEUE_END = 31
M_PROCESS_LIST = 32
M_PROCESSES = 64
def init_memory():
    memory = [0xFFFF] * 256
    memory[M_PROCESS_LIST] = 0
    memory[M_QUEUE_TAIL] = M_QUEUE_BASE
    memory[M_QUEUE_HEAD] = M_QUEUE_BASE
    return memory

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

# Processes
P_SIZE = 32
# 0-7 Process control block
PCB_PID = 0
PCB_PC = 1
PCB_ACC = 2
PCB_R0 = 3
PCB_R1 = 4
PCB_R2 = 5
# 8-15 words of data
PD_BASE = 8
PD_LENGTH = 8
# 16-31 words of code
PC_BASE = 16
PC_LENGTH = 16

def start_process(reg, mem, asm):
    pid = mem[M_PROCESS_LIST]+1
    # Validate process limit and check for gaps
    mem[M_PROCESS_LIST] += 1
    process_base = M_PROCESSES+(pid-1)*P_SIZE
    mem[M_PROCESS_LIST+pid] = process_base
    mem[process_base + PCB_PID] = pid
    mem[process_base + PCB_PC] = process_base + PC_BASE
    # Load asm into binary, then into asm
    for i, instruction in enumerate(assemble(asm)):
        mem[process_base + PC_BASE + i] = instruction
    mem[M_CURRENT_PID] = pid
    enqueue(reg, mem)

# Placeholder
def assemble(asm):
    for line in asm:
        yield line

def save_process(reg, mem):
    process_base = mem[M_PROCESS_LIST+mem[M_CURRENT_PID]]
    mem[process_base + PCB_PC] = reg[C_PC]
    mem[process_base + PCB_ACC] = reg[C_ACC]
    mem[process_base + PCB_R0] = reg[C_R0]
    mem[process_base + PCB_R1] = reg[C_R1]
    mem[process_base + PCB_R2] = reg[C_R2]

def load_process(reg, mem):
    process_base = mem[M_PROCESS_LIST+mem[M_CURRENT_PID]]
    reg[C_PC] = mem[process_base + PCB_PC]
    reg[C_ACC] = mem[process_base + PCB_ACC]
    reg[C_R0] = mem[process_base + PCB_R0]
    reg[C_R1] = mem[process_base + PCB_R1]
    reg[C_R2] = mem[process_base + PCB_R2]

def enqueue(reg, mem):
    mem[mem[M_QUEUE_TAIL]] = mem[M_CURRENT_PID]
    mem[M_QUEUE_TAIL] += 1
    if mem[M_QUEUE_TAIL] > M_QUEUE_END:
        mem[M_QUEUE_TAIL] = M_QUEUE_BASE

def dequeue(reg, mem):
    mem[M_CURRENT_PID] = mem[mem[M_QUEUE_HEAD]]
    mem[M_QUEUE_HEAD] += 1
    if mem[M_QUEUE_HEAD] > M_QUEUE_END:
        mem[M_QUEUE_HEAD] = M_QUEUE_BASE

# No local variables for the fun and realism
def cpu_cycle(reg, mem):
    reg[C_IR] = reg[C_PC]
    reg[C_PC] += 1

    # decode_execute(reg, mem, reg[C_IR])

    # Scheduler calls
    # Check queue
    # Save/load if needed
    save_process(reg, mem)
    enqueue(reg, mem)
    dequeue(reg, mem)
    load_process(reg, mem)

def padded_hex(n):
    return hex(n)[2:].zfill(4) if n != 0xFFFF else "----"

def hexdump(src):
    for i in range(0, len(src), 8):
        print("\033[7m" if i % 32 == 0 else "\033[0m", end="")
        print(f"{padded_hex(i)}-{padded_hex(i+7)}:", " ".join(padded_hex(src[i]) for i in range(i, i+8)))
    print("\033[0m", end="")

memory = init_memory()

start_process(registers, memory, range(4))
start_process(registers, memory, range(8))
start_process(registers, memory, range(12))
start_process(registers, memory, range(16))
dequeue(registers, memory)
load_process(registers, memory)
hexdump(memory)
hexdump(registers)
while input("> ") == "y":
    cpu_cycle(registers, memory)
    hexdump(memory)
    hexdump(registers)
