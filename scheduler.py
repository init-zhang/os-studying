# Memory
# 0-23 OS and scheduler
# 24 Queue tail
# 25 Queue head
# 26-31 Process queue
# 32 Next free PID
# 33-63 Process list
# 64-1023 Processes
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

# Omit pid parameter in the future
def enqueue(reg, mem, pid):
    mem[mem[M_QUEUE_TAIL]] = pid
    mem[M_QUEUE_TAIL] += 1
    if mem[M_QUEUE_TAIL] > M_QUEUE_END:
        mem[M_QUEUE_TAIL] = M_QUEUE_BASE

def dequeue(reg, mem):
    pid = mem[M_QUEUE_HEAD]
    mem[M_QUEUE_HEAD] += 1
    if mem[M_QUEUE_HEAD] > M_QUEUE_END:
        mem[M_QUEUE_HEAD] = M_QUEUE_BASE
    return pid

# No local variables for the fun and realism
def cpu_cycle(reg, mem):
    reg[C_IR] = reg[C_PC]
    reg[C_PC] += 1

    # decode_execute(reg, mem, reg[C_IR])

    # Scheduler calls
    # Check queue
    # Save/load if needed

def padded_hex(n):
    return hex(n)[2:].zfill(4) if n != 0xFFFF else "----"

def hexdump(src):
    for i in range(0, len(src), 8):
        print(f"{padded_hex(i)}-{padded_hex(i+7)}:", " ".join(padded_hex(src[i]) for i in range(i, i+8)))

memory = init_memory()

start_process(registers, memory, 0)
start_process(registers, memory, 0)
start_process(registers, memory, 0)
start_process(registers, memory, 0)
enqueue(registers, memory, 1)
enqueue(registers, memory, 1)
enqueue(registers, memory, 2)
enqueue(registers, memory, 3)
enqueue(registers, memory, 1)
enqueue(registers, memory, 1)
dequeue(registers, memory)
dequeue(registers, memory)
dequeue(registers, memory)
enqueue(registers, memory, 10)
hexdump(memory)
