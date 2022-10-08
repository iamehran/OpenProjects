#include <stdio.h>
#include<stdio.h>
#include <ctype.h>
#include <string.h>
int comparePriority(char op1, char op2);


#define  MAX  20
typedef  char  item_type;

/*stack */
typedef struct s_tag
{
int  top;
item_type ele[MAX];
} Stack;

/*function to initialize a stack
  input: stack pointer
*/
void initialize(Stack *sp)	
{	
sp->top = -1;	/*set top to initial value */
}	


/*function to push an item onto  a stack
  input: stack pointer sp, item to be pushed x
*/
void push(Stack *sp, item_type  x)	
{	
if  (full(sp))	/*stack is full */
	printf("\nStack Overflow");	/*display message*/
else	/*otherwise*/
	sp->ele[++sp->top] = x;	/*first increment top, then insert */
}	


/*function to pop an item from  a stack
  input: stack pointer sp
  output: the popped item
*/
item_type pop(Stack *sp)	
{	
item_type  x;	/*to hold popped item*/
	
if  (empty(sp))	/*stack is empty */
	printf("\nStack Underflow");	/*display message*/
else	/*otherwise*/
	x = sp->ele[sp->top--];	/*get top most item, then decrement top */
return x;	/*return deleted item*/
}	


/*function to check whether a stack is full or not
  input: stack pointer sp
  output: 1(true) - if stack is full
   0(false) - is stack is not full
*/
int  full(Stack *sp)	
{	
if  (sp->top == MAX-1)	/* stack is full */
	return 1;	/*return TRUE*/
else	/*stack is not full*/
	return 0;	/*return FALSE*/
}	


/*function to check whether a stack is empty or not
  input: stack pointer sp
  output: 1(true) - if stack is empty
   0(false) - is stack is not empty*/
int  empty(Stack *sp)	
{	
if  (sp->top == -1)	/* stack is empty */
	return 1;	/*return TRUE*/
else	/*stack is not empty*/
	return 0;	/*return FALSE*/
}	

/* Fucntion to return the value of count
    input: the stack pointer sp
    output: the size of stack
*/
int   size(Stack  *sp)
{
	return sp->top + 1;
}

/*function to get the top most element from stack
  without removing it
*/
item_type peek(Stack *sp)
{
	if (!empty(sp) )
		return sp->ele[sp->top];
	else 
		return 0;
}
//function to convert inFix expression to postFix expression
void inToPost(char *inFix, char *postFix)
{
	char symbol, topOperator;
	char temp[2] = {'\0', '\0'};
	Stack s;

	*postFix = '\0'; //initialize the resultant string
	initialize(&s);

	while(*inFix) //traverse the infix string
    {
        symbol = *inFix;

        if (isalnum(symbol)) //symbol is operand
        {
            temp[0] = symbol;
            strcat(postFix, temp);//append operand to postfix string
        }
        else //symbol is operator
        {
            topOperator = peek(&s); //get top of the stack operator

            while(!empty(&s) && comparePriority(symbol, topOperator) == -1)
            {
                temp[0] = pop(&s);
                strcat(postFix, temp);
            }
            push(&s, symbol); //push current operator on the stack
        }
        ++inFix;
    }
    //inFix string ends
    while( !empty(&s))
    {
        temp[0] = pop(&s);
        strcat(postFix, temp);
    }
}


/* Function to compare priority of two operators
   input: two operators
   output: 0 - same priority; 1 - op1 has higher priority; -1 op2 has higher priority
*/
int comparePriority(char op1, char op2)
{
	char oper[2][3] = { {'*', '/', '%'}, {'+', '-', 0} };
	int row1, row2, i, j;

	for (i=0; i<2; ++i)
    {
        for (j=0; j<3; ++j)
        {
            if (op1==oper[i][j]) row1 = i;
            if (op2==oper[i][j]) row2 = i;

        }
    }

    if (row1 == row2) return 0;
    if (row1 < row2) return 1;
    if (row1 > row2) return -1;
}
int main()
{
	char inFix[20], postFix[20];

	printf("Enter expression in infix: ");
	gets(inFix);

	inToPost(inFix, postFix);

	printf("The equivalent postfix expression is: %s \n", postFix);

	return 0;
}
