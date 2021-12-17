#include <bits/stdc++.h>

using namespace std;

bool canFit(vector<vector<int>> &board, int r, int c, int num)
{
    for (int i = 0; i < 9; i++)
    {
        if (board[r][i] == num)
            return false;
    }
    for (int i = 0; i < 9; i++)
    {
        if (board[i][c] == num)
            return false;
    }
    r = r / 3;
    c = c / 3;
    r = 3 * r;
    c = 3 * c;
    for (int i = 0; i <  3; i++)
    {
        for (int j = 0; j <  3; j++)
        {
            if (board[i+r][j+c] == num)
                return false;
        }
    }
    return true;
}
void print(vector<vector<int>> &b)
{
    for (auto &a : b)
    {
        for (auto &c : a)
            cout << c << " ";
        cout << "\n";
    }
}

void sudoku(vector<vector<int>> &board)
{
    for (int r = 0; r < 9; r++)
    {
        for (int c = 0; c < 9; c++)
        {
            if (board[r][c] == 0)
            {
                for (int num = 1; num <= 9; num++)
                {
                    if (canFit(board, r, c, num))
                    {
                        board[r][c] = num;
                        sudoku(board);
                        board[r][c] = 0;
                    }
                }
                return;
            }
        }
    }
    print(board);
    int v;
    cout << "press 1 to look for more solution ";
    cin >>v;
    if (!v) exit(0);
}

int main(int argc, char const *argv[])
{
    /* code */
    vector<vector<int>> grid = 
//     {
//   { 5, 3, 0, 0, 7, 0, 0, 0, 0 },
//   { 6, 0, 0, 1, 9, 5, 0, 0, 0 },
//   { 0, 9, 8, 0, 0, 0, 0, 6, 0 },
//   { 8, 0, 0, 0, 6, 0, 0, 0, 3 },
//   { 4, 0, 0, 8, 0, 3, 0, 0, 1 },
//   { 7, 0, 0, 0, 2, 0, 0, 0, 6 },
//   { 0, 6, 0, 0, 0, 0, 2, 8, 0 },
//   { 0, 0, 0, 4, 1, 9, 0, 0, 5 },
//   { 0, 0, 0, 0, 8, 0, 0, 0, 0 } 
// };
{
  {5,3,0,0,7,0,0,0,0},
  {6,0,0,1,9,5,0,0,0},
  {0,9,8,0,0,0,0,6,0},
  {8,0,0,0,6,0,0,0,3},
  {4,0,0,8,0,3,0,0,1},
  {7,0,0,0,2,0,0,0,6},
  {0,6,0,0,0,0,2,8,0},
  {0,0,0,4,1,9,0,0,5},
  {0,0,0,0,8,0,0,0,0},
};
    cout << canFit(grid,0,3,6);
    sudoku(grid);

    return 0;
}
