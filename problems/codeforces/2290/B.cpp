#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (int t;cin>>t)
    {
        while (t--)
        {
            if (int n;cin>>n)
            {
                int num{0};
                if (string s = to_string(n);cin>>s)
                {
                    bool red=true;
                    for (auto c : s)
                    {
                        if (c=='B'&&red){num++;}
                        else if (c=='B'&&!red){red=true;}
                        else if (c=='R'&&!red){num++;}
                        else if (c=='R'&&red){red=false;}
                    }
                }
                cout<<num<<endl;
            }
        }
    }

    return 0;
}
