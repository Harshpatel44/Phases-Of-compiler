# Phases-Of-compiler
These Repository shows the Compilation Stages of a C program with a User Interface


The four stages for a C program to become an executable are the following:

1.Pre-processing
2.Compilation
3.Assembly
4.Linking


1. Preprocessing
This is the first stage of compilation process where preprocessor directives (macros and header files are most common) are expanded. To perform this step gcc executes the following command internally.

[root@host ~]# cpp helloworld.c > helloworld.i

2. Compilation
In this phase compilation proper takes place. The compiler (ccl) translates helloworld.i into helloworld.s. File helloworld.s contains assembly code. You can explicitly tell gcc to translate helloworld.i to helloworld.s by executing the following command.

[root@host ~]# gcc -S helloworld.i

3. Assembly
Here, the assembler (as) translates helloworld.s into machine language instructions, and generates an object file helloworld.o. You can invoke the assembler at your own by executing the following command.

[root@host ~]# as helloworld.s -o helloworld.o

4. Linking
This is the final stage in compilation of "Hello World!" program. This phase links object files to produce final executable file.
