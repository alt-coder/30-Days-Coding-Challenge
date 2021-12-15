#include<bits/stdc++.h>
using namespace std;

bitset<4> rows;
void gen(vector<int> &arr, int c)
{
    
    if (c == 4)
    {
        for (auto i : arr)
            {cout << i << " ";}
        cout << "\n";
        return;
    }
    for (int row = 0; row < 4; row++)
    {
        if (!rows[row]){
        arr[c] = row;
        rows[row]=1;
        gen(arr, c + 1);
        rows[row]=0;

        }
    }
}

int main(){
vector<int> arr{0, 0, 0, 0};
    gen(arr,0);
}