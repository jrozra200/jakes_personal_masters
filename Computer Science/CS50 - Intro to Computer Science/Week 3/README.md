# Week 3 - Algorithms

## Lecture Notes

- As n gets large, the order of `N/2` is approximately the same as `N`
- Common run times:
    - `O(n<sup>2<\sup>)`
    - `O(n log n)`
    - `O(n)`
    - `O(log n)`
    - `O(1)`
- `Ω` (Omega) is lower bound
- `Θ` (Theta) is when the upper and lower bound are equal
- Linear Search: Look one by one
    - Psuedo code: 
        - For each door, one by one, look for 0
            - If 0 is present, return TRUE
        - return FALSE
    - Lower level psuedo code:
        - For i from 0 to n-1:
            - If number behind doors[i]
                - Return true
            - Return false 
    - Run time: 
        - `O(n)`
        - `Ω(1)`
- Binary Search: numbers are sorted; go to the middle and continue to go the 
middle in the direction of the number (up or down)
    - Psuedo code: 
        - If no doors
            - Return false
        - If the number is behind the middle door
            - Return true
        - Else if the number is less than the middle door 
            - Search lower half
        - Else if the number is greater than the middle door
            - Search upper half 
    - Lower level psuedo code:
        - If no doors
            - Return false
        - If the number is behind doors[middle]
            - Return true
        - Else if the number < doors[middle]
            - Search doors[0] through doors[middle]
        - Else if the number is greater than the middle door
            - Search doors[middle] through doors[n]
    - Run time:
        - `O(log n)`
        - `Ω(1)`
- data structures: create your own data type with `typedef struct`
- Selection Sort: Select the smallest and place it in the right place
    - Psudeo code:
        - For i from 0 to n-1
            - Find smallest number between numbers[i] and numbers[n-1]
            - Swap smallest number with numbers[i]
    - Run time: 
        - `O(n<sup>2<\sup>)`
        - `Ω(n<sup>2<\sup>)`
- Bubble Sort: Compare the first two numbers and swap them if they are misorders
    - Psuedo code: 
        - Repeat n-1 times
            - For i from 0 to n-2
                - If numbers[i] and numbers[i+1] are out of order, swap them
            - If no swaps 
                - Quit
    - Run time:
        - `O(n<sup>2<\sup>)`
        - `Ω(n)`
- Sort visualization: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html

    

~~~ Paused at 49:00