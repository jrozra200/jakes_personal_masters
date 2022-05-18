# Week 4 - Memory

## Lecture Notes

- Hexidecimal: 16 digits
    - 0 1 2 3 4 5 6 7 8 9 A B C D E F
    - Base-16
    - FF = (15 * 16) + (15 * 1) = 255
    - 11111111 = 255 (Binary)
    - Hexidecimal numbers are started with `0x` (i.e. `0xA` or `0x1A`)
- Pointer: variable that stores the specific byte that a variable is stored
    - `int *p = &n;`
    - `int` tells the computer what type of variable we are pointing to, then 
    `*` to tell it that `p` is a pointer, and `&` to tell it that we want the 
    address of `n`
    - To print the pointer, you need to use `%p`
- Dynamic memory allocation
    - `malloc`: lock a block of ram for something
    - `free`: give a block of ram back
- `valgrind`: checks out the memory usage of your code
- [Binky pointer fun](https://www.youtube.com/watch?v=5VnDaHBi8dM&list=PL266A3129CAE45C0A&index=1)
    
~~~ Stopped at 1:58:08