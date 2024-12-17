// memory storage

const MEMORY_MAX: usize = 1 << 16;

//general purpose registers to perform any calculations

#[derive(Debug, Copy, Clone, PartialEq)]
enum Register {
    R0 = 0,
    R1,
    R2,
    R3,
    R4,
    R5,
    R6,
    R7,
    PC,
    COND,
    COUNT,
}

fn main() {
    let memory: [u16; MEMORY_MAX] = [0; MEMORY_MAX];
}
