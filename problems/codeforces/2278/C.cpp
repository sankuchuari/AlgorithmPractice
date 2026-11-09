#include <bits/stdc++.h>
using namespace std;
//My Solve
// void solve()
// {
//     if (int n;cin >> n)
//     {
//         vector<int> v(n);
//         int max_i{0},max_num{0};
//         for (int i = 0; i < n; i++)
//         {
//             if (int a; cin >> a)
//             {
//                 if (max_num <a || (max_num==a && n-i<i))
//                 {
//                     max_num = a;
//                     max_i = i;
//                 }
//                 v[i]=a;
//             }
//         }
//         if (max_num > 1)
//         {
//             int sum{0};
//             bool head{false},back{false},mid{false},loss{false};
//             if (max_i!=0)
//             {
//                 if (max_i!=1)
//                 {
//                     for (int i=0;i<max_i;i++)
//                     {
//                         sum += v[i];
//                         if (v[i]>1 && !head) head = true;
//                         if (v[i]==1 && head && !mid) mid = true;
//                     }
//                     if (!head)
//                     {
//                         sum=0;
//                     }
//                     else
//                     {
//                         if (v[0]>1 && mid)
//                         {
//                             sum-=2;
//                             mid=false;
//                         }
//                         else
//                         {
//                             sum-=1;
//                         }
//                     }
//                 }
//                 else
//                 {
//                     if (v[0]!=1)
//                     {
//                         sum+=v[0]-1;
//                     }
//                     else
//                     {
//                         if (n>2)
//                         {
//                             v[2]+=1;
//                             loss=true;
//                         }
//                     }
//                 }
//             }
//             if (max_i!=n-1)
//             {
//                 if (max_i!=n-2)
//                 {
//                     for (int i=n-1;i>max_i;i--)
//                     {
//                         sum+=v[i];
//                         if (v[i]>1 && !back) back = true;
//                         if (v[i]==1 && back && !mid) mid = true;
//                     }
//                     if (!back)
//                     {
//                         sum=0;
//                     }
//                     else
//                     {
//                         if (v[n-1]>1 && mid)
//                         {
//                             sum-=2;
//                         }
//                         else
//                         {
//                             sum-=1;
//                         }
//                     }
//                 }
//                 else
//                 {
//                     if (v[n-1]!=1)
//                     {
//                         sum+=v[n-1]-1;
//                     }
//                 }
//             }
//             if (n==3 && max_i==1 && !loss)
//             {
//                 sum+=1;
//             }
//             cout<<sum+v[max_i]<<endl;
//         }
//         else
//         {
//             cout << "-1" << endl;
//         }
//     }
// }

//wakanda-forever's solve
void solve()
{
    int n;
    cin >> n;

    vector<int> a(n);
    for(auto& z : a) cin >> z;

    int sum = accumulate(a.begin(), a.end(), 0);
    if(sum == n) cout << -1 << '\n';
    else if(sum == n - 2 + a[0] + a[n - 1]) cout << a[0] + a[n - 1] - 1 << '\n';
    else cout << sum - 1 << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (int t;cin >> t)
    {
        while(t--)
        {
            solve();
        }
    }

    return 0;
}
