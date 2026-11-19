<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">D. Letters Down</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">2 seconds</span> | <b>memory:</b> <span style="color:#61AFEF;">256 megabytes</span> | <a href="https://codeforces.com/contest/2290/problem/D" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

你被给定一个长度为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>仅由小写拉丁字母组成的字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>s</i></span>。

在一个操作中，你选择一个除了 a 以外的小写字母<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i></span>，并将<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i></span>中所有出现的字母替换为其前面的字母。例如，如果<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>s</i></span>，一个以<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>s</i> = bcab</span>为操作的字母序列会变成 bbab，随后一个以<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> = <i>c</i></span>为操作的字母序列会将所有的 b 替换为 a，变成 aaaa。如果<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> = <i>b</i></span>在<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i></span>中不存在，那么这个操作不会改变<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>s</i></span>。

找出将<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>s</i></span>变为 palindrome 所需的最小操作数。palindrome 是一个从左读和从右读都一样的字符串。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

每个测试包含多个测试用例。第一行包含测试用例的数量<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 10<sup>4</sup></span>）。测试用例的描述随后。

第一行每个测试用例中都包含一个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>n</i> ≤ 2· 10<sup>5</sup></span>） — 字符串的长度。

第二行每个测试用例包含一个长度为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>仅由小写拉丁字母组成的字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>s</i></span>。

保证所有测试用例中<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>的和不超过<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2· 10<sup>5</sup></span>。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

对于每个测试用例，打印一个整数 — 使<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>s</i></span>成为回文所需的最小操作数。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#E06C75;">5</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#E06C75;">4</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#E06C75;">abca</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">4</span><span style="color:#E06C75;">4</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">5</span><span style="color:#E06C75;">abdc</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">6</span><span style="color:#E06C75;">7</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">7</span><span style="color:#E06C75;">racecar</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">8</span><span style="color:#E06C75;">4</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">9</span><span style="color:#E06C75;">cbad</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">10</span><span style="color:#E06C75;">4</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">11</span><span style="color:#E06C75;">zaza</span></div></pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#98C379;"><span style="color:#98C379;">1</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#98C379;"><span style="color:#98C379;">3</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#98C379;"><span style="color:#98C379;">0</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">4</span><span style="color:#98C379;"><span style="color:#98C379;">2</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">5</span><span style="color:#98C379;"><span style="color:#98C379;">25</span></span></div></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

在第一组测试用例中，进行一次操作<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> = <i>c</i></span>，可以使字符串abca变成回文abba。

在第二组测试案例中，您可以使用<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> = <i>d</i></span>，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> = <i>c</i></span>，和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> = <i>b</i></span>进行操作： abdc<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">→</span>abcc<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">→</span>abbb<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">→</span>aaaa 。第二个操作改变了两个字母 c ，第三个操作改变了所有三个字母 b 。

在第三组测试案例中，字符串本身就是回文。

在第四组测试案例中，您可以使用<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> = <i>d</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> = <i>b</i></span>进行操作：cbad<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">→</span>cbac<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">→</span>caac。

在第五个测试用例中，按照<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> = <i>z</i>, <i>y</i>, …, <i>b</i></span>的顺序进行操作会将 zaza 转换为 aaaa。

</div>