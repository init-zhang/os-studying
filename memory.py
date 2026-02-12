from constants import *

def init_memory():
    memory = [0xFFFF] * 256
    memory[M_PROCESS_LIST] = 0
    memory[M_QUEUE_TAIL] = M_QUEUE_BASE
    memory[M_QUEUE_HEAD] = M_QUEUE_BASE
    return memory
