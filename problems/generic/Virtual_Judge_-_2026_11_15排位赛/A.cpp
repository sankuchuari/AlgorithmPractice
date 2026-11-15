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
                string s;cin>>s;

                int max{0};
                int cnt{0};
                for (int i{0};i<n;i++)
                {
                    if (s[i]=='#')
                    {
                        cnt++;
                    }

                    if (cnt>max)
                    {
                        max=cnt;
                    }


                    if (s[i]!='#')
                    {
                        cnt=0;
                    }
                }


                if (max%2==0)
                {
                    cout<<max/2<<endl;
                }
                else
                {
                    if (max==1)
                    {
                        cout<<"1"<<endl;
                    }
                    else
                    {
                        cout<<max/2 +1<<endl;
                    }
                }
            }
        }
    }

    return 0;
}
