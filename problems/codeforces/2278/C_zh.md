<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">C. Math and Physics</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">2 seconds</span> | <b>memory:</b> <span style="color:#61AFEF;">256 megabytes</span> | <a href="https://codeforces.com/contest/2278/problem/C" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>个核芯按照从左到右的顺序依次编号为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>到<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>。第<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>个核芯初始质量为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">a<sub>i</sub></span>。

一次操作中，你可以选择一个核心<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>i</i> ≤ <i>k</i></span>，其中<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>k</i></span>是当前的核心数量），然后将其分裂成两个正整数部分<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>y</i></span>，使得<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> ≥ 1</span>，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>y</i> ≥ 1</span>，和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> + <i>y</i> = a<sub>i</sub></span>。

分隔后，序列中的第<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>个核心被移除，从而减少核心总数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>。移除的核心左侧邻居如果存在，其质量<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i></span>被添加；移除的核心右侧邻居如果存在，其质量<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>y</i></span>被添加。如果邻居不存在，则相应的质量会损失到环境中。

序列立即填补缺口。当无法进行进一步操作时，过程才会停止。

判断是否有可能最终只剩下唯一一个核心，如果可行，找出这个最终单个核心的最大可能质量。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

第一行输入包含一个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 10<sup>4</sup></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>），表示测试用例的数量。每个测试用例的描述随后给出。

第一行每个测试用例包含一个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2 ≤ <i>n</i> ≤ 2 · 10<sup>5</sup></span>) — 初始的核芯数量。

第二行每个测试用例包含<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">a<sub>1</sub>, a<sub>2</sub>, …, a<sub>n</sub></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ a<sub>i</sub> ≤ 1000</span>）——核心的初始质量。

保证所有测试用例中<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>的和不超过<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2 · 10<sup>5</sup></span>。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

对于每一组测试数据，打印一个整数 — 最终剩余核心的最大可能质量。如果无法最终剩下恰好一个核心，则打印<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">-1</span>。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#E06C75;">3</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#E06C75;">4</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#E06C75;">1 2 3 4</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">4</span><span style="color:#E06C75;">5</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">5</span><span style="color:#E06C75;">1 1 1 1 1</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">6</span><span style="color:#E06C75;">2</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">7</span><span style="color:#E06C75;">6 7</span></div></pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#98C379;"><span style="color:#98C379;">9</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#98C379;"><span style="color:#98C379;">-1</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#98C379;"><span style="color:#98C379;">12</span></span></div></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

考虑第一个测试用例。初始序列是<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[1, 2, 3, 4]</span>。一个最优的操作序列是：

* 将<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>分成<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> = 1</span>：序列变为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[1 + 1, 3 + 1, 4] = [2, 4, 4]</span>。
* 将第一个<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4</span>分成<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> = 1</span>,<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>y</i> = 3</span>: 序列变为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[2 + 1, 4 + 3] = [3, 7]</span>。
* 将<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">3</span>分割为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i>=1, <i>y</i>=2</span>。左侧的部分永久丢失，右侧的部分添加到核心部分。最终序列是<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[7 + 2] = [9]</span>。

现在只剩下了一个核心，它的质量为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">9</span>。可以证明这是最大的可能。

对于第二组测试案例，无法进行任何操作，因此不可能剩下唯一的核。因此，输出<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">-1</span>。

</div>