#include <bits/stdc++.h>
using namespace std;

void solve()
{
    vector<int> v;
    static string op{"PRS"};
    int sum{0};
    for (int i=0;i<3;i++)
    {
        if (int o;cin>>o)
        {
            sum+=o;
            v.push_back(o);
        }
    }
    auto p=ranges::max_element(v)-v.begin();
    while (sum--)
    {
        cout<<op[p];
    }
    cout<<endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (int t;cin>>t)
    {
        while(t--)
        {
            solve();
        }
    }

    return 0;
}
