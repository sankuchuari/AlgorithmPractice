#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (int m,d;cin>>m>>d)
    {
        string s;cin>>s;

        int cnt=m;
        bool flag[m];
        for (int i=0;i<m;i++){flag[i]=false;}

        for (int i=0;i<m;i++)
        {
            if (s[i]=='G')
            {
                for (int j=i-d>0?i-d:0;j<=(i+d<m-1?i+d:m-1);j++)
                {
                    if (!flag[j])
                    {
                        cnt--;
                        flag[j]=true;
                    }
                }
            }
        }

        cout<<cnt<<endl;
    }

    return 0;
}
