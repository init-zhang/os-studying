PROCESS_LIST_MAX_INDEX = 64
# Process size = 8,16,32 = 56 spaces
PROCESS_SIZE = 56
PROCESS_CONTEXT_SIZE = 8
PROCESS_DATA_SIZE = 16
PROCESS_CODE_SIZE = 32


# Memory
memory = [0] * 1024
# CPU registers
C_PC = 0
C_IR = 1
C_MAR = 2
C_MDR = 3
C_ACC = 4
C_R0 = 5
C_R1 = 6
C_R2 = 7
cpu = [0] * 8

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
