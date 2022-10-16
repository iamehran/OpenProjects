//by ssy2306 using Arrays
#include<iostream>
#include<string.h>  //12
using namespace std;
int mathmin(int a,int b)
{
    if(a>b)
    return b;
    else    
    return a;
}
int mathmax(int a,int b)
{
    if(a<b)
    return b;
    else    
    return a;
}
int rw(int a[],int length){
    int left[8],right[8];   //left[length], right[length]
    left[0]=a[0];
  right[7]=a[7]; //   right[length-1]=a[length-1];
    for(int i=1;i<length;i++){
        left[i]=mathmax(left[i-1],a[i]);
    }
    for(int i=length-2;i>=0;i--){
        right[i]=mathmax(right[i+1],a[i]);;
    }
    int answer=0;
    for(int i=0;i<length;i++)
    {
        answer+=(mathmin(left[i],right[i])-a[i]);
    }
    return answer;
}
int main(){
    int a[8]={3,1,2,4,0,1,3,2},length=8;
    int RainWaterCollected=rw(a,length);
    cout<<RainWaterCollected;
}
