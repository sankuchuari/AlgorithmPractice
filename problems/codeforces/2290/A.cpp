#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (int t;cin>>t)
    {
        while (t--)
        {
            if (int a,b,c;cin>>a>>b>>c)
            {
                int max=(a>b ? a : b)>c?(a>b ? a : b):c;
                int min=(a<=b ? a : b)<=c?(a<=b ? a : b):c;
                int mid=a+b+c-max-min;
                if (max-mid==mid-min && max-mid==1){cout<<"YES"<<endl;}
                else{cout<<"NO"<<endl;}
            }
        }
    }

    return 0;
}
