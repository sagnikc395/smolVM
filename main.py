from enum import Enum


# LC-3 memory locations i.e 128kb 
MEMORY_MAX = 1 << 16

## total locations in memory
MEMORY = [None] * MEMORY_MAX 

# registers -> 8 general purpose registers (R0-R7), 1 PC (program counter) , 1 condition flags register

class Register(Enum):
    R_R0 = 0
    R_R1 = 1
    R_R2 = 2
    R_R3 = 3
    R_R4 = 4
    R_R5 = 5
    R_R6 = 6
    R_R7 = 7
    R_PC = 8 # program counter
    R_COND = 9 # conditional flag

R_COUNT = 10 # pin count 

    
# store the registers in an array
REG = [None]* R_COUNT

# instruction set opcode repr one task that the CPU knows how to do
# in this only 16 opcodes in LC-3. Everything that a computer can calculate in some seq of these simple instructions.

class InstructionSet(Enum):
    OP_BR = 0 # branch
    OP_ADD = 1 # add
    OP_LD = 2 # load
    OP_ST = 3 # store
    OP_JSR = 5 #jump register
    OP_AND = 6 # bitwsie and
    OP_LDR = 7 # load the register
    OP_STR = 8 # store the register
    OP_RTI = 9 # unused
    OP_NOT = 10 # bitwise not
    OP_LDI = 11 # load indirect
    OP_STI = 12 # store indirect
    OP_JMP = 13 # jump
    OP_RES = 14 # reserved(unused)
    OP_LEA = 15 # load effective address
    OP_TRAP = 16 # exec trap
    

## condition flags provide ifno about the most recently executed calculation. This allows programs to check logical conditions ushc as if (x> 0 ) {...}
# each CPU has a variety of condition flags to signla various situations.

class ConditionFlags(Enum):
    FL_POS = 1 << 0
    FL_ZRO = 1 << 1
    FL_NEG = 1 << 2



def main():
    REG[Register.R_COND] = ConditionFlags.FL_ZRO

    # PROGRAM COUNTER TO START POSN
    # setting 0x3000 as the default
    PC_START = hex(0x3000)

    REG[Register.R_PC] = PC_START

    running = 1

    for(running):
        # fetch the data
        # TODO
    


if __name__ == '__main__':
    main()
    
