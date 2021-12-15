#include <bits/stdc++.h>
using namespace std;
#define N 4
bitset<N> rows;
bitset<2 * N - 1> diag1, diag2;
void gen(vector<int> &arr, int c, int *ans)
{

    if (c == N)
    {
        for (auto i : arr)
        {
            cout << i + 1 << " ";
        }
        cout << "\n";
        *ans = *ans + 1;
        return;
    }
    for (int row = 0; row < N; row++)
    {
        if (!rows[row] && !diag1[row - c + (N - 1)] && !diag2[row + c])
        {
            arr[c] = row;
            rows[row] = diag1[row - c + (N - 1)] = diag2[row + c] = 1;
            gen(arr, c + 1, ans);
            rows[row] = diag1[row - c + (N - 1)] = diag2[row + c] = 0;
        }
    }
}

int main()
{
    vector<int> arr(N);
    int ans = 0;
    gen(arr, 0, &ans);
    cout << "total answers = " << ans;
}