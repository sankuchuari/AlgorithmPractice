#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (int t;cin >> t)
    {
        while (t--)
        {
            if (int n,k,ans{0};cin >> n >> k)
            {
                for (int i{1},a;i<=n&&cin>>a;++i)
                {
                    i%(k+1)==1?ans^=a&1:ans;
                }
                ans==0?cout<<"Bob\n":cout<<"Alice\n";
            }
        }
    }
    return 0;
}