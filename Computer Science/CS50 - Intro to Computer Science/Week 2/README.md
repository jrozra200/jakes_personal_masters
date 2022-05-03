# Week 2 - Arrays

## Lecture Notes

- `make` uses `clang`
- `clang -o hello hello.c` is the same as `make hello`
- To use the `cs50.h` library, you need to use `clang -o hello hello.c -l cs50` 
    - Need to go back and reinstall `cs50.h` to see if this works for me
    - `make` does this automatically, but not locally. Still need to work that out.
- Compiling your code is doing the following automatically all at once:
    1. **Preprocessing**: finds the files for `#include` on the hard drive and 
    brings the functions into your program
    2. **Compiling**: converts `c` code into `assembly` language instructions
        - Assembly language is as close to 0s and 1s you can get; computer 
        instructions
    3. **Assembling**: `assembly` languague is turned into 0s and 1s 
    4. **Linking**: stitches all of the programs into a single file of 0s and 1s
- `debugging`
    - Create outputs with `printf` to output variables as the program runs.
    - VS Code has a nice debugger where you can set break points to "step 
    through" your code and see values of variables throughout. 
    - "Rubber Duck" debugging is talking through your code, step-by-step, with 
    an inanimate object
    
~~~ Stopped at 35:53