#include <bits/stdc++.h>
using namespace std;
#include <algorithm>
// bool findpath(vector<vector<bool>> maze, pair<int,int> previous,pair<int,int> next,pair<int,int> current,pair<int,int> destination,vector<pair<int,int>> &ans){
// if (current == destination){
//     for (auto a : ans){
//         //cout<< "("<<a.first<<","<<a.second<<")->";
//     }
//     //cout<<"\n";
//     return;
// }
// ans.push_back(current);
// // right
// int right = current.second+1;
// if (right < maze[0].size()){

// }

// }
bool isvalid(pair<int, int> &point, vector<vector<int>> &maze)
{
    if (point.first < 0 or point.first >= maze.size())
        return false;
    if (point.second < 0 or point.second >= maze[0].size())
        return false;
    if (maze[point.first][point.second])
    {
        return true;
    }
    return false;
}
string ans ="";
vector<string> sol{};
bool findPath(vector<vector<int>> &maze, pair<int, int> current, pair<int, int> destination)
{
    if (current == destination)
    {   
    //     cout<<"(0,0)";
    //     for (auto a : ans){
    //     cout<< "->("<<a.first<<","<<a.second<<")";
    // }
    // cout<<"\n";
    sol.push_back(ans);
        return true;
    }
bool result = false;
    vector<pair<int, int>> next;
    next.push_back(pair<int, int>(current.first - 1, current.second));
    next.push_back(pair<int, int>(current.first + 1, current.second));
    next.push_back(pair<int, int>(current.first, current.second - 1));
    next.push_back(pair<int, int>(current.first, current.second + 1));
    for (int k=0;k<4;k++)
    {
        auto point = next[k];
        if (isvalid(point, maze))
        {   
            char ch;
            switch (k)
            {
            case 0:ch='U';
                /* code */
                break;
            case 1:ch='D';
                /* code */
                break;
            case 2:ch='L';
                /* code */
                break;
            case 3:ch='R';
                /* code */
            default:
                break;
            }
            ans.push_back(ch);
            //cout<<""<<"("<<current.first<<","<<current.second<<")"<<"->"<< "("<<point.first<<","<<point.second<<") \n";
            maze[point.first][point.second] = 0;
            result =  findPath(maze, point, destination) or result;
            //cout<<"("<<current.first<<","<<current.second<<")"<<"<-"<<  "("<<point.first<<","<<point.second<<") \n";
            maze[point.first][point.second] = 1;
            ans.pop_back();
        }
        //return result;
    }
    return result;
}

int main(){

    vector<vector<int>> maze={
        {0, 1, 1, 1},
        {1, 1, 1, 0},
        {1, 0, 1, 1},
        {0, 0, 1, 1}
    };
    pair<int,int> current{0,0};
    pair<int,int> destination{maze.size()-1,maze[0].size()-1};
    if (maze[0][0]==0){
        sol.clear();
        return 0;
    }
    maze[0][0] = 0;
    bool s  = findPath(maze,current,destination);
    //sol.clear();
    sort(sol.begin(),sol.end());
    cout<<s;
}