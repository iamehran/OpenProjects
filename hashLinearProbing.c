#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <time.h>

typedef int iType;
int collCount=0;

iType *createTable(int n);
void show(iType *a, int n);
void generateAndInsertKey(iType *a, int n);
void readAndInsertKey(iType *a, int n);
int hash(iType *a, int n, iType key);
int handleCollision(iType *a, int n, iType key, int pos);
int search(iType *a, int n, iType key);


void main()
{
    iType *a, key;
    int n, pos;

    printf("Enter size of the list: ");
    scanf("%d", &n);

    a = createTable(n);
    //generateAndInsertKey(a, n);  //randomly generate item
    readAndInsertKey(a, n);    //read item from keyboard

    printf("\n\nEnter the item to be searched: ");
    scanf("%d", &key);

    pos = search(a, n, key);
    if (pos != -1)
        printf("Item %d found at index %d\n", key, pos);
    else
        printf("Item not found\n");

    free(a);
    return 0;
}

iType *createTable(int n)
{
    iType *a; int i;
    a = (iType*)malloc(n*sizeof(iType));
    if (a==NULL)
    {
        printf("Memory not allocated\n");
        exit(1);
    }

    //initialize the list
    for(i=0; i<n; ++i)
        a[i] = -1;
    return a;
}

void show(iType *a, int n)
{
    int i;
    printf("List is: ");
    for (i=0; i<n; ++i)
        printf("%d\t", a[i]);
    printf("\n\n");
}

//handling collision by linear probing
int handleCollision(iType *a, int n, iType key, int pos)
{
    while (a[pos] != -1) //collision occurred
    {
        printf("Generated key is: %d, Collision occurred at position: %d, Searching empty position\n", key, pos);
        ++collCount;
        pos = (pos+1)%n; //linear probing
    }
    return pos;
}

int hash(iType *a, int n, iType key)
{
    int pos;
    srand(key);
    pos =  rand()%n;
    if (a[pos] != -1) //it is a collision
        pos = handleCollision(a, n, key, pos);
    return pos;
}

void generateAndInsertKey(iType *a, int n)
{
    int i, pos;
    iType key;
    int count=0;

    srand(time(0));
    for (i=0; i<n; ++i)
    {
        key = rand()%100;  //generate random item in the range of 0 to 99

        pos = hash(a, n, key);

        printf("Generated item is: %d and its position is: %d\n", key, pos);
        a[pos] = key;

        show(a, n);
        getch();
    }
    printf("\n\nTotal count of collisions are: %d\n",collCount);
}

void readAndInsertKey(iType *a, int n)
{
    int i, pos;
    iType key;
    int count=0;

    for (i=0; i<n; ++i)
    {
        printf("Enter next key: ");
        scanf("%d", &key);

        pos = hash(a, n, key);
        printf("Generated item is: %d and its position is: %d\n", key, pos);
        a[pos] = key;

        show(a, n);
        getch();
    }
    printf("\n\nTotal count of collisions are: %d\n",collCount);
}

int search(iType *a, int n, iType value)
{
    int pos, i=0;

    srand(value);
    pos =  rand()%n;

    while (a[pos] != value && i<n) //collision occurred
    {
        pos = (pos+1)%n;
        ++i;
        printf("Searching next position: %d......\n", pos);
    }
    printf("Searching took %d comparisons\n", i);
    if (i==n) return -1;
    return pos;
}


