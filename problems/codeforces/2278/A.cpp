#include <bits/stdc++.h>
using namespace std;

static string ers(string& A, const string& B) {
    for (char ch : B)
    {
        size_t pos = A.find(ch);
        if (pos != string::npos)
        {
            A.erase(pos, 1);
        }
    }
    return A;
}

static void solve()
{
    int n,m;
    map<char,int> c;
    string p,q,res;
    res.reserve(p.size());
    if (cin >> n >> m >> p >> q && n-m==3)
    {
        res=ers(p, q);
        for (char ch : res)
        {
            c[ch]++;
        }
        if (c.size()==3 && c['s']==1 && c['i']==1 && c['x']==1)
        {
            cout<<"YES"<<endl;
        }
        else
        {
            cout<<"NO"<<endl;
        }
    }
    else
    {
        cout<<"NO"<<endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (int t; cin >> t)
    {
        while (t--)
        {
            solve();
        }
    }

    return 0;
}