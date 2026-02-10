# Memory
# 0-31 OS and scheduler
# 15 Current PID
# 16 Queue tail
# 17 Queue head
# 18-23 Process queue
# 24 Next free PID
# 25-31 Process list
# 32-1023 Processes
M_CURRENT_PID = 15
M_QUEUE_TAIL = 16
M_QUEUE_HEAD = 17
M_QUEUE_BASE = 18
M_QUEUE_END = 23
M_PROCESS_LIST = 24
M_PROCESSES = 32

def init_memory():
    memory = [0xFFFF] * 256
    memory[M_PROCESS_LIST] = 0
    memory[M_QUEUE_TAIL] = M_QUEUE_BASE
    memory[M_QUEUE_HEAD] = M_QUEUE_BASE
    return memory
