# Instruction set
# 00000000 00000000 00000000
# opcode   r1       r2/immediate
# 
# Categories
# 0X control
# 1X registers and memory
# 2X ALU
# 
# Control
# 00 nop
# 01 halt
# 02 jump
# 03 jump if zero, reg, addr
# 04 jump it not zero, reg, addr
# 
# registers and memory
# 10 read reg, reg_out, reg_in
# 11 write reg, reg_out, reg_in
# 12 write reg immediate, reg_out, immediate
# 13 read mem, reg_out, mem_in
# 14 write mem, reg_out, mem_in
# 15 write mem immediate, mem_out, immediate
#
# ALU
# 30 add, reg1, reg2
# 31 add immediate, reg1, reg2
# 32 mul, reg1, reg2
# 33 mul immediate, reg1, reg2
# 34 and, reg1, reg2
# 35 or, reg1, reg2
# 36 not, reg1
# 37 xor, reg1, reg2
# 38 shift left, reg1, reg2
# 39 shift left immediate, reg1, reg2
# 3a shift right, reg1, reg2
# 3b shift right immediate, reg1, reg2
# 3c div, reg1, reg2
# 3d mod, reg1, reg2
