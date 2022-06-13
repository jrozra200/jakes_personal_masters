# Week 0 - Search

## Lecture Notes

- agent: entity that perceives its environment and acts upon that environment
- state: a configuration of the agent and its environment
    - initial state: the state in which the agent begins
- actions: choices that can be made in a state
    - `Action(s)` returns the set of actions that can be executed in state `s`
- Transition model: what state we get from taking an action
    - `Result(s, a)` returns the state we get from performing action `a` in
    state `s`
- State space: all possible states reachable by any actions
    - Can be represented by a graph
- Goal test: way to determine whether a given state is a goal state
- Path cost: numerical cost associate with a given path
- Search problems have:
    - Initial State
    - Actions
    - Transition Model
    - Goal Test
    - Path cost function
- solution: a sequence of actions that will take from the initial state to the 
goal state
- optimal solution: a solution that has the lowest path cost among all solutions
- node: a data structure that keeps track of 
    - a state
    - a parent
    - an action
    - a path cost
- frontier: all the things that we could explore next
- Initial search approach:
    - start with a frontier that contains the initial state
    - repeat:
        - if the frontier is empty, then no solution
        - remove a node from the frontier
        - if that node is a goal state, return the solution
        - expand node, add resulting nodes to the frontier
- Revised search approach:
    - start with a frontier that contains the initial state
    - start with an empty explored set
    - repeat:
        - if the frontier is empty, then no solution
        - remove a node from the frontier
        - if that node is a goal state, return the solution
        - add the node to the explored state
        - expand node, add resulting nodes to the frontier if they aren't 
        already in the frontier or the explored set
- Ways to remove a node from the frontier:
    - depth-first search: expand the deepest node first
        - Stack: last in, first out 
        - as long as your state is finite, you WILL find a solution
        - Won't necessarily find a good solution
    - breadth-first search: expand the shallowest node first
        - queue: first in, first out 
        - Does find the optimal state
        - needs to explore a lot of states to find the optimal solution
- Uninformed search: search strategy that uses no problem-specific knowledge
    - DFS and BFS are examples of this
- Informed search: search strategies that use problem-specific knowledge to find 
solutions more efficiently 
    - Greedy best-first search: search algorithm that expands the node that is 
    closest to the goal, as estimated by a heuristic function `h(n)`
        - `h(n)` estimated cost to goal
        - Will not always find the optimal solution
        - It makes the "best" local solutions, which doesn't always lead to the 
        "best" overall solution
    - A* search: search algorithm that expands node with the lowest value of 
    `g(n) + h(n)`
        - `g(n)` cost to reach node
        - `h(n)` estimated cost to goal
        - Will find an optimal solution if:
            - `h(n)` is admissible (never overestimates the true cost) and,
            - `h(n)` is consistent (for every node `n` and successor `n'` with 
            step cost `c`, `h(n) <= h(n') + c`)
        - A* tends to use a lot of memory
- Heuristic functions:
    - Manhattan distance `h(n)`: how many steps away are you from the goal
- Adversarial Search
    - Minimax:
        - Objectives: 
            - `MAX (X)` wants to maximize the score
            - `MIN (O)` wants to minimize the score
        - Pseudo code:
            - Given a state `s`
                - MAX picks an action `a` in `Actions(a)` that produces the 
                highest value of `Min-Value(Results(s, a))`
                - MIN picks an action `a` in `Actions(a)` that produces the 
                highest value of `Max-Value(Results(s, a))`
            - function `Max-Value(Results(s, a))`:
                - if terminal(state): 
                    - return Utility(state)
                - v = -infinity
                - for every action in Actions(state):
                    - v = Max(v, Min-Value(Results(s, a)))
                - return v
            - function `Min-Value(Results(s, a))`:
                - if terminal(state): 
                    - return Utility(state)
                - v = infinity
                - for every action in Actions(state):
                    - v = Min(v, Max-Value(Results(s, a)))
                - return v
        - Optimizations:
            - Alpha-Beta pruning: track the current highest value (alpha) and 
            lowest (beta) and ignore any branches that are lower or higher, 
            respectively
            - Depth-Limited Minimax: Only look a certain amount of moves ahead 
            and then stop. Requires an evaluation function, which gives you an 
            expected utility from a given state (even of incomplete games). 