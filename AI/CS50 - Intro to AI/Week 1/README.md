# Week 1 - Knowledge

## Lecture Notes

- knowledge-based agents: agents that reason by operating on internal 
representations of knowledge
- sentence: an assertion about the world in a knowledge representation language
- propositional logic: statements about the world
    - `P`, `Q`, `R` are logic statements
    - `¬` (not), `^` (and), `∨` (or), `->` (implication), `<->` (biconditional)

- NOT (`¬`) operator

| `P` | `¬P` |
|-----|------|
| `false` | `true` |
| `true` | `false` |

- AND (`^`) operator

| `P` | `Q` | `P ^ Q` |
|-----|------|--------|
| `false` | `false` | `false` |
| `false` | `true` | `false` |
| `true` | `false` | `false` |
| `true` | `true` | `true` |

- OR (`v`) operator

| `P` | `Q` | `P v Q` |
|-----|------|--------|
| `false` | `false` | `false` |
| `false` | `true` | `true` |
| `true` | `false` | `true` |
| `true` | `true` | `true` |

- IMPLICATION (`->`) operator
    - if `P` is `true`, then `Q` also needs to be `true`
    - if `P` is `false`, then we make no claim about `Q`

| `P` | `Q` | `P -> Q` |
|-----|------|--------|
| `false` | `false` | `true` |
| `false` | `true` | `true` |
| `true` | `false` | `false` |
| `true` | `true` | `true` |

- BICONDITIONAL (`<->`) operator
    - Only `true` when `P` and `Q` are the same

| `P` | `Q` | `P <-> Q` |
|-----|------|--------|
| `false` | `false` | `true` |
| `false` | `true` | `false` |
| `true` | `false` | `false` |
| `true` | `true` | `true` |

- model: assignment of a truth value to every propositional symbol
- knowledge base: a set of sentences known by a knowledge-based agent as true
- entailment: 
    - `α ⊨ β`
    - In every model in which sentence `α` is true, `β` is also true
- inference: the process of deriving new sentences from old ones
- model checking: to determine if `KB ⊨ α`, we need to enumerate all possible 
models; if every model where `KB` is true, `α` is also true, `KB` does entail 
`α`