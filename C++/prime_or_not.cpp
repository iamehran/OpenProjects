#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin>>n;
    int c=0;
    for(int i=1;i<=n;i++)
    {
        if(n%i==0)
        c++;
    }
    if(c==2)
    cout<<"Prime number"<<"\n";
    else
    cout<<"Not a prime number"<<"\n";
    return 0;
}
