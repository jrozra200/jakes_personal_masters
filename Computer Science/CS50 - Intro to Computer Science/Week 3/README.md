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

~~~ Paused at 49:00