<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">A. Fraction and Six</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">1 second</span> | <b>memory:</b> <span style="color:#61AFEF;">256 megabytes</span> | <a href="https://codeforces.com/contest/2278/problem/A" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

你被给定了两个字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>，由小写字母组成。

解析字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>为分式分子中变量的乘积，解析字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>为分式分母中变量的乘积。每个字符代表一个变量。

由于乘法是可交换的，因此分子和分母中的变量可以任意重新排序。此外，分子和分母中都出现的变量可以相互抵消。请注意，分母中单个变量的出现只能与分子中相同个数的变量相互抵消，反之亦然。

判断是否可以通过简化分数使其结果恰好等于字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttsix</span>。换句话说，在进行任何次数的约简和重新排列后，分母中必须没有变量存在，而分子中的变量必须恰好形成字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttsix</span>。

例如，如果<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i>=textttsinx</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i>=textttn</span>，那么变量<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttn</span>可以被取消，留下<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttsix</span>在分子中。

![](https://espresso.codeforces.com/1ac4929438e4908210cb2bb8872c7d6702fcd18f.png)

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

第一行输入包含一个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 100</span>) — 测试用例的数量。每个测试用例的描述随后给出。

第一行每个测试用例包含两个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>m</i></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>n</i>, <i>m</i> ≤ 100</span>） — 字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>的长度，分别。

第二行每个测试用例包含一个字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>，表示分数的分子。保证该字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>的长度等于<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>，且仅包含小写英文字母。

第三行每个测试用例中包含一个字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>，表示分数的分母。保证规定该字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>的长度等于<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>m</i></span>且仅包含小写英文字母。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

对于每个测试用例，如果可以简化分数使得结果表达式恰好等于字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttsix</span>，则打印 "YES"，否则打印 "NO"。

你可以输出 "YES" 和 "NO" （例如，字符串 "yEs"，"yes" 和 "Yes" 也将被识别为积极响应）。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#E06C75;">5</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#E06C75;">4 1</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#E06C75;">sinx</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">4</span><span style="color:#E06C75;">n</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">5</span><span style="color:#E06C75;">6 7</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">6</span><span style="color:#E06C75;">xixsms</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">7</span><span style="color:#E06C75;">mixsxim</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">8</span><span style="color:#E06C75;">8 5</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">9</span><span style="color:#E06C75;">fixtures</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">10</span><span style="color:#E06C75;">frute</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">11</span><span style="color:#E06C75;">3 3</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">12</span><span style="color:#E06C75;">abc</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">13</span><span style="color:#E06C75;">def</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">14</span><span style="color:#E06C75;">5 10</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">15</span><span style="color:#E06C75;">sixty</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">16</span><span style="color:#E06C75;">codeforces</span></div></pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#98C379;"><span style="color:#E5C07B;font-weight:bold;">YES</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#98C379;"><span style="color:#61AFEF;font-weight:bold;">NO</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#98C379;"><span style="color:#E5C07B;font-weight:bold;">YES</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">4</span><span style="color:#98C379;"><span style="color:#61AFEF;font-weight:bold;">NO</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">5</span><span style="color:#98C379;"><span style="color:#61AFEF;font-weight:bold;">NO</span></span></div></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

在第一组测试案例中，变量 n 同时出现在分子和分母中，因此可以取消。分子中的剩余变量为 s, i, 和 x, 可以重新排列为六个。

在第二组测试案例中，在取消所有可能的公共变量后，分子中只剩下 s 而分母中只剩下 mi。因此，这个分数无法简化为六。

在第三组测试案例中，变量 f, r, u, t, 和 e 可以从等式的两边同时取消。等式分子中剩余的变量是 s, i, 和 x, 可以重新排列形成六个。

</div>