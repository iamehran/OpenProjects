#include<bits/stdc++.h>
using namespace std;

void graph(int n, int m, vector<int> adj[])
{
    for(int i=0;i<m;i++)
    {
        int x,y;
        cin>>x>>y;
        if(x<=n && y<=n)
        {
            adj[x].push_back(y);
            adj[y].push_back(x);
        }
    }
}

void traversalbfs(int n, int vis[],queue<int> q, vector<int>&bfs, vector<int> adj[]){
    while(!q.empty()){
        int node=q.front();
        q.pop();
        bfs.push_back(node);
        for(auto it:adj[node]){
            if(!vis[it])
            {
                vis[it]=1;
                q.push(it);
            }
        }
    }
}

void gprint(int n, vector<int> adj[]){
    for(int i=1;i<=n;i++){
        cout<<i<<" node : -> ";
        for(int j=0;j<adj[i].size();j++)
        {
            cout<<adj[i][j]<<" ";
        }
        cout<<endl;
    }
}

void print(vector<int>&v){
    for(int i=0;i<v.size();i++){
        cout<<v[i]<<" ";
    }
}

int main(){
    int n;
    cout<<"Enter no of nodes"<<endl;
    cin>>n;
    int m;
    cout<<"No of edges"<<endl;
    cin>>m;
    cout<<"Enter nodes b/w edges"<<endl;
    vector<int> adj[n+1];
    graph(n,m,adj);
    int vis[n+1]={0};
    vector<int> bfs;
    queue<int> q;
    q.push(1);
    vis[1]=1;
    traversalbfs(n,vis,q,bfs,adj);
    print(bfs);
    return 0;
}