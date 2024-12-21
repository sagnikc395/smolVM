// memory storage

const MEMORY_MAX: usize = 1 << 16;

//general purpose registers to perform any calculations

#[derive(Debug, Copy, Clone, PartialEq)]
enum Register {
    RR0 = 0,
    RR1,
    RR2,
    RR3,
    RR4,
    RR5,
    RR6,
    RR7,
    RPC, //program counter
    RCOND,
    RCOUNT,
}
#[derive(Debug, Copy, Clone, PartialEq)]
enum Opcodes {
    OPBR = 0, //branch
    OPADD,    //add
    OPLD,     // load
    OPST,     // store
    OPJSR,    /* jump register */
    OPAND,    /* bitwise and */
    OPLDR,    /* load register */
    OPSTR,    /* store register */
    OPRTI,    /* unused */
    OPNOT,    /* bitwise not */
    OPLDI,    /* load indirect */
    OPSTI,    /* store indirect */
    OPJMP,    /* jump */
    OPRES,    /* reserved (unused) */
    OPLEA,    /* load effective address */
    OPTRAP,   /* execute trap */
}

#[derive(Debug, Copy, Clone, PartialEq)]
enum ConditionFlags {
    FLPOS = 1 << 0, // p
    FLZRO = 1 << 1, //z
    FLNEG = 1 << 2, // N
}

fn main() {
    let memory: [u16; MEMORY_MAX] = [0; MEMORY_MAX];
}
