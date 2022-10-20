#include <iostream>
using namespace std;
int main()
{
    //here XOR( ^ ) operator operator is used

    int ans = 0, arr[5] = {1, 2, 3, 2, 1};


    for(int i=0; i<5; i++){
        ans = ans ^ arr[i];
    }

    cout<<ans;



    return 0;
}