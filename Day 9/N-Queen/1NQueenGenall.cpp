#include <bits/stdc++.h>
using namespace std;

void gen(vector<int> &arr, int r)
{

    if (r == 4)
    {
        for (auto i : arr)
        {
            cout << i << " ";
        }
        cout << "\n";
        return;
    }
    for (int i = 0; i < 4; i++)
    {
        arr[r] = i;
        gen(arr, r + 1);
    }
}
void gen(vector<int> &arr, int r, int num)
{
    arr[r] = num;
    if (r == 3)
    {
        for (auto i : arr)
        {
            cout << i << " ";
        }
        cout << "\n";
        return;
    }

    gen(arr, r + 1, 0);
    gen(arr, r + 1, 1);
    gen(arr, r + 1, 2);
    gen(arr, r + 1, 3);
}
int main()
{
    int x;
    //    cin >> x;
    //     cout <<" this is x " << x;
    vector<int> arr{0, 0, 0, 0};
    gen(arr, 0);
}