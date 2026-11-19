<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">F. Modulo and Counting</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">2 seconds</span> | <b>memory:</b> <span style="color:#61AFEF;">512 megabytes</span> | <a href="https://codeforces.com/contest/2278/problem/F" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

你被给定两个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span><span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>m</i></span>。

一个长度为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>的数组<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>a</i></span>被称为好数组，如果它满足以下两个条件：

*<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">colorredm + 2 ≥ a<sub>1</sub> ≥ a<sub>2</sub> ≥ … ≥ a<sub>n-1</sub> ≥ a<sub>n</sub> ≥ 1</span>;
*<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(a<sub>1</sub>  mod  a<sub>2</sub>) + (a<sub>2</sub>  mod  a<sub>3</sub>) + … + (a<sub>n-1</sub>  mod  a<sub>n</sub>) = <i>m</i></span>.

任务是找出所有好数组的数量。由于答案可能非常大，报告答案时对<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">998 244 353</span>取模。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

输入的第一行为一个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 2 000</span>)，表示测试用例的数量。每个测试用例的描述紧随其后。

每个测试用例的第一行包含两个用空格隔开的整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>m</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2 ≤ <i>n</i> ≤ 4 000</span>;<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>m</i> ≤ 4 000</span>)。

每个测试用例中<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>的总和不超过<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4000</span>，每个测试用例中<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>m</i></span>的总和不超过<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4000</span>。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

对于每个测试用例，打印好数组的数量。由于答案可能很大，输出它对<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">998 244 353</span>的模。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;color:#E06C75;">6
3 1
3 2
6 7
41 67
998 244
353 420</pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><span style="color:#98C379;">3</span>
<span style="color:#98C379;">1</span>
<span style="color:#98C379;">60</span>
<span style="color:#98C379;">972763487</span>
<span style="color:#98C379;">288208692</span>
<span style="color:#98C379;">566410295</span></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

对于第一个测试案例，好的数组是：

*<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[3, 2, 1]</span>:<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(3  mod  2) + (2  mod  1) = 1 + 0 = 1</span>。
*<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[3, 2, 2]</span>:<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(3  mod  2) + (2  mod  2) = 1 + 0 = 1</span>。<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[3, 3, 2]</span>:<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(3  mod  3) + (3  mod  2) = 0 + 1 = 1</span>。

对于第二组测试案例，唯一的良好数组是<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[4, 3, 2]</span>。

</div>