#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (int t;cin>>t)
    {
        while (t--)
        {
            {
                int n,x,y;
                bool flag{true},yep{true};
                cin>>n>>x>>y;

                vector<int> v(n);
                vector<int> u;
                cin>>v[0];

                if (n==1)
                {
                    yep=true;
                }
                else
                {
                    for (int i=1;i<n;i++)
                    {
                        cin>>v[i];
                        if (v[i]<v[i-1]){flag=false;}
                    }
                    if (flag){cout<<"YES"<<endl;continue;}

                    for (int j=0;j<n;j++)u.push_back(abs(v[j]-j-1));

                    int ri =gcd(x,y);

                    for (int i=0;i<n;i++)
                    {
                        if (u[i]%ri!=0) yep=false;
                    }
                }

                if (yep){cout<<"YES"<<endl;}
                else{cout<<"NO"<<endl;}
            }
        }
    }

    return 0;
}
