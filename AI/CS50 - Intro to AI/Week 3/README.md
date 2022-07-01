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
- Simulated Annealing: 
    - early on in the simulation, more likely to accept a neighbor that is worse
    - later on in the simulation, less likely to accept a neighbor that is worse
    - Pseudo-code:
    
``` python
function simulated-annealing(problem, max):
    current = initial state of problem
    for t = 1 to max:
        T = temperature(t)
        neighbor = random neighbor of current
        delta_E = how much better is neighbor than current
        if delta_E > 0:
            current = neighbor
        with probability e ^ delta_E/t set current = neighbor
    
    return current
```

