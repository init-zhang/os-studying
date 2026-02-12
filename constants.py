# CPU registers
C_PC = 0
C_IR = 1
C_MAR = 2
C_MDR = 3
C_ACC = 4
C_R0 = 5
C_R1 = 6
C_R2 = 7

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
