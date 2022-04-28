# Week 1

## Lecture Notes

- **Correctness**: code needs to be correct
- **Design**: is your code efficient and well formulated?
- **Style**: punctuation, spacing, indentation, etc.
- **Integrated Development Environment (IDE)**: The program that interprets your 
code and changes it to 0s and 1s
    - visual studio
    - **compiler**: takes source code to 0s and 1s
- cli commands:
    - `make`: makes a c program; not a compiler - it finds the compiler for me
    - `rm`: removes a file
    - `ls`: lists files in a directory
    - `cp`: copy
    - `mkdir`: make directory
    - `mv`: Move/rename
    - `rmdir`: remove directory
    - `cd`: change directory
        - `..`: parent directory
        - `~` OR ` ` (nothing, just `cd` by itself): default directory
    - `control+l` OR `clear`: clear the terminal output
- `c` commands:
    - `printf()`: to print to screen
    - `get_string()`: to get a string from user (from the cs50.h library)
    - types:
        - `bool`
        - `char`
        - `double`
        - `float`
        - `int`
        - `long`
        - ...
    - cs50 functions:
        - `get_char`
        - `get_int`
        - `get_string`
        - ...
    - format codes:
        - `%c`: char
        - `%f`: float/double
        - `%li`: long
        - `%i`: integer
    - syntactic sugar:
        - `counter += 1;` == `counter++` == `counter = counter + 1`
        - `counter -= 1;` == `counter--` == `counter = counter - 1`
    - `const`: turn a variable into a constant; they cannot be changed after 
    they are created.
        - usually represented with a variable named in ALL CAPS
- **Magic numbers**: numbers in your code that are hard coded that could/should 
be a variable instead.
- **floating point impercision**: In languages like `c`, they are approximating 
decimals after a certain point.
- January 19, 2038 is when the number of seconds since the epoch goes past 32 
bits

    
