Useless is a stupid programming language. It is similar to brainf***, where you manipulate a variable with arithmetic.<br>The key variable is called TheHolyChar.<br>Line numbers are defined by the line number multiplied by 10. For example
```
10 +23
20 !
```
This writes a single 'A' to a .c file and compiles it, as TheHolyChar starts at 42 and you can control it with + and -

Other features:

Compile time randomness: ?min_max is used<br>; can set TheHolyChar to a specific number, but not consecutively<br>Macros: #include filename is used to include a .useh file, which contains macros and functions defined like so:
```
MACR STDIO #include <stdio.h>
MACR MAIN int main() {
FUNC PRINT printf(%);
MACR END return 0;}
```
This creates macros for STDIO MAIN PRINT and END, which can be used like this

```
10 #include filename
20 &=STDIO
30 ;10
40 &=MAIN
50 &PRINT<"Hello, World!\n">
60 &=END
70 !
```

! is for EOF (End of file) and is required for the code to run.<br>Macros are accessed with &=. Parameters in macros can be used with % and then used by \<parameters\><br>
Please share this to everyone you know!
