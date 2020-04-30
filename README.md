<h1>Phases of C language compiler<h1>
  <h3>These Repository shows the Compilation Stages of a C program with a User Interface. </h3>
<h2>How to use:</h2> <br>
1. Enter the path of the C language file (.C) in Entry Box <br>
2. Click on Pre-processing Button <br>
3. Then Compilation , Assembly & finally Linking <br>
4. As you Click , You will find the content <br>
5. The Files of Preprocessing, Compiling , Assembly are also saved in the path<br>
<br>
<h2> Program stages </h2>
The four stages for a C program to become an executable are the following:<br>
1. Pre-processing<br>
2. Compilation<br>
3. Assembly<br>
4. Linking<br>

<h2>Working with explaination</h2>
<b>1. Preprocessing</b>
<p>This is the first stage of compilation process where preprocessor directives (macros and header files are most common) are expanded. To perform this step gcc executes the following command internally.</p><br>
<i>[root@host ~]# cpp helloworld.c > helloworld.i</i><br>
<br>
<b>2. Compilation</b>
<p>In this phase compilation proper takes place. The compiler (ccl) translates helloworld.i into helloworld.s. File helloworld.s contains assembly code. You can explicitly tell gcc to translate helloworld.i to helloworld.s by executing the following command.</p>
<br>
<i>[root@host ~]# gcc -S helloworld.i</i><br>
<br>
<b>3. Assembly</b>
<p>Here, the assembler (as) translates helloworld.s into machine language instructions, and generates an object file helloworld.o. You can invoke the assembler at your own by executing the following command.</p>
<br>
<i>[root@host ~]# as helloworld.s -o helloworld.o</i><br>
<br>
<b>4. Linking</b>
<p>This is the final stage in compilation of "Hello World!" program. This phase links object files to produce final executable file.</p><br>
