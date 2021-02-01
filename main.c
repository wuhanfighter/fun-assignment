// module imports
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

// main function
int main() {

    // variable declaration
    int choice, number, counter, factorial=1;
    float area, radius, width, length, perimeter;
    double pi=3.14;

    // show choices while true
    while (1) { 
        printf("1. Area of Circle\n");
        printf("2. Area and Perimeter of Rectangle\n");
        printf("3. Odd and Even for Number\n");
        printf("4. Factorial for Number\n");
        printf("5. FizzBuzz\n");
        printf("\n");
        printf("Your choice: ");
        scanf("%d", &choice); 
        system("clear"); 

        // test choice and compare multiple cases
        switch (choice) { 
            // calculate area of circle
            case 1: 
                printf("You have choosen to calculate Area of Circle\n");
                printf("\n");
                printf("Enter your desire radius: ");
                scanf("%f", &radius);
                system("clear");

                area = pi * radius;
                printf("Area of circle is %.2f\n", area);
                printf("\n");

                break;
            // calculate area and perimeter of rectangle
            case 2:
                printf("You have choosen to calculate Area and Perimeter of Rectangle\n");
                printf("\n");
                printf("Enter your desire width: ");
                scanf("%f", &width);
                printf("Enter your desire length: ");
                scanf("%f", &length);
                system("clear");

                area = width * length;
                perimeter = 2*(length + width);
                printf("Area of rectangle is %.2f\n", area);
                printf("Perimeter of rectangle is %.2f\n", perimeter);
                printf("\n");

                break;
            // determined odd and even number
            case 3: 
                printf("You have choosen to determined Odd and Even for Number\n");
                printf("\n");
                printf("Enter your desire number: ");
                scanf("%d", &number);
                system("clear");

                if (number%2 == 0) { 
                    printf("%d is an Even number\n", number);
                    printf("\n");
                } else { 
                    printf("%d is an Odd number\n", number);
                    printf("\n");
                }

                break;
            // determined factorial number
            case 4: 
                printf("You have choosen to determined Factorial for Number\n");
                printf("\n");
                printf("Enter your desire number: ");
                scanf("%d", &number);
                system("clear");

                for (counter=1; counter <= number; counter++) {
                    factorial *= counter;
                }
                printf("Factorial of %d is %d\n", number, factorial);
                printf("\n");

                break;
            // determined fizzbuzz number
            case 5: 
                printf("You have choosen to determined FizzBuzz for Number\n");
                printf("\n");
                printf("Enter your desire number: ");
                scanf("%d", &number);
                system("clear");

                if (number>=1 && number<=100) {
                    if ((number%3 == 0) && (number%5 == 0)) {
                        printf("FizzBuzz\n");
                        printf("\n");
                    } else if(number%3==0){
                        printf("Fizz\n");
                        printf("\n");
                    } else if(number%5==0) { 
                        printf("Buzz\n");
                        printf("\n");
                    } else {
                        printf("%d\n", number);
                        printf("\n");
                    }
                } else { 
                    printf("Number limited from 1 to 100\n");
                    printf("\n");
                }

                break;
            // default case
            default:
                printf("Invalid input choice\n");
                printf("\n");
        }
    }
}