## Virtual Machine 

- VM is a program that will act like a computer. 
- It will simulate a CPU along with a few other hardware components -> allowing to perform arithmatic, read and write to memory, interact with I/O devices


- Some VMs are designed to reproduce the behaviour of some particular computer, like a NES.
- Other VMs dont act like any real computer and are entirely made up! This is done primarily to make software development easier.

- A VM could offer a standard platform which provided portability for all of them. Instead of rewriting a program in different dialects of assembly for each CPU architecture, we would need to write the small VM programme in each assembly language.

- Similarly JVM is a good example, once JVM is implemented on a new device, the only cost is the overhead of the VM itself and the further abstraction from the machine.

- VMs are also useuful for executing code in a secure of isolated way. One application of this is garbage collection. 
No trivial way to implement automatic GC on top of C/C++ since a program cannot see its own stack or variable
