#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (int t;cin>>t)
    {
        while(t--)
        {
            if (int n;cin>>n)
            {
                vector<int> v(n);
                vector<int> e;
                vector<int> f;
                int cnt{0};
                for (auto& i : v)cin>>i;
                ranges::sort(v);
                int last={0};
                for (int i=n-1;i>=0;i--)
                {
                    if (last==v[i])
                    {
                        if (e.size()>0)
                        {
                            if (v[i]<e[e.size()-1]){cnt++;}
                        }
                        e.push_back(v[i]);
                    }
                    else
                    {
                        if (e.size()>0)
                        {
                            if (v[i]<e[0]){cnt++;}
                        }
                        f.push_back(v[i]);
                        if (last==0)
                        {
                            e.push_back(v[i]);
                        }
                    }
                    last=v[i];
                }
                if (n>1)
                {
                    if (v[n-1]==v[n-2]){cnt+=2;}
                    else if (v[n-1]>v[n-2]){cnt++;}
                }
                if (n==1){cnt++;}

                cout<<cnt<<endl;

                for (int i=f.size()-1;i>=0;i--){cout<<f[i]<<" ";}
                for (int i=1;i<=e.size()-1;i++){cout<<e[i]<<" ";}
                cout<<endl;
            }
        }
    }

    return 0;
}
