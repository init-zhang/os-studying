from cpu_registers import CPURegisters
from pcb import ProcessControlBlock

class Scheduler:
    def __init__(self, cpu, memory, blah):
        self.cpu = cpu
        self.memory = memory
        self.blah = blah

    def load_process(self, process):

STACK_MAX_INDEX = 8
HEAP_MAX_INDEX = 32
PROCESS_LIST_MAX_INDEX = 64
# Process size = 8,16,32 = 56 spaces
PROCESS_SIZE = 56
PROCESS_CONTEXT_SIZE = 8
PROCESS_DATA_SIZE = 16
PROCESS_CODE_SIZE = 32

memory = [0] * 1024  # 64-bit integer -> 8 bytes, 1024 of 8 bytes
stack_index = 0
heap_index = STACK_MAX_INDEX
process_list_index = HEAP_MAX_INDEX
process_index = PROCESS_LIST_MAX_INDEX

def append_to_stack(memory, value):
    memory[stack_index] = value
    stack_index += 1

def top_from_stack(memory):
    return memory[stack_index-1]

def pop_from_stack(memory):
    stack_index -= 1
    return memory[stack_index]

def add_process(memory, context, data, code):
    # Write process index to process index list
    # Write context, data, and code, with respects to their sizes
    # Update process index (process size) and process list index

    memory[process_list_index] = process_index
    
    for i in range(PROCESS_CONTEXT_SIZE):
        memory[process_index + i] = context[i]

    for i in range(PROCESS_DATA_SIZE):
        memory[process_index + PROCESS_CONTEXT_SIZE + i] = context[i]

    for i in range(PROCESS_CODE_SIZE):
        memory[process_index + PROCESS_CONTEXT_SIZE + PROCESS_DATA_SIZE + i] = context[i]

    process_list_index += 1
    process_index += PROCESS_SIZE

print(memory)

print(memory)