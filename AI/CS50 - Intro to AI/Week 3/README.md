# Week 3 - Optimization

## Lecture Notes

- Optimization: Choosing the best option from a set of options
- Local search: Search algorithms that maintain a single node and searches by 
moving to a neighboring node 
    - Hill climbing: Consider the neighbors and pick the options that is higher 
    (if you are trying to maximize). Keep going until both neighbors are lower 
    than your current state. Do the opposite if you are trying to minimize. 
    - Pseudo-code:

``` python
function hill-climb(problem):
    current = initial state of problem
    repeat: 
        neighbor = highest value neighbor of current
        if neighbor is not better than current:
            return current
        current = neighbor

```
    - Variants: 
        - Steepest Ascent: choose the highest valued neighbor
        - Stochastic: choose randomly from one of the better neighbors
        - First-choice: pick the first neighbor that is higher valued
        - Random-restart: conduct hill climbing multiple times
        - Local beam search: chooses the k-highest valued neighbors