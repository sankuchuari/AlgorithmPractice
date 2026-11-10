#include <bits/stdc++.h>
using namespace std;

static void solve()
{
    if (int n;cin >> n)
    {
        vector<int> a(n);

        for (auto& x:a) cin >> x;

        ranges::sort(a);

        int temp{a[0]};
        long long k_cnt{0};
        for (int i = 0; i < n-1; i++)
        {
            if (a[i+1] != temp)
            {
                temp = a[i+1];
                k_cnt+=1ll*((i+1<n-i-1)?i+1:n-i-1)*(a[i+1]-a[i]);
            }
        }

        cout<<k_cnt<<" "<<a[n-1]-a[0]<<endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (int t;cin>>t)
    {
        while (t--)
        {
            solve();
        }
    }
    return 0;
}