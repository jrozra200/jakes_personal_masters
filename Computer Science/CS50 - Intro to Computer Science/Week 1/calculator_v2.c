#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("x: ");
    
    //Prompt user for y
    int y = get_int("y: ");
    
    float z = (float) x / (float) y;
    
    //Output x + y
    printf("%.50f\n", z);
}