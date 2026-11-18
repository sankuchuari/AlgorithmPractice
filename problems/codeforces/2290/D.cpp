#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t)
    {
        while (t--)
        {
            int n;
            if (cin >> n)
            {
                string s;cin >> s;
                vector<vector<int>> u;
                int left = 0, right = n - 1;
                while (left < right)
                {
                    int a = s[left] - 'a';
                    int b = s[right] - 'a';

                    if (a != b)
                    {
                        u.push_back({min(a, b), max(a, b)});
                    }
                    left++;
                    right--;
                }
                if (u.empty())
                {
                    cout << 0 << "\n";
                    continue;
                }
                ranges::sort(u);

                int cnt = 0;
                int cur_start = u[0][0];
                int cur_end = u[0][1];

                for (size_t i = 1; i < u.size(); i++)
                {
                    if (u[i][0] <= cur_end)
                    {
                        cur_end = max(cur_end, u[i][1]);
                    }
                    else
                    {
                        cnt += (cur_end - cur_start);
                        cur_start = u[i][0];
                        cur_end = u[i][1];
                    }
                }
                cnt += (cur_end - cur_start);
                cout << cnt << "\n";
            }
        }
    }
    return 0;
}
