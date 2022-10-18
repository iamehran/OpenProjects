#include <bits/stdc++.h>
using namespace std;
#define N 9

bool isSafe(int board[N][N], int row, int col, int num)
{

    // Checking in Row
    for (int d = 0; d < N; d++)
    {
        if (board[row][d] == num)
        {
            return false;
        }
    }

    // Checking in Column
    for (int d = 0; d < N; d++)
    {
        if (board[d][col] == num)
        {
            return false;
        }
    }

    // Checking in square
    int sq = sqrt(N);
    int rowStart = row - row % sq;
    int colStart = col - col % sq;
    for (int x = rowStart; x < rowStart + sq; x++)
    {
        for (int y = colStart; y < colStart + sq; y++)
        {
            if (board[x][y] == num)
            {
                return false;
            }
        }
    }

    return true;
}

bool canBeSolved(int board[N][N], int n)
{

    for (int num = 1; num <= 9; num++)
    {
        bool noneIsEmpty = true;
        int row = -1, col = -1;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (board[i][j] == 0)
                {
                    row = i;
                    col = j;
                    noneIsEmpty = false;
                    break;
                }
            }
            if (!noneIsEmpty)
                break;
        }
        if (noneIsEmpty)
        {
            return true;
        }
        if (isSafe(board, row, col, num))
        {
            board[row][col] = num;
            if (canBeSolved(board, n))
                return true;
            else
                board[row][col] = 0;
        }
    }
    return false;
}
int main()
{
    int grid[N][N] = {{3, 0, 6, 5, 0, 8, 4, 0, 0},
                      {5, 2, 0, 0, 0, 0, 0, 0, 0},
                      {0, 8, 7, 0, 0, 0, 0, 3, 1},
                      {0, 0, 3, 0, 1, 0, 0, 8, 0},
                      {9, 0, 0, 8, 6, 3, 0, 0, 5},
                      {0, 5, 0, 0, 9, 0, 6, 0, 0},
                      {1, 3, 0, 0, 0, 0, 2, 5, 0},
                      {0, 0, 0, 0, 0, 0, 0, 7, 4},
                      {0, 0, 5, 2, 0, 6, 3, 0, 0}};
    if (canBeSolved(grid, 9) == true)
        cout << "Possible\n";

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
            cout << grid[i][j] << " ";
        cout << "\n";
    }

    return 0;
}