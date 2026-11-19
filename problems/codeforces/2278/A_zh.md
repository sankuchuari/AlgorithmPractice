<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">A. Fraction and Six</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">1 second</span> | <b>memory:</b> <span style="color:#61AFEF;">256 megabytes</span> | <a href="https://codeforces.com/contest/2278/problem/A" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

你被给定两个由小写英文字母组成的字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>。

将字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>解读为分式分子中变量的乘积，将字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>解读为分式分母中变量的乘积。每个字符代表一个变量。

由于乘法是可交换的，分子和分母中的变量可以任意重新排序。此外，分子和分母中都出现的变量可以相互抵消。请注意，分母中单个变量的出现只能与分子中单个变量的出现相互抵消，反之亦然。

判断是否可以通过简化分数使其结果恰好等于字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttsix</span>。换句话说，在进行任何次数的约简和重新排列后，分母中必须没有变量存在，而分子中的变量必须恰好形成字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttsix</span>。

例如，如果<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i>=textttsinx</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i>=textttn</span>，那么变量<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttn</span>可以被取消，留下<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttsix</span>作为分子。

![](https://espresso.codeforces.com/1ac4929438e4908210cb2bb8872c7d6702fcd18f.png)

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

输入的第一行为一个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 100</span>)，表示测试用例的数量。每个测试用例的描述紧随其后。

每组测试的第一行包含两个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>m</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>n</i>, <i>m</i> ≤ 100</span>) — 分别表示字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>的长度。

第二行每个测试用例包含一个字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>，表示分数的分子。保证该字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>的长度等于<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>，并且只包含小写英文字母。

第三行每个测试用例包含一个字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>，表示分数的分母。保证则字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>的长度等于<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>m</i></span>且仅包含小写英文字母。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

对于每个测试用例，如果可以简化分数使得结果表达式恰好等于字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttsix</span>，则打印 "YES"，否则打印 "NO"。

可以以任何形式输出 "YES" 和 "NO" (例如，"yEs", "yes" 和 "Yes" 会被识别为积极响应)。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;color:#E06C75;">5
4 1
sinx
n
6 7
xixsms
mixsxim
8 5
fixtures
frute
3 3
abc
def
5 10
sixty
codeforces</pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><span style="color:#E5C07B;font-weight:bold;">YES</span>
<span style="color:#61AFEF;font-weight:bold;">NO</span>
<span style="color:#E5C07B;font-weight:bold;">YES</span>
<span style="color:#61AFEF;font-weight:bold;">NO</span>
<span style="color:#61AFEF;font-weight:bold;">NO</span></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

在第一组测试案例中，变量 n 同时出现在分子和分母中，因此可以取消。分子中剩余的变量是 s, i 和 x, 可以重新排序以得到六个。

在第二组测试案例中，在取消所有可能的公共变量后，分子中只剩下 s 而分母中只剩下 mi。因此，这个分数无法简化为六。

在第三组测试案例中，变量 f, r, u, t, 和 e 可以从等式两边同时取消。等式分子中剩余的变量是 s, i, 和 x, 可以重新排列成六个。

</div>