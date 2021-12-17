#include <bits/stdc++.h>
using namespace std;

unordered_map<int,int> colors;

bool canColor(int node,int targetcolor,vector<vector<int>> &graph,unordered_map<int,int> &colors){

    for(int i =0; i < graph[0].size();i++){
        if(graph[node][i] and colors.find(i) != colors.end() and colors[i] == targetcolor){
            return false;
        }
    }
    return true;

}

void Fillcolor(vector<vector<int>> &graph, int M){

for(int i =0;i<graph.size(); i++){
    for(int j=0 ; j< graph[0].size();j++){
        if (graph[i][j] && colors.find(i) == colors.end()){
            for (int k=0; k < M; k++){
                if(canColor(i,k,graph,colors)){
                    colors[i]=k;
                    Fillcolor(graph,M);
                    colors.erase(i);
                }
            }
            return;
        }
    }
}
for(auto ans: colors){
    cout << ans.first <<" : "<< ans.second<<" \n";
}
cout<<"\n";


}

int main(){
    vector<vector<int>> graph ={
        {0, 1, 1, 1},
        {1, 0, 1, 0},
        {1, 1, 0, 1},
        {1, 0, 1, 0}
    };
    int M=3;
    Fillcolor(graph,M);

}