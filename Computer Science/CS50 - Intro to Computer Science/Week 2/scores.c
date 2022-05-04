# include <stdio.h>

int main(void)
{
    // An array that stores 3 integers
    int scores[3];
    
    scores[0] = get_int("Score: ");
    scores[1] = 73;
    scores[2] = 33;
    
    printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
}