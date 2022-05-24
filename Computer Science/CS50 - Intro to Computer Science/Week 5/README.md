# Week 5 - Data Structures

## Lecture Notes

- Search runtime: `O(log n)`; `Ω(1)`
- Insert runtime: `O(n)`; `Ω(1)`
- Linked list: linking bytes in memory so you don't have to move data around

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

~~~ Stopped at 51:22