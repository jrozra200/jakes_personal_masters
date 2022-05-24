# Week 5 - Data Structures

## Lecture Notes

- Search runtime: `O(log n)`; `Ω(1)`
- Insert runtime: `O(n)`; `Ω(1)`
- Linked list: linking bytes in memory so you don't have to move data around
    - Search runtime: `O(n)`; `Ω(1)`
    - Insert runtime: 
        - `O(n)` (if we want to maintain sorted order)
        - `O(1)` (if we don't want to maintain sorted order)
        - `Ω(1)`
- Binary search tree: linking bytes in memory with two pointers (left and right)
    - Search runtime: 
        - `O(log n)` (if the tree is balanced); 
        - `O(n)` (if the tree is unbalanced); 
        - `Ω(1)`
    - Insert runtime: 
        - `O(log n)` (if the tree is balanced); 
        - `O(n)` (if the tree is unbalanced); 
        - `Ω(1)`
- Hash tables: an array of linked lists
    - Search runtime: 
        - `O(n)`
        - `Ω(1)`
- Tries: Tree with constant time lookup, even with massive dataset
    - Array of Arrays
    - Search runtime:
        - `O(1)`
        - `Ω(1)`
- Abstract data structures: 
    - Queues
        - First in, first out (FIFO)
        - enqueue: add to the queue
        - dequeue: remove from the queue
        - Can be implemented with a linked list
    - Stacks
        - Last in, first out (LIFO)
        - Can be implemented with a linked list
        - push onto the stack
        - pop off of the stack

### Tries Code

```{c}
typedef struct node
{
    bool is_word;
    struct node *children[SIZE_OF_ALPHABET];
}
node;
```

### Hash Table Code

```{c}
typedef struct node
{
    char word[LONGEST_WORD + 1];
    struct node *next;
}
node;

node *hash_table[NUMBER_OF_BUCKETS];
```

### Binary Search Tree Code

```{c}
typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
}
node;

bool search(node *tree, int number)
{
    if(tree == NULL)
    {
        return false;
    }
    else if (number < tree->number)
    {
        return search(tree->left, number);
    }
    else if (number > tree->number)
    {
        return search(tree->right, number);
    }
    else
    {
        return true;
    }
}
```

### Linked List Code

```{c}
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(void)
{
    node *list = NULL;

    node *n = malloc(sizeof(node));
    
    if (n != NULL)
    {
        n->number = 1;
        n->next = NULL;
    }
    
    list = n;
}
```