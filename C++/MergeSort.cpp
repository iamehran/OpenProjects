#include <iostream>

using namespace std;

void merge(int a[], int si, int ei){
    int mid = (si+ei)/2, size = ei-si+1;
    int n=mid+1, m=ei+1, i=si, j=mid+1, k=0, res[size];
    while(i<n && j<m){
        if(a[i]<a[j]){
            res[k] = a[i];
            i++;
            k++;
        }
        else{
            res[k] = a[j];
            j++;
            k++;
        }
    }
    
    if(i<n){
        for(int c=i; c<n; c++){
            res[k] = a[i];
            k++;
            i++;
        }
    }
    else if(j<m){
            for(int c=j; c<m; c++){
            res[k] = a[j];
            k++;
            j++;
        }
    }
    
    int s = si;
    for(int c=0; c<size; c++){
        a[s] = res[c];
        s++;
    }

}

void merge_sort(int a[], int si, int ei){
    if(si>=ei){
        return;
    }
    int mid = (si+ei)/2;
    merge_sort(a, si, mid);
    merge_sort(a, mid+1, ei);
    merge(a, si, ei);
}

int main()
{
    int a[100], n;
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    
    merge_sort(a, 0, n-1);
    
    for(int i=0; i<n; i++){
        cout<<a[i]<<" ";
    }

    return 0;
}