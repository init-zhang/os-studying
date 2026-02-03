PROCESS_LIST_MAX_INDEX = 64
# Process size = 8,16,32 = 56 spaces
PROCESS_SIZE = 56
PROCESS_CONTEXT_SIZE = 8
PROCESS_DATA_SIZE = 16
PROCESS_CODE_SIZE = 32


# Memory
# 0-31 OS and scheduler
# 32 Next free PID
# 33-63 Process list
# 64-1023 Processes
M_PROCESS_LIST = 32
M_PROCESSES = 64
memory = [0] * 256

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
    process_base = M_PROCESSES+(pid-1)*32
    mem[M_PROCESS_LIST+pid] = process_base
    mem[process_base + PCB_PID] = pid
    mem[process_base + PCB_PC] = process_base + PC_BASE
    # Load asm into binary, then into asm
    print(pid, process_base)

# Method should not require pid parameter
# Should be known in memory
def save_process(reg, mem, pid):
    process_base = mem[M_PROCESS_LIST+pid]
    mem[process_base + PCB_PC] = reg[C_PC]
    mem[process_base + PCB_ACC] = reg[C_ACC]
    mem[process_base + PCB_R0] = reg[C_R0]
    mem[process_base + PCB_R1] = reg[C_R1]
    mem[process_base + PCB_R2] = reg[C_R2]

def load_process(reg, mem, pid):
    process_base = mem[M_PROCESS_LIST+pid]
    reg[C_PC] = mem[process_base + PCB_PC]
    reg[C_ACC] = mem[process_base + PCB_ACC]
    reg[C_R0] = mem[process_base + PCB_R0]
    reg[C_R1] = mem[process_base + PCB_R1]
    reg[C_R2] = mem[process_base + PCB_R2]

# No local variables for the fun and realism
def cpu_cycle(reg, mem):
    reg[C_IR] = reg[C_PC]
    reg[C_PC] += 1

    # decode_execute(reg, mem, reg[C_IR])

    # Scheduler calls
    # Check queue
    # Save/load if needed

def padded_hex(n):
    return hex(n)[2:].zfill(4) if n else "...."

def hexdump(src):
    for i in range(0, len(src), 8):
        print(f"{padded_hex(i)}-{padded_hex(i+7)}:", " ".join(padded_hex(src[i]) for i in range(i, i+8)))

start_process(registers, memory, 0)
start_process(registers, memory, 0)
start_process(registers, memory, 0)
start_process(registers, memory, 0)
hexdump(memory)
load_process(registers, memory, 2)
hexdump(registers)
cpu_cycle(registers, memory)
hexdump(registers)
save_process(registers, memory, 2)
hexdump(memory)
